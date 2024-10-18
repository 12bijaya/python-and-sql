CREATE DATABASE IF NOT EXISTS 01_CLASSROOM;
USE 01_CLASSROOM;
DROP DATABASE IF EXISTS BIJAYA;
USE 01_COLLAGE;
CREATE TABLE STUDENT(
	id INT PRIMARY KEY,
    name VARCHAR(50),
	age INT NOT NULL
);

INSERT INTO STUDENT VALUES (1,"ROJINA",16);
INSERT INTO STUDENT
	VALUES
    (2,"BIKASH",19),
    (3,"ANJANA",12)
    ;

SELECT * FROM STUDENT;

SHOW DATABASES;

SHOW TABLES;

use 01_classroom;
drop table student;
create table student(
roll_no  INT PRIMARY KEY,
name VARCHAR(50),
marks INT NOT NULL,
grade VARCHAR(34),
city VARCHAR(50)
);
INSERT INTO student
(roll_no, name, marks, grade, city)
 VALUES
 (101,"ANJANA",85,"A","LAINCHOUR"),
 (102,"SHAIJU",95,"A+","BHAKTAPUR"),
 (103,"BIKASH",99,"A+","MANAMAIJU"),
 (104,"BIJAYA",100,"A+","TOKHA"),
 (105,"JHARNA",0,"E","TOILET"),
 (106,"SUPRINA",100,"A+","CHANDRAGIRI"),
 (107,"KALIN","99","A+","INDRENI POOL");
 select name,marks from student;
 select * from student;
select distinct grade from student; 
select * from student where marks > 90; 
select * from student where city != "TOILET";