s = LOAD '/data/students.txt' USING PigStorage(',') as (id:int, firstname:chararray, lastname:chararray, age:chararray, phone:chararray, city:chararray );
k1 = FOREACH s generate  (id,firstname), STARTSWITH (firstname, 's') as f1;
k2 = FILTER k1 by f1==true;
dump k2;


