-- Day 29 SQL – Window Functions + Ranking

-- Schema:
-- employees(id, name, salary, dept_id)
-- departments(dept_id, dept_name)

-- Rank employees by salary within each department
SELECT
    name,
    dept_id,
    salary,
    RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS salary_rank
FROM employees;

-- Top 2 highest paid employees per department with department name
SELECT
    e.name,
    d.dept_name,
    e.salary
FROM (
    SELECT
        *,
        DENSE_RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS rnk
    FROM employees
) e
JOIN departments d
    ON e.dept_id = d.dept_id
WHERE e.rnk <= 2;

-- Employees earning more than their department average (window function)
SELECT
    name,
    dept_id,
    salary
FROM (
    SELECT
        name,
        dept_id,
        salary,
        AVG(salary) OVER (PARTITION BY dept_id) AS dept_avg
    FROM employees
) t
WHERE salary > dept_avg;

-- Third highest salary in the company
SELECT salary
FROM (
    SELECT
        salary,
        DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
    FROM employees
) ranked
WHERE rnk = 3;