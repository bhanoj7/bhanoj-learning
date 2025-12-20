-- Day 28 SQL Tasks – JOIN + GROUP BY + FILTERING (Single Paste)

-- Schema:
-- employees(id, name, salary, dept_id)
-- departments(dept_id, dept_name)

-- Task 1: Departments where average salary is above 60000
SELECT
    d.dept_name,
    AVG(e.salary) AS avg_salary
FROM employees e
JOIN departments d
    ON e.dept_id = d.dept_id
GROUP BY d.dept_name
HAVING AVG(e.salary) > 60000;

-- Task 2: Employees earning more than the average salary of their department
SELECT
    e.name,
    e.salary,
    d.dept_name
FROM employees e
JOIN departments d
    ON e.dept_id = d.dept_id
WHERE e.salary > (
    SELECT AVG(salary)
    FROM employees
    WHERE dept_id = e.dept_id
);

-- Task 3: Highest salary employee in each department (name + salary)
SELECT
    d.dept_name,
    e.name,
    e.salary
FROM employees e
JOIN departments d
    ON e.dept_id = d.dept_id
WHERE (e.dept_id, e.salary) IN (
    SELECT dept_id, MAX(salary)
    FROM employees
    GROUP BY dept_id
);

-- Task 4: Count employees in each department (sorted highest to lowest)
SELECT
    d.dept_name,
    COUNT(e.id) AS total_employees
FROM employees e
JOIN departments d
    ON e.dept_id = d.dept_id
GROUP BY d.dept_name
ORDER BY total_employees DESC;

-- Task 5: Second highest salary from each department
SELECT
    dept_id,
    salary
FROM (
    SELECT
        dept_id,
        salary,
        DENSE_RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS rnk
    FROM employees
) ranked
WHERE rnk = 2;