student_details = LOAD '/students.txt' USING PigStorage(',')
   as (id:int, firstname:chararray, lastname:chararray, age:int, phone:chararray, city:chararray);

Dump student_details;
filter_data = FILTER student_details BY city == 'Chennai';
Dump filter_data;

STORE filter_data INTO ' /s4/' USING PigStorage (',');
