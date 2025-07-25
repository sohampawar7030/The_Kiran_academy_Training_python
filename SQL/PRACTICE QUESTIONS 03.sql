-- Practical Questions --
use company;
select * from teacher;
select * from car;

-- 1.SELECT ALL THE COUNTRY NAMES STARTING WITH ‘A’ AND ‘U’-- 
select COUNTRY from car 
where COUNTRY like 'A%' or COUNTRY like 'U%';

-- 2.SELECT ALL THE COUNTRY NAMES WHICH ARE NOT STARTING WITH U AND G
select COUNTRY from car 
where COUNTRY NOT like 'U%' AND COUNTRY NOT like 'G%';

-- 2.SELECT ALL THE COUNTRY NAMES WHICH ARE NOT STARTING WITH U AND G from Car table --
select country from car WHERE country NOT LIKE 'U%' AND country NOT LIKE 'G%';

-- UPDATE THE NAME OF THE TEACHER WHOSE ID IS 10 -- 
update teacher set name="soham Pawar" where ID=10;
SET SQL_SAFE_UPDATES = 0;
select * from teacher;

-- 4.UPDATE THE COUNTRY AND NAME OF THE TEACHER WHOSE ID IS 10 --
update teacher set country="India",name="Sohan pawar" where id=10;
select * from teacher;
 
 -- 5.FIND ALL THE TEACHER WHOSE AGE IS BETWEEN 25 TO 35 --
 SELECT * FROM TEACHER WHERE AGE BETWEEN 25 AND 35;
select MIN(AGE) FROM TEACHER;

-- 6.LIST ALL THE TEACHER WHO DOESNT BELONG TO THE AGE 25-40 --
SELECT NAME,AGE FROM TEACHER WHERE AGE NOT between 25 AND 40; 

-- 7.SELECT ALL THE NAME OF THE TEACHER WHO HAS 'R' ANY WHERE IN THE NAME--
SELECT NAME FROM TEACHER WHERE NAME LIKE '%R%';
SELECT * FROM TEACHER;
-- 8.SELECT ALL THE FIELDS WHERE COUNTRY NAME IS INDIA AND USA --
SELECT * FROM TEACHER WHERE COUNTRY="india" OR COUNTRY="USA";

-- 9.SELECT ALL THE RECORDS WHERE COUNTRY NAME IS NOT USA AND INDIA --
SELECT * FROM TEACHER WHERE COUNTRY not in('usa','india');

-- 10.SELECT ALL THE NAMES OF THE teacher WHICH ARE ENDING WITH 'A' --
SELECT * FROM TEACHER WHERE NAME LIKE '%A' OR NAME LIKE '%a' ;

-- 11.ARRANGE THE RECORDS IN CARS TABLE BASED ON THEIR NAMES IN ASCENDING ORDER.--
SELECT * FROM car ORDER BY name ASC;

-- 12.ARRANGE THE RECORDS IN CARS TABLE BASED ON THEIR NAMES IN DESC AND PRICE IN ASC ORDER --
SELECT * FROM car ORDER BY name DESC, price ASC;

-- 13.DELETE THE RECORD FROM THE TABLE WHERE CAR_ID IS 10 --

delete from car where id=10;
select * from car;
-- 14.DISPLAY ONLY THE NAME OF THE CARS WHERE COLOR IS NOT ADDED.--
select name from car where color IS null;

-- 15.SELECT TOP 2 MOST EXPENSIVE CARS.--
SELECT * 
FROM car 
ORDER BY price DESC 
LIMIT 2;

 

	
