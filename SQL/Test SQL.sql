

-- Create the database
CREATE DATABASE Company;

-- Use the database
USE Company;

-- Create the Employees table
CREATE TABLE Employees (
    id INT PRIMARY KEY,
    Name VARCHAR(50),
    Salary INT,
    Department VARCHAR(50),
    Location VARCHAR(50)
);

-- Insert values into the Employees table
INSERT INTO Employees (id, Name, Salary, Department, Location) VALUES
(1, 'Anup', 10000, 'Dev', 'Pune'),
(2, 'Rani', 26000, 'Test', 'Nashik'),
(3, 'Jay', 18000, 'Dev', 'Nagpur'),
(4, 'Vishal', 22000, 'Support', 'Pune'),
(5, 'Shina', 35000, 'Test', 'Nagpur'),
(6, 'Rony', 11000, 'Support', 'Nagpur'),
(7, 'Pooja', 38000, 'Dev', 'Nashik');

select * from Employees;

-- . What are the names of all employees?--
select name from employees;

-- 2. How many employees are there in total? --
select count(*) as employee_count from employees;

-- 3. What departments do the employees work in? -- 
select name,department from employees;

-- 4. How many employees work in each department? --
select department,count(id) from employees group by department;

-- 5. Who is the highest-paid employee? --
select * from employees order by SALARY DESC limit 1;

-- 6.  Who is the lowest-paid employee? --
SELECT * FROM EMPLOYEES ORDER BY SALARY ASC LIMIT 1;

-- 7. How many employees earn more than RS 20000 per year? --
SELECT * FROM EMPLOYEES WHERE SALARY>20000;

-- 8. What is the average salary of all employees? --
SELECT AVG(SALARY) AS AVG_SALARY FROM EMPLOYEES;

-- 9. Who are the top 5 highest-paid employees? --
SELECT * FROM EMPLOYEES ORDER by SALARY desc LIMIT 5;

-- 10. Who are the employees in the Marketing department? --
SELECT * FROM EMPLOYEES WHERE DEPARTMENT="Marketing";

-- 11. How many employees have a salary between RS 15000 and RS 25000? --
select * from employees where salary between 15000 and  25000;

-- 12. Who are the employees with a salary of NULL? --
select * from employees where salary is null;

-- 13. Who are the employees with a first name starting with "J"? --
select * from employees where name like 'J%';
select * from employees;

-- 14. What are the salaries of all employees sorted in descending order? --
select * from employees order by salary desc;

-- 15. What is the total salary expenditure of the company? --
select sum(salary) as total_expenses from employees;

-- 16. Who are the employees with the same first names? -- 
SELECT Name
FROM Employees
GROUP BY Name
HAVING COUNT(*) > 1;

-- 17 . How many employees are there in Pune location? --
select * from employees where location="pune";
select count(*)as Count_employees from employees where location="pune";

-- 18. What is the average salary of employees in Dev department? --
select avg(salary) from employees where department="Dev";

-- 19. Who are the employees with salaries above the average? --
select * from employees where salary>(select avg(salary) from employees);

-- 20. Who are the employees with the lowest salary in Test department?
SELECT * FROM employees WHERE department = 'Test' AND salary = (SELECT MIN(salary) FROM employees WHERE department = 'Test');

-- 21. How many employees were hired in 2023 year? --
select count(*) from employees ;

-- 22. Who are the employees hired in the year 2023? --
select name from employees;

-- What is the total salary expenditure in Dev and Support department? --
select sum(salary) from employees where department="Dev" or department="Support";

-- 24. Who are the employees with a salary greater than the average salary of Dev department? --

select * from employees where salary>(select avg(salary) from employees where department="dev") ;

-- 25. What is the total salary expenditure in Pune location? --
select sum(salary) from employees where location = "pune";






