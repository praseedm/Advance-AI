A = LOAD '/data/vimala/A.txt' USING PigStorage(',')  as  (a1:int,a2:chararray);
B = LOAD '/data/vimala/B.txt' USING PigStorage(',')  as  (b1:int,b2:chararray);

C = CROSS A,B;
dump C;
