student = load '/samples/students.txt' 
   USING PigStorage(',');
Dump student;

Describe student;

