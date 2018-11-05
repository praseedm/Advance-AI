# Question 1
y<-c(1:20,19:1)
y
x<-c(4,6,3)

# Question 2
a<-rep(x,10)
?rep
b<-rep(x,11,31)
b
n<-c(rep(4,10),rep(6,20),rep(3,30))

# Question 3
R <- c(2.27, 1.98, 1.69, 1.88, 1.64, 2.14)
H <- c(8.28, 8.04, 9.06, 8.70, 7.58, 8.34)
v <- 1/3*pi*R*R*H
rounded <- round(v,2)
min(rounded)
max(rounded)

# Question 4
A <- sample(0:999,250)
B <- A[which(A > 900)]
C <- sort(B)

# Question 5
height_cm <- c(180, 165, 160, 193)
weight_kg <- c(87, 58, 65, 100)
?power
BMI <- weight_kg / ((height_cm/100)^2)
BMI_G25 <- BMI[which(BMI > 25)]
mean(BMI)

# Question 6
marks <- sample(0:50,10)
p1 <- mean(marks)
p2 <- median(marks)

# Question 7
dry <- c(77, 93, 92, 68, 88, 75, 100)
sum(dry)
length(dry)
mean(dry)
sum(dry)/length(dry) ## Equation for mean
median(dry)
sd(dry)
var(dry) ##Variance
sd(dry)^2
min(dry)
max(dry)
summary(dry)

# Question 8
?sample
random <- sample(1:20,10,TRUE)
random[which(random %% 2 == 0)]