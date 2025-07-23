Create database company;
use company;
-- 1. Create table TEACHER with ID, NAME, CITY, SALARY, AGE, COUNTRY--
CREATE TABLE TEACHER (
    ID INT,
    NAME VARCHAR(100),
    CITY VARCHAR(100),
    SALARY DECIMAL(10, 2),
    AGE INT,
    COUNTRY VARCHAR(100)
);


-- 3. Insert 10 records in each table --
INSERT INTO TEACHER (ID, NAME, CITY, SALARY, AGE, COUNTRY) VALUES
(1, 'Anil Sharma', 'Delhi', 55000.00, 45, 'India'),
(2, 'Meena Kumari', 'Mumbai', 60000.00, 38, 'India'),
(3, 'Rajesh Patel', 'Ahmedabad', 48000.00, 40, 'India'),
(4, 'Sunita Rao', 'Bangalore', 62000.00, 35, 'USA'),
(5, 'Vikram Joshi', 'Pune', 51000.00, 42, 'Canada'),
(6, 'Neha Verma', 'Chennai', 58000.00, 33, 'India'),
(7, 'Amitabh Reddy', 'Hyderabad', 63000.00, 39, 'UK'),
(8, 'Kiran Desai', 'Surat', 47000.00, 41, 'Australia'),
(9, 'Swati Mishra', 'Lucknow', 52000.00, 36, 'India'),
(10, 'Manish Dubey', 'Bhopal', 50000.00, 44, 'Germany');

select * from TEACHER;

--  SELECT THE MAXIMUM SALARY OF TEACHER.--
select max(salary) as Max_salary from teacher;

-- SELECT THE TEACHERS FROM COUNTRY 'INDIA'--
select * from teacher where country="india";

-- 6.SELECT THE MINIMUM SALARY OF TEACHER --
select min(salary) as min_salary from teacher;

-- 7. SELECT THE AVG SALARY OF ALL THE TEACHERS --
select avg(salary) as avg_salary from teacher;

-- 8. UPDATE ANY NAME OF TEACHER TO 'SUMAN' --
SET SQL_SAFE_UPDATES = 0;
update  teacher set name='Sumen' where name ="Anil Sharma";
select * from teacher;

-- 9.SELECT THE TEACHER WHOSE CITY IS 'surat’ --
select * from teacher where city="surat";

-- 16.SHOW ALL THE TEACHERS WHOSE SALARY IS GREATER THAN 45K --
SELECT * FROM TEACHER WHERE SALARY > 45000;

-- 17.SHOW ALL THE TEACHERS WHOSE SALARY IS LESS THAN EQUALS TO 30K --
SELECT * FROM TEACHER WHERE SALARY <=30000;

-- 18.SHOW ALL THE TEACHERS WHOSE COUNTRY NAME IS NULL --

SELECT * FROM TEACHER WHERE COUNTRY is null;



-- 2.Also create table CAR with ID, NAME, COLOR, PRICE, LAUNCH DATE, COUNTRY --
CREATE TABLE CAR (
    ID INT ,
    NAME VARCHAR(100),
    COLOR VARCHAR(50),
    PRICE DECIMAL(10, 2),
    LAUNCH_DATE DATE,
    COUNTRY VARCHAR(100)
);
-- 3. Insert 10 records in each table --
INSERT INTO CAR (ID, NAME, COLOR, PRICE, LAUNCH_DATE, COUNTRY) VALUES
(1, 'Toyota Corolla', 'White', 22000.00, '2022-03-15', 'Japan'),
(2, 'Ford Mustang', 'Red', 45000.00, '2021-11-20', 'USA'),
(3, 'Hyundai i20', 'Blue', 15000.00, '2023-05-10', 'South Korea'),
(4, 'Volkswagen Golf', 'Black', 27000.00, '2020-09-01', 'Germany'),
(5, 'Honda Civic', 'Silver', 23000.00, '2022-07-05', 'Japan'),
(6, 'Tesla Model 3', 'White', 40000.00, '2024-01-10', 'USA'),
(7, 'Renault Clio', 'Grey', 18000.00, '2021-04-18', 'France'),
(8, 'Kia Seltos', 'Orange', 21000.00, '2023-02-28', 'South Korea'),
(9, 'Skoda Octavia', 'Green', 26000.00, '2022-10-12', 'Czech Republic'),
(10, 'Mahindra XUV700', 'Black', 25000.00, '2023-08-22', 'India');

select * from car;

-- 10.SELECT THE MINIMUM PRICE OF THE CAR --
select min(price) from car;

-- 11.FIND OUT THE TOTAL OF ALL THE PRICES OF CAR --
select sum(price) from car;

-- 12. FIND OUT THE AVERAGE OF ALL THE PRICES OF CAR --
select avg(price) from car;

-- 13.UPDATE THE LAUNCH DATE OF CAR WHOSE ID IS 105 TO TODAYS DATE --

update car set launch_date= curdate() where launch_date="2020-09-01";
select * FROM CAR;

-- 14.LIST ALL THE CARS WHICH ARE HAVING PRICE GREATER THAN 25000--
SELECT * FROM CAR WHERE PRICE >= 25000;

 -- 15.DISPLAY THE COUNT OF ALL THE CARS IN THE TABLE -- 
 SELECT COUNT(COLOR) FROM CAR;


