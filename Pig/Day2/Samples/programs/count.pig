file = load '/data/dm.txt' as (line:chararray);
words = FOREACH file  GENERATE   FLATTEN(TOKENIZE(line)) as word;
w = GROUP words by word;
c = FOREACH w GENERATE  group,COUNT(words) as  cnt;
c1 = ORDER c by cnt desc;
l = LIMIT c1 10;
dump l;
