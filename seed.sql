-- Run after schema.sql from psql in the project root.
-- Opening balance was 10,000 MAD for each account before these 100 events.
\copy users(user_id, full_name, email, created_at) FROM 'users.csv' WITH (FORMAT csv, HEADER true);
\copy accounts(account_id, user_id, account_type, currency, status, created_at, balance) FROM 'accounts.csv' WITH (FORMAT csv, HEADER true);
\copy transactions(transaction_id, transaction_type, source_account_id, destination_account_id, amount, created_at, reference) FROM 'transactions.csv' WITH (FORMAT csv, HEADER true, NULL '');
