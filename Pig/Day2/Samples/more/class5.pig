C1 = LOAD '/data/vimala/C1.txt' USING PigStorage(',')  as  (a1:int,a2:int,a3:int);
C2 = LOAD '/data/vimala/C2.txt' USING PigStorage(',')  as  (b1:int,b2:int);

C = COGROUP C1 by a1 inner, C2 by b1 inner;
dump C;


