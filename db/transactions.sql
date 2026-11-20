CREATE TABLE IF NOT EXISTS transactions(
  transaction_id INTEGER  GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  transaction_type TEXT NOT NULL check(transaction_type in ('deposit','withdrawal','transfer')),
  source_account_id INTEGER REFERENCES accounts(account_id),
  destination_account_id INTEGER REFERENCES accounts(account_id) ,
  amount NUMERIC (14,2) NOT NULL  check(amount>0),
  created_at TIMESTAMP NOT NULL DEFAULT NOW() ,
  reference TEXT NOT NULL unique,
  CHECK((transaction_type='deposit' and source_account_id is NULL and destination_account_id is NOT NULL )
  OR 
  (transaction_type='withdrawal' and source_account_id is not NULL and destination_account_id is  NULL )
  OR 
 (transaction_type='transfer' and source_account_id is not NULL and destination_account_id is NOT NULL  
 and source_account_id<>destination_account_id)));
