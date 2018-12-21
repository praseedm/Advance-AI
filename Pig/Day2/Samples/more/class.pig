s = LOAD '/data/vimala/dd.txt' USING PigStorage('\t')  as  (f1:chararray,f2:chararray);
k = FOREACH s generate f1,STRSPLIT(f2,',');
dump k;
