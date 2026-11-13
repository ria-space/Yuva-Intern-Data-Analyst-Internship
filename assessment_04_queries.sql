-- Change the table name if your MySQL table uses a different name.
-- 1. Total transaction count
SELECT COUNT(*) AS total_transactions FROM upi_transactions;

-- 2. Flagged transaction count and percentage
SELECT COUNT(*) AS total_transactions,
       SUM(fraud_flag = 1) AS flagged_transactions,
       ROUND(100.0 * SUM(fraud_flag = 1) / COUNT(*), 3) AS flagged_rate_percent
FROM upi_transactions;

-- 3. Transaction summary by type
SELECT transaction_type, COUNT(*) AS transaction_count,
       SUM(fraud_flag = 1) AS flagged_count
FROM upi_transactions
GROUP BY transaction_type
ORDER BY transaction_count DESC;

-- 4. Average amount by device
SELECT device_type, ROUND(AVG(amount_inr),2) AS average_amount,
       COUNT(*) AS transaction_count
FROM upi_transactions
GROUP BY device_type;

-- 5. Null checks for selected columns
SELECT SUM(transaction_id IS NULL) AS null_ids,
       SUM(amount_inr IS NULL) AS null_amounts,
       SUM(transaction_type IS NULL) AS null_types
FROM upi_transactions;
