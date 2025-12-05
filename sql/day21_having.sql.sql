SELECT department,COUNT(*) FROM employees GROUP BY department HAVING COUNT(*)>2;
SELECT department,avg(salary) FROM employees GROUP BY department HAVING avg(salary) > 70000;
SELECT department,max(salary) FROM employees GROUP BY department order by max(salary) desc;
SELECT department,COUNT(*) FROM employees GROUP BY department order by COUNT(*) desc;