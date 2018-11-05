 dpois(5, lambda=3)
 dpois(5, lambda=1.5)


?ppois


#generate 10,000 random counts from 5 different Poisson distributions
pois1<-rpois(n=2608,lambda=10097/2608)
pois1
hist(pois1)
pois1<-rpois(n=10000,lambda=1)
pois1
pois2<-rpois(n=10000,lambda=2)
pois2
pois5<-rpois(n=10000,lambda=5)
pois5
pois10<-rpois(n=10000,lambda=10)
pois10
pois20<-rpois(n=10000,lambda=20)
pois20
pois <- data.frame(Lambda.1=pois1,Lambda.2=pois2,Lambda.5=pois5,Lambda.10=pois10,Lambda.20=pois20)
tail(pois)
require(reshape2)
pois=melt(data=pois,variable.name="Lambda",value.name="x")

plot(pois)
hist(pois5)
barplot(pois)
boxplot(pois)
dev.off()


