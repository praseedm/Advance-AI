/*s = LOAD '/data/students.txt' USING PigStorage(',') as (id: int,fname:chararray,lname:chararray,age:int,phone:chararray,city:chararray);
k1 = FOREACH s generate (id,fname), SUBSTRING(city, 0,2) as c;
k2 = FOREACH s generate (id,fname), UCFIRST(fname) as n;

dump k2;


s = LOAD '/data/customers2.txt' as (line:chararray);
k = DISTINCT s;
dump k;

*/
