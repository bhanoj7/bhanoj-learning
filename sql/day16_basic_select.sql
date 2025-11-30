-- Day 16 — Basic SELECT and WHERE practice
-- Date: 2025-11-29
-- Database: learning_db
-- Topic: SELECT, WHERE, LIMIT

SELECT * FROM employees;
SELECT name, salary FROM employees;
SELECT * FROM employees WHERE salary > 50000;
SELECT * FROM employees WHERE department = 'HR';
SELECT * FROM employees ORDER BY salary DESC LIMIT 3;
