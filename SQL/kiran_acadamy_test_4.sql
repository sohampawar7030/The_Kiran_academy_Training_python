use oops;
CREATE TABLE Departments (
    id INT PRIMARY KEY,
    name VARCHAR(50)
);

-- 2. Create Locations Table
CREATE TABLE Locations (
    id INT PRIMARY KEY,
    city VARCHAR(50)
);

-- 3. Create Employees Table
CREATE TABLE Employees (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    salary INT,
    department_id INT,
    location_id INT,
    hire_date DATE,
    FOREIGN KEY (department_id) REFERENCES Departments(id),
    FOREIGN KEY (location_id) REFERENCES Locations(id)
);

-- Insert data into Departments
INSERT INTO Departments (id, name) VALUES
(1, 'Marketing'),
(2, 'Development'),
(3, 'Support');

-- Insert data into Locations
INSERT INTO Locations (id, city) VALUES
(1, 'Pune'),
(2, 'Mumbai');

-- Insert data into Employees
INSERT INTO Employees (id, name, salary, department_id, location_id, hire_date) VALUES
(1, 'Alice', 25000, 1, 1, '2022-01-15'),
(2, 'Bob', 22000, 1, 2, '2022-02-20'),
(3, 'Charlie', 28000, 2, 1, '2022-03-10'),
(4, 'David', 20000, 2, 2, '2022-04-05'),
(5, 'Eve', 30000, 1, 1, '2023-01-07');



select * from Departments;

select * from Employees;

select * from Locations;


-- Who are the employees in the Marketing department and what are their  salaries?

select e.id,e.name,d.name,e.salary from employees as e inner join Departments as d on e.department_id=d.id where d.name="Marketing";


-- Who are the employees with salaries above the average salary of the  company, and which department are they in? 

select e.name,d.name,e.salary from employees as e inner join departments as d on d.id=e.department_id where salary>(select avg(salary) from employees);

-- 3. Who are the employees with the lowest salary in the Test department? --
SELECT 
    e.name AS employee_name,
    e.salary,
    d.name AS department_name
FROM 
    Employees AS e
INNER JOIN 
    Departments AS d ON e.department_id = d.id
WHERE 
    d.name = 'Development'
    AND e.salary = (
        SELECT MIN(e2.salary)
        FROM Employees AS e2
        INNER JOIN Departments AS d2 ON e2.department_id = d2.id
        WHERE d2.name = 'Development'
    );
-- 4. What is the total salary expenditure of the company?

select sum(salary) as total_salary_expenditure from employees;

-- 5. What is the average salary of employees in the Development (Dev) department?

select avg(e.salary) as avg_salary from employees as e inner join departments as d on d.id=e.department_id where d.name = "Development";

-- What is the total salary expenditure in the Development (Dev) and Support departments?

select sum(e.salary) from employees as e inner join departments as d on d.id=e.department_id where d.name="Development" or d.name="Support";

-- Who are the employees with a salary greater than the average salary of the Development (Dev) department?
select e.name,e.salary,d.name from employees as e inner join departments d on e.department_id=d.id where e.salary > (select avg(e2.salary) from employees as e2 inner join departments as d2 on e2.department_id=d2.id  where d2.name="Development");


-- 8. What is the total salary expenditure in Pune location? 

select sum(e.salary) from employees as e inner join locations as l on e.location_id = l.id where l.city="Pune";


-- Who are the employees hired in the year 2023 and what department are they in?

select * from employees as e where e.hire_date like "2023%";

-- 10. How many employees are there in Pune location? --
select e.name,l.city from employees as e inner join locations as l on l.id = e.location_id where l.city="pune";