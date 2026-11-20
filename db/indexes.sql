CREATE INDEX idx_accounts_user_id on accounts(user_id);
CREATE INDEX idx_transactions_source_time on transactions(source_account_id ,created_at DESC);
CREATE INDEX idx_transactions_destination_time on transactions(destination_account_id,created_at DESC);
