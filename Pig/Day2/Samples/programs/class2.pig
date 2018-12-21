s = LOAD '/data/students.txt' USING PigStorage(',') as (id: int,fname:chararray,lname:chararray,age:int,phone:chararray,city:chararray);



k = FOREACH s  GENERATE   id +age ;
dump k; 