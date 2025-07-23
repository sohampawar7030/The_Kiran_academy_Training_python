create database companyHome;
use companyHome;

CREATE TABLE SUPPLIER (
    SID INT PRIMARY KEY,
    SNAME VARCHAR(50) NOT NULL,
    AGE INT ,
    QTY INT ,
    PRICE DECIMAL(10, 2),
    CITY VARCHAR(50),
    STATE VARCHAR(50)
);
INSERT INTO SUPPLIER (SID, SNAME, AGE, QTY, PRICE, CITY, STATE) VALUES
(1, 'Amit Traders', 35, 100, 5000.00, 'Pune', 'Maharashtra'),
(2, 'Sharma Supply Co', 40, 200, 7000.00, 'Delhi', 'Delhi'),
(3, 'Goenka Corp', 45, 150, 6500.00, 'Mumbai', 'Maharashtra'),
(4, 'Nexus Suppliers', 38, 80, 4000.00, 'Chennai', 'Tamil Nadu'),
(5, 'Fast Track Supply', 30, 300, 9000.00, 'Hyderabad', 'Telangana'),
(6, 'Reliable Suppliers', 50, 120, 5500.00, 'Nagpur', 'Maharashtra'),
(7, 'Om Distributors', 28, 70, 3500.00, 'Ahmedabad', 'Gujarat'),
(8, 'Bright Traders', 36, 90, 4800.00, 'Kolkata', 'West Bengal'),
(9, 'Southway Corp', 33, 60, 3000.00, 'Bangalore', 'Karnataka'),
(10, 'Elite Supply', 42, 110, 5200.00, 'Jaipur', 'Rajasthan');

CREATE TABLE PRODUCT (
    PID INT PRIMARY KEY,
    PNAME VARCHAR(50) NOT NULL,
    DATE_OF_MANUFACTURE DATE,
    PRICE DECIMAL(10, 2) CHECK (PRICE > 0),
    SID INT,
    FOREIGN KEY (SID) REFERENCES SUPPLIER(SID)
);

INSERT INTO PRODUCT (PID, PNAME, DATE_OF_MANUFACTURE, PRICE, SID) VALUES
(101, 'Laptop', '2024-12-15', 45000.00, 1),
(102, 'Keyboard', '2025-01-10', 1200.00, 2),
(103, 'Mouse', '2025-02-20', 800.00, 3),
(104, 'Monitor', '2025-03-05', 9500.00, 4),
(105, 'Printer', '2025-04-01', 15000.00, 5),
(106, 'Scanner', '2025-04-12', 8200.00, 6),
(107, 'Webcam', '2025-05-20', 2500.00, 7),
(108, 'Router', '2025-06-01', 3500.00, 8),
(109, 'Hard Drive', '2025-06-15', 4200.00, 9),
(110, 'RAM', '2025-07-01', 3200.00, 10);


select * from supplier;
select * from product;

-- Find out the product With Maximum Price
select s.SName,p.pname,p.price from supplier as s inner join product as p on
s.SID=p.SID order by price desc limit 1;

-- Find out the avg of all the Product Price 
select avg(p.price) as Avg_price from supplier as s  inner join product as p on
s.SID = p.SID; 
-- Find out the avg of all the Product Price with products --
SELECT 
    PName,
    Price,
    (SELECT AVG(Price) FROM PRODUCT) AS Avg_Product_Price
FROM PRODUCT; 

-- FIND OUT THE MIN ORDER SUPPLIED BY THE SUPPLIER --

select p.pname,s.sname,s.Qty,s.price from supplier as s inner join product as p on 
s.SID=p.SID order by qty asc limit 1;

-- 6.FIND OUT THE SUPPLIER WHO DOESNT BELONG TO MAHARASHTRA --

select s.sname,s.state from supplier as s where s.state <> "Maharashtra"; 

-- 7.FIND OUT THE PRODUCT WHOSE PRICE IS LESS THAN 1500 --

select p.pname,p.price as product_price,s.price as supplier_price from supplier as s inner join product as p on 
s.SID=p.SID where p.price < 1500;

-- COUNT THE TOTAL PRODUCTS IN PRODUCT TABLE-- 
select count(*) as Total_product from product ;

-- 9.PRINT ALL THE RECORDS OF THE PRODUCT TABLE BUT PRICE SHOULD BE 10 TIMES OF THE ORIGINAL PRICE

select * from Supplier;
select * from product;
select pid , pname,Date_of_manufacture,price,price*10 as inceresed_price ,sid from product ;


-- 10.LIST THE SUPPLIERS WHOSE AGE IS NOT 22,28 AND 30

select * from supplier where age not in (22,28,30);

-- 11.LIST THE SUPPLIERS WHO BELONG TO STATE MAHARASHTRA, GUJARAT AND DELHI --
select * from supplier where state in ('MAHARASHTRA', 'GUJARAT','DELHI');

-- 12.LIST ALL THE SUPPLIERS WHOSE NAME HAVE 'A' TWICE IN IT
select * from supplier where lower(sname) like "%a%a%";

-- LIST ALL THE PRODUCTS WHOSE NAME START WITH A TO M ALPHABET --
select * from product where pname >= 'a' and pname <='n';

-- 14.COPY THE TABLE SUPPLIER TO NEW TABLE CUSTOMER 
CREATE TABLE CUSTOMER AS 
SELECT * FROM SUPPLIER;

select * from CUSTOMER;

-- 15.FIND OUT THE SUPPLY WHOSE QUANTITY IS LESS THAN 20 --
SELECT P.PNAME,S.QTY FROM SUPPLIER AS S INNER JOIN PRODUCT AS P ON 
S.SID=P.SID WHERE QTY < 20;

-- 16.LIST ALL THE PID,PNAME,SID AND SNAME IN SINGLE TABLE --
 SELECT P.PID,P.PNAME,S.SID,S.SNAME FROM SUPPLIER AS S INNER JOIN PRODUCT AS P ON 
S.SID=P.SID ;

-- 17. FIND OUT THE NAME OF THE PRODUCT WITH HIGHEST PRICE
SELECT P.PNAME,S.PRICE AS SUPPLIER_PRICE ,P.PRICE AS ACTUAL_PRICE FROM SUPPLIER AS S INNER JOIN PRODUCT AS P ON 
S.SID=P.SID ORDER BY P.PRICE DESC LIMIT 1; 

-- 18.FIND OUT THE PRODUCT WITH THE LOWEST PRICE IN THE PRODUCT TABLE
SELECT P.PNAME,S.PRICE AS SUPPLIER_PRICE ,P.PRICE AS ACTUAL_PRICE FROM SUPPLIER AS S INNER JOIN PRODUCT AS P ON 
S.SID=P.SID ORDER BY P.PRICE ASC LIMIT 1; 

-- 19. FIND OUT THE LIST OF TOP 5 HIGHEST PRICE PRODUCT.
SELECT P.PNAME,S.PRICE AS SUPPLIER_PRICE ,P.PRICE AS ACTUAL_PRICE FROM SUPPLIER AS S INNER JOIN PRODUCT AS P ON 
S.SID=P.SID ORDER BY P.PRICE DESC LIMIT 5;
 
 -- 20.FIND OUT THE LIST OF 5 PRODUCT STARTING FROM LOWEST PRICE FIRST FROM THE TABLE.
 SELECT P.PNAME,S.PRICE AS SUPPLIER_PRICE ,P.PRICE AS ACTUAL_PRICE FROM SUPPLIER AS S INNER JOIN PRODUCT AS P ON 
S.SID=P.SID ORDER BY P.PRICE ASC LIMIT 5;

-- 21. Find out how many suppliers are from each city.
SELECT CITY,COUNT(CITY) FROM SUPPLIER GROUP BY CITY;

