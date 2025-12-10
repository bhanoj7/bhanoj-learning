--- Return all employees with salary greater than 50,000. ---
SELECT *
FROM employees
WHERE salary > 50000;

---- Pattern Matching: Return all employees whose name starts with 'S' -------------

SELECT *
FROM employees
WHERE name LIKE 'S%';

--- Task 3 - DISTINCT values : Return the list of unique department IDs from employees. ----

SELECT DISTINCT dept_id
FROM employees;

---- Task 4 - BETWEEN : Return employees with salary between 40,000 and 70,000. ------

SELECT *
FROM employees
WHERE salary BETWEEN 40000 AND 70000;

--- Return employees:In HR department With salary above 60,000 And name ends with 'a'
SELECT e.name, e.salary, d.dept_name
FROM employees e
JOIN departments d ON e.dept_id = d.id
WHERE d.dept_name = 'HR'
  AND e.salary > 60000
  AND e.name LIKE '%a';
