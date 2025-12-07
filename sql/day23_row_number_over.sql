SELECT name, salary, ROW_NUMBER() OVER (ORDER BY salary DESC) AS ranking FROM employees;
SELECT NAME, DEPARTMENT, SALARY, ROW_NUMBER() OVER
(PARTITION BY department ORDER BY salary DESC) AS depart_ranking FROM employees;
WITH ranked AS (
  SELECT name, department, salary,
         ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS rnk
  FROM employees
)
SELECT * FROM ranked WHERE rnk = 1;
WITH ranked AS (
SELECT name, department, salary, ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary ASC) AS rnk
FROM employees
)
SELECT * FROM RANKED WHERE RNK = 1;