A = LOAD '/data/vimala/uclicks.txt' USING PigStorage(',')  as  (uid:chararray,clicks:int);

B = group A all;

C = foreach B generate SUM(A.clicks) as total;

D = foreach C generate (float)total;

describe D;
