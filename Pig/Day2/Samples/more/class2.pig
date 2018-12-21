s = LOAD '/data/movies.txt' USING PigStorage(',');
dump s;

/*s = LOAD '/data/students.txt' USING PigStorage(',') as (id: int,fname:chararray,lname:chararray,age:int,phone:chararray,city:chararray);
dump s;
g = GROUP s by city;
dump g;
c = FOREACH g GENERATE group,COUNT(s.city);
d = FOREACH c GENREATE flatten($0)
dump d;*/
