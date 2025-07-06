-- Keep a log of any SQL queries you execute as you solve the mystery.
SELECT * FROM atm_transactions
SELECT * FROM crime_scene_reports WHERE street='Humphrey Street'AND year=2023 AND month=7;
SELECT * FROM bakery_security_logs WHERE year=2023 AND month=7;
SELECT * FROM bakery_security_logs WHERE license_plate='5209A97'
SELECT license_plate
FROM bakery_security_logs
WHERE day = 26
GROUP BY license_plate
HAVING COUNT(license_plate) = 2;
SELECT * FROM interviews WHERE month=7 AND day = 27;
SELECT * FROM interviews WHERE id=295;
SELECT * FROM interviews WHERE id=254;
SELECT * FROM interviews WHERE transcript LIKE '%thief%';
SELECT * FROM people WHERE license_plate='5209A97';
SELECT * FROM atm_transactions WHERE atm_location='Leggett Street' AND day=27 AND transaction_type='withdraw';
SELECT * FROM bank_accounts JOIN atm_transactions ON atm_transactions.account_number=bank_accounts.account_number
WHERE atm_transactions.atm_location='Leggett Street' AND atm_transactions.day=27 AND atm_transactions.transaction_type='withdraw';
