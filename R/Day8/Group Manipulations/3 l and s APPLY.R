#lapply

x <- list(a = 1:10, b = 10:20, c=100:120)
lapply(x, mean)



thelist<-list(A=matrix(1:9,3),B=1:4,C=matrix(1:9,2),D=21)
lapply(thelist,mean)

seq(20)
i39 <- lapply(3:9, seq) 

 



x <- list(a = 1:10, beta = exp(-3:3), logic = c(TRUE,FALSE,FALSE,TRUE))
lapply(x,mean)


 

x <- list(a = 1:10, beta = exp(-3:3), logic = c(TRUE,FALSE,FALSE,TRUE), data=c("a","b","c"))
lapply(x,mean)
#sapply

thelist<-list(A=matrix(1:9,3),B=1.4,C=matrix(1:10,2),D=21)
s=sapply(thelist,sum)






