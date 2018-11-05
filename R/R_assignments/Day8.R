# Question 1
##a
dbinom(5,50,.8)
##b
dbinom(5,50,0.05)
##c atmost 5
pbinom(5,50,.8)
##d atleast 25
1-pbinom(25,50,.8)
##e atmost 5
pbinom(5,50,0.05)

# Question 2
##1
dbinom(40,60,.65)
##2 atleast 40
1-pbinom(40,60,.65)

# Question 3
##a p(S)=0.15
rv <- seq(0,30,1)
probs <- dbinom(rv,30,0.15)
plot(rv,probs)
#b p(s)=0.4
probs <- dbinom(rv,30,0.4)
plot(rv,probs)
#c p(s)=0.8
probs <- dbinom(rv,30,0.8)
plot(rv,probs)

# Question 4
ps=0.5
#a 20,25or30
dbinom(20,60,ps)+dbinom(25,60,ps)+dbinom(30,60,ps)
#b <20
pbinom(20,60,ps)
#c between 20 and 30
pbinom(30,60,ps)-pbinom(20,60,ps)

# Question 5
size=100
m1=0.15
rv <- rpois(size,m1)
hist(rv)
probs1 <- dpois(rv,m1)
plot(rv,probs1)
m2=0.4
rv <- rpois(size,m2)
hist(rv)
probs2 <- dpois(rv,m2)
plot(rv,probs2)
m3=0.8
rv <- rpois(size,m3)
hist(rv)
probs3 <- dpois(rv,m3)
plot(rv,probs3)

# Question 6
size = 2608
rvs <- rpois(size,(10097/2608))
hist(rvs)

# Question 7
mean=7
#a <5
ppois(5,7)
#b > 10
1-ppois(10,7) 
#c between 4 and 16
ppois(16,7)-ppois(4,7)

# Question 8
?punif()
punif(6,0,25)
6/25
