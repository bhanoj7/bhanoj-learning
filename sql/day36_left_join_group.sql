-- Base query: count employees per department (include empty departments)
SELECT
    d.dept_name,
    COUNT(e.id) AS emp_count
FROM departments d
LEFT JOIN employees e
    ON d.id = e.dept_id
GROUP BY d.dept_name;

-- Variation 1: Departments with more than 2 employees
SELECT
    d.dept_name,
    COUNT(e.id) AS emp_count
FROM departments d
LEFT JOIN employees e
    ON d.id = e.dept_id
GROUP BY d.dept_name
HAVING COUNT(e.id) > 2;

-- Variation 2: Departments with NO employees
SELECT
    d.dept_name,
    COUNT(e.id) AS emp_count
FROM departments d
LEFT JOIN employees e
    ON d.id = e.dept_id
GROUP BY d.dept_name
HAVING COUNT(e.id) = 0;
