-- **Task 1 — List each employee with their department name**


SELECT e.id, e.name, d.dept_name, e.salary
FROM employees e
JOIN departments d
ON e.dept_id = d.id;

**WHY:** Most APIs require joining employee → department.

---

-- **Task 2 — Count employees in each department**

SELECT d.dept_name, COUNT(*) AS total_employees
FROM employees e
JOIN departments d ON e.dept_id = d.id
GROUP BY d.dept_name;

---

-- **Task 3 — Average salary per department**

-
SELECT d.dept_name, AVG(e.salary) AS avg_salary
FROM employees e
JOIN departments d ON e.dept_id = d.id
GROUP BY d.dept_name;


-- **Task 4 — Highest earning employee in each department**

SELECT d.dept_name, MAX(e.salary) AS highest_salary
FROM employees e
JOIN departments d ON e.dept_id = d.id
GROUP BY d.dept_name;

---

-- **Task 5 — Departments with more than 2 employees**


SELECT d.dept_name, COUNT(*) AS total
FROM employees e
JOIN departments d ON e.dept_id = d.id
GROUP BY d.dept_name
HAVING COUNT(*) > 2;


---

- WH-Questions 

--- **WHAT are JOINs?**

A way to combine data from related tables.

--- **WHY do we use JOINs?**

Real systems split data into multiple tables to avoid duplication.

--- **WHEN to use INNER JOIN?**

When matching rows MUST exist in both tables.

--- **WHERE is aggregation used?**

Dashboards, analytics, reporting, salary analysis.

--- **HOW does GROUP BY work?**

Groups rows by a column; aggregation runs on each group.

---

- Sticky Notes

```
JOIN = connect tables
GROUP BY = group rows
HAVING = filter groups
WHERE = filter rows
Always join employees.dept_id → departments.id
```

