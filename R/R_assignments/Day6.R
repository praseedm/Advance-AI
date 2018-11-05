# Question 1
plot.new()
ages <- c(2,3,5,7,8)
weights <- c(14,20,32,42,44)
plot(ages,weights) 
relation <- lm(weights~ages)
abline(relation)
ageval <- data.frame(ages=6)
predict(relation,ageval)

# Question 2
Customers <- c(8,7,6,4,2,1)
Distances <- c(15,19,25,23,34,40)
plot(Distances,Customers)
relation <- lm(Customers ~ Distances)
disval <- data.frame(Distances=2)
predict(relation,disval)
predict(lm(Distances ~ Customers), data.frame(Customers=5))
rel2 = lm(Distances ~ Customers)

# Question 3

Maths<-c(6,4,8,5,3.5)
Chemistry <- c(6.5,4.5,7,5,4)
plot(Maths,Chemistry)
rel<-lm(Chemistry~Maths)
abline(rel)
predict(rel,data.frame(Maths=7.5))

# Question 4
Height <- c(186,189,190,192,193,193,198,201,203,205)
Weight <- c(85,85,86,90,87,91,93,103,100,101)
plot(Height,Weight)
re <- lm(Weight~Height)

abline(re)
cor(Weight,Height)
predict(re,data.frame(Height=208))
abline(v=208)

# Question 5
Hours <- c(80,79,83,84,78,60,82,85,79,84,80,62)
Prod <- c(300,302,315,330,300,250,300,340,315,330,310,240)
cor(Hours,Prod)

# Question 6
Shours <- c(6,7,8,9,10)
Thours <- c(4,3,3,2,1)
cor(Shours,Thours)
r <- lm(Thours~Shours)
predict(r,data.frame(Shours=8))

# Question 7
scores <- c(25,42,33,54,29,36)
sales <- c(42,72,50,90,45,48)
cor(scores,sales)
r1 <- lm(sales~scores)
predict(r1,data.frame(scores=47))