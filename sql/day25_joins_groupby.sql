------- Create the new table -------
CREATE TABLE departments (
	id SERIAL PRIMARY KEY,
	dept_name VARCHAR(50)
);
-------- Insert sample rows --------
INSERT INTO departments (dept_name)
VALUES ('Engineering'), ('HR'), ('Finance'), ('Sales');
----- Check Table ------
SELECT * FROM departments;
SELECT * FROM employees;
---- Removing department column for adding dept_id ----
ALTER TABLE employees DROP COLUMN department;
----- Upadted employees table ------------------
UPDATE employees SET dept_id = 1 WHERE id IN (1,3,4,7);
UPDATE employees SET dept_id = 2 WHERE id IN (2,6);
UPDATE employees SET dept_id = 3 WHERE id IN (5);
------- Task 1 : INNER JOIN ---------
SELECT e.id, e.name, e.salary, d.dept_name FROM employees e INNER JOIN departments d ON e.dept_id = d.id;
----- TASK 2: LEFT JOIN ------
SELECT e.id, e.name, e.salary, d.dept_name FROM employees e LEFT JOIN departments d ON e.dept_id = d.id;
------ Task 3: Count Per Department ----
SELECT d.dept_name, COUNT(e.id) AS employee_count FROM departments d LEFT JOIN employees e ON d.id = e.dept_id GROUP BY d.dept_name;
----- Task 4: Max salary per department ---
SELECT d.dept_name, MAX(e.salary) AS highest_salary FROM departments d LEFT JOIN employees e ON d.id = e.dept_id GROUP BY d.dept_name;
---- Task 5: AVG salary per department ---
SELECT d.dept_name, AVG(e.salary) AS average_salary FROM departments d LEFT JOIN employees e ON d.id = e.dept_id GROUP BY d.dept_name;
