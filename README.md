# Banking Transaction API

A learning-focused REST API for managing simulated bank accounts and transfers, built with **Python, FastAPI, PostgreSQL, and psycopg**. The goal is to practice relational database design, safe money movement, and reliable backend engineering.

> **Educational project only.** All customers, accounts, and transactions are fictional. No real funds, banking credentials, or payment integrations are involved.

## Features (planned)

- Create and retrieve users and accounts
- Check account balances
- Deposit and withdraw simulated funds
- Transfer funds between accounts atomically
- Retrieve transaction history with pagination
- Validate inputs and handle domain errors
- Test transfer correctness and concurrent requests

## Tech stack

| Layer | Technology |
| --- | --- |
| Language | Python |
| API | FastAPI |
| Database | PostgreSQL |
| Database driver | psycopg 3 |
| Validation | Pydantic |
| Tests | pytest |

## Database design

```text
users (1) ──────< accounts (many)
                       │
                       ├──< transactions.source_account_id
                       └──< transactions.destination_account_id
```

- **users:** customer identity and contact information
- **accounts:** owner, account type, currency, status, and current balance
- **transactions:** immutable record of deposits, withdrawals, and transfers

Money uses `NUMERIC(14,2)` in PostgreSQL; use Python `Decimal` in application code.

## Starter data

| File | Records | Description |
| --- | ---: | --- |
| `users.csv` | 20 | Fictional customers |
| `accounts.csv` | 25 | Accounts, including 5 customers with two accounts |
| `transactions.csv` | 100 | Deposits, withdrawals, and transfers |

All accounts begin with an **implicit opening balance of 10,000.00 MAD** before the sample transaction history. The balances in `accounts.csv` represent the **final balances after all 100 transactions**. The opening balance is not recorded as a transaction. This is a fixture for learning, not a complete accounting ledger.

## Import sample data

Create a PostgreSQL database and run the following commands from the project directory:

```bash
psql -d banking_api -f schema.sql
psql -d banking_api -f seed.sql
```

The `seed.sql` script uses PostgreSQL `psql`'s `\copy` command and expects the CSV files in the current directory. It is intended for a **fresh, empty database**. The seed files populate tables directly; they do not call the API.

## Suggested API routes

| Method | Endpoint | Purpose |
| --- | --- | --- |
| GET | `/health` | Health check |
| POST | `/users` | Create user |
| POST | `/accounts` | Open account |
| GET | `/accounts/{account_id}` | Account details |
| GET | `/accounts/{account_id}/balance` | Current balance |
| POST | `/accounts/{account_id}/deposits` | Deposit funds |
| POST | `/accounts/{account_id}/withdrawals` | Withdraw funds |
| POST | `/transfers` | Transfer funds |
| GET | `/accounts/{account_id}/transactions` | Paginated history |

These endpoints are a **roadmap**, not implemented code.

## Implementation milestones

1. Design and query the database with raw SQL.
2. Implement read-only FastAPI routes.
3. Add deposits and withdrawals with validation.
4. Implement atomic transfers with `COMMIT`/`ROLLBACK`.
5. Add row-level locking and idempotency safeguards.
6. Add automated tests, migrations, and Docker if needed.

## Critical engineering rules

- A transfer must debit one account and credit the other in **one database transaction**.
- Never allow a negative balance or a nonpositive transaction amount.
- Protect against simultaneous requests spending the same balance.
- Reject duplicate transfer requests using an idempotency key.
- Treat transaction records as immutable after successful posting.
- Do not trust account IDs or amounts without server-side validation.
- Do not expose account data to arbitrary users; add authentication/authorization before any nonlocal deployment.

## Future improvements

- Replace the simplified transaction log with a **double-entry ledger**.
- Add authentication and account ownership checks.
- Introduce Alembic migrations, integration tests, and Docker.
- Add audit trails, reconciliation, and observability.

## Status

**Planning / database seed prepared.** Backend implementation is the next step.

## License

Choose a license before public distribution.
