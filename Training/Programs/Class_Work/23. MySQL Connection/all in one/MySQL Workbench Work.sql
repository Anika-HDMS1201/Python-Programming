create database anikaDB;

CREATE TABLE anikaDB.friends (
    name VARCHAR(30),
    phone_number BIGINT(10),
    address VARCHAR(100)
);
            
insert into anikaDB.friends values ('Sayan Chakraborty', 4435547, 'Goria kolkata');
select * from anikaDB.friends; #fetching all data from database without using filtering
select * from anikadb.friends where name = 'Chittajit Chakraborty'; #filtering
select * from anikadb.friends where phone_number = 4435547; #filtering
select * from anikadb.friends order by name; #Sorting name alphabatically ascheding
select * from anikadb.friends order by name desc; #Sorting name alphabatically descending 