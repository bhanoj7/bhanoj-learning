SELECT department,COUNT(*) FROM employees GROUP BY department;
SELECT department,AVG(salary) FROM employees GROUP BY department;
SELECT department,MAX(salary) FROM employees GROUP BY department;
SELECT department,COUNT(*) FROM employees WHERE salary > 90000 GROUP BY department;
