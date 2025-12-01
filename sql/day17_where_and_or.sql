SELECT * FROM employees WHERE salary BETWEEN 50000 AND 80000;
SELECT * FROM employees WHERE department = 'HR' OR department='IT';
SELECT * FROM employees WHERE department <> 'HR';
SELECT * FROM employees WHERE name LIKE 'B%';
SELECT * FROM employees WHERE salary > 60000 AND department='IT';