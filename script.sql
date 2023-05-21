
CREATE DATABASE sheltor;

CREATE TABLE animal(
animal_id INT NOT NULL AUTO_INCREMENT,
name VARCHAR(255),
animal_type VARCHAR(255),
sex VARCHAR(255),
weight FLOAT,
PRIMARY KEY (animal_id)
);

ALTER TABLE animal ADD age INT;

INSERT INTO animal (animal_id,name,animal_type,sex,weight,age) VALUES (1,'Malta', 'Lion', 'she', 5,6);
INSERT INTO animal (animal_id,name,animal_type,sex,weight,age) VALUES (2,'Alisa', 'Cat', 'she', 5,3);
INSERT INTO animal (animal_id,name,animal_type,sex,weight,age) VALUES (3,'Oskar', 'Dog', 'he', 3,11);
INSERT INTO animal (animal_id,name,animal_type,sex,weight,age) VALUES (4,'Simba', 'Tiger', 'he', 4,6);


SELECT count(*)
FROM animal
animalanimal

SELECT count(*)
FROM animal
WHERE animal_type LIKE 'Dog';

SELECT avg(weight) FROM animal GROUP BY animal_type='Dog';

SELECT animal_type FROM animal;

INSERT INTO animal (animal_id,name,animal_type,sex,weight,age) VALUES (5,'Барсик', 'Dog', 'he', 4,5);
INSERT INTO animal (animal_id,name,animal_type,sex,weight,age) VALUES (6,'Арчик', 'Dog', 'he', 6,12);

SELECT animal_type FROM animal;

INSERT INTO animal (animal_id,name,animal_type,sex,weight,age) VALUES (7,'Вилли', 'Dog', 'he', 4,5);
INSERT INTO animal (animal_id,name,animal_type,sex,weight,age) VALUES (8,'Вилли', 'Dog', 'he', 6,3);

SELECT * FROM animal WHERE name='Вилли';

SELECT sex, count(*)
FROM animal
GROUP BY sex;

INSERT INTO animal (animal_id,name,animal_type,sex,weight,age) VALUES (9,'Sharlotka', 'Cat', 'she', 5,4);
INSERT INTO animal (animal_id,name,animal_type,sex,weight,age) VALUES (10,'Ita', 'Cat', 'she', 4,6);

SELECT DISTINCT age FROM animal;

SELECT DISTINCT name FROM animal;

SELECT * FROM animal WHERE name LIKE '%ик';

UPDATE animal
SET name='Монти'
WHERE name='Барсик';

SELECT * FROM animal



