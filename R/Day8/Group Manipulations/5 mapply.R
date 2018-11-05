#mapply

f<-list(A=matrix(1:9,3),B=1.4,C=matrix(1:10,2),D=21)
s<-list(A=matrix(1:9,1),B=1.4,C=matrix(1:10,2),D=21)
mapply(identical,f,s)


identical(2,1)


rep(1,4)


mapply(rep, 1:4, 4:1)

1:20
seq(1,20,0.5)


