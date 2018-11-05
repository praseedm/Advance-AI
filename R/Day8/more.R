
runif(20,10,100)

poisson_distrib <- rpois(2608, 10097/2608)
hist(poisson_distrib)

 
binom_distrib <- rbinom(20, 6, 28/52)
binom_distrib
hist_breaks<-c(0.5,1.5,2.5,3.5,4.5,5.5,6.5)
hist(binom_distrib, breaks=hist_breaks, xlim=c(0,6))

factorial(4)
choose(6, 3)
?runif

p <- 28/52
choose(6,3)*(p^3)*((1-p)^(6-3))

dbinom(3, 6, 28/52)

