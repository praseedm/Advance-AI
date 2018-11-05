# Question 1
a <- sample(1:6,3000,replace = T)
b <- sample(30:70,27)
faircoin <- sample(c('H','T'),1000,replace = T)

# Question 2
#mean =0 sd =30 n =100
rv <- rnorm(100,0,30)
prob <- dnorm(rv,0,30)
plot(rv,prob)

cdf <- pnorm(rv,0,30)
plot(rv,cdf)

qnorm(0.2,0,30)
qnorm(0.5,0,30)

# Question 3
#sd 15
prob15 <- dnorm(rv,0,15)
plot(rv,prob15)

#sd 45
prob45 <- dnorm(rv,0,45)
plot(rv,prob45)

#mean 50
prob50 <- dnorm(rv,50,30)
plot(rv,prob50)

#mean -50
prob_50 <- dnorm(rv,-50,30)
plot(rv,prob_50)

# Question 4
rvs <- rnorm(5000,20,5)
hist(rvs)

# Question 5
###>29
1-pnorm(29,22,5)
###<17
pnorm(17,22,5)
###<5+>25
pnorm(5,22,5) + (1-pnorm(25,22,5))

# Question 6
sigma <- 2
mu <- 30
1/(sqrt(2*pi)*sigma)*exp(-((31 - mu)^2/(2*sigma^2)))

dnorm(31,30,2)