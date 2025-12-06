SELECT * FROM employees WHERE salary > (SELECT AVG(salary) FROM employees);
SELECT department,SUM(salary) FROM employees GROUP BY department HAVING(SUM(salary))>150000;
SELECT name, salary, department FROM employees e WHERE salary = (SELECT MAX(salary) FROM employees WHERE department=e.department);
SELECT * FROM employees WHERE salary > ALL (SELECT salary FROM employees WHERE department = 'HR');
SELECT * FROM employees WHERE salary > (SELECT MAX(salary) FROM employees WHERE department = 'HR');
SELECT * FROM employees WHERE department IN (SElECT department FROM employees GROUP BY department HAVING(COUNT(*)>2));