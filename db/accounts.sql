CREATE TABLE IF NOT EXISTS accounts(
  account_id INTEGER PRIMARY KEY ,
  user_id INTEGER NOT NULL references users(user_id),
  account_type TEXT NOT NULL check(account_type in ('checking','savings')),
  currency CHAR(3) NOT NULL default 'MAD' check (currency='MAD'),
  status TEXT NOT NULL check (status in ('active','frozen','closed')),
  created_at TIMESTAMP NOT NULL ,
  balance NUMERIC(14,2) NOT NULL check (balance>=0)
);
