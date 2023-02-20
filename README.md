# devops_microservices
Creating basic microservices in python with PostgreSQL database

Task: create new table transactions_konakbayev with the following columns:
- id (int, primary key)
- description(varchar)
- price_kzt (int)
- quantity (int)
- amount (int)
- price_usd (int)
- date (timestamp)

Services:
1) Create a new transaction every minute
2) Read all transactions from database and multiply price by quantity
3) Read all transactions from database and multiply amount by currency of USD to get price_usd
