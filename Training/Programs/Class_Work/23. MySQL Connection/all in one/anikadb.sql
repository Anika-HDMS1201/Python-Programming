create database anikaDB;
use anikaDB;
use bank; //its my DB {use // for single line comment}

create table anikaDB.friends(
				name varchar(30), 
				phone_number bigint(10),
				address varchar(100)
			);

CREATE TABLE `anikadb`.`phone_diary` (
  `id` INT NOT NULL,
  `Person Name` VARCHAR(45) NULL,
  `Person Number` BIGINT(11) NULL,
  PRIMARY KEY (`id`));
  


insert into anikadb.friends values('chittajit chakraborty', 7059663127, '24/2/12 PK road');

INSERT INTO friends(name, phone_number, address) VALUES ('chittajit chakraborty', 7059663127, '24/2/12 PK road');


insert into anikadb.friends values('Anika Jana', 9477514446, 'Howrah Shibpur');
select * from anikadb.friends;
select * from anikadb.friends where name = 'Chittajit Chakraborty';
DELETE FROM anikadb.friends WHERE phone_number = 7059663127;
DELETE FROM anikadb.friends WHERE name = 'Anika Jana';

show databases;
use chittajit;
show tables;
select * from customers2;