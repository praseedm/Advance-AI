student_data = LOAD '/samples/students.txt' USING PigStorage(',') as (id:int, firstname:chararray, lastname:chararray, age:chararray, phone:chararray, city:chararray );
dump student_data;
describe student_data;

