use 01_collage;
CREATE TABLE TENP1(
ID INT,
NAME VARCHAR(50),
AGE INT,
CITY VARCHAR(50),
PRIMARY KEY(ID,NAME)
);
CREATE TABLE IF NOT EXISTS EMP(
ID INT,
SALARY INT DEFAULT 10000
);
INSERT INTO EMP(ID) VALUE (101);
SELECT * FROM EMP;