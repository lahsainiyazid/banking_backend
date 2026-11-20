-- Educational simulation only: no real banking use.
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    full_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    created_at TIMESTAMP NOT NULL
);

CREATE TABLE accounts (
    account_id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(user_id),
    account_type TEXT NOT NULL CHECK (account_type IN ('checking', 'savings')),
    currency CHAR(3) NOT NULL DEFAULT 'MAD' CHECK (currency = 'MAD'),
    status TEXT NOT NULL CHECK (status IN ('active', 'frozen', 'closed')),
    created_at TIMESTAMP NOT NULL,
    balance NUMERIC(14,2) NOT NULL CHECK (balance >= 0)
);

CREATE TABLE transactions (
    transaction_id INTEGER PRIMARY KEY,
    transaction_type TEXT NOT NULL CHECK (transaction_type IN ('deposit','withdrawal','transfer')),
    source_account_id INTEGER REFERENCES accounts(account_id),
    destination_account_id INTEGER REFERENCES accounts(account_id),
    amount NUMERIC(14,2) NOT NULL CHECK (amount > 0),
    created_at TIMESTAMP NOT NULL,
    reference TEXT NOT NULL UNIQUE,
    CHECK (
      (transaction_type = 'deposit' AND source_account_id IS NULL AND destination_account_id IS NOT NULL) OR
      (transaction_type = 'withdrawal' AND source_account_id IS NOT NULL AND destination_account_id IS NULL) OR
      (transaction_type = 'transfer' AND source_account_id IS NOT NULL AND destination_account_id IS NOT NULL AND source_account_id <> destination_account_id)
    )
);

CREATE INDEX idx_accounts_user_id ON accounts(user_id);
CREATE INDEX idx_transactions_source_time ON transactions(source_account_id, created_at DESC);
CREATE INDEX idx_transactions_destination_time ON transactions(destination_account_id, created_at DESC);
