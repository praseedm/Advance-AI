plot.new()

# Question 1

x <- c('Comedy', 'Action', 'Romance', 'Science Fiction')
data <- sample(x,20,replace = T)
s <- c(10,15,14,22)
color <- rainbow(4)
pie(s,s,col=color,main="Fav Movie Types",clockwise =T)
legend("topright",x,fill=color,cex=0.6)

# Question 2

barplot(s,xlab = "categories",ylab = "Counts" ,names.arg=x,main="Fav Movie Types",col="violet",border = "red")

# Question 3
A <- sample(10:30,4)
B <- sample(10:30,4)
C <- sample(10:30,4)
Data <- matrix(c(A,B,C),nrow = 3,byrow = T)
color = rainbow(3)
names=c("1st Q","2nd Q","3rd Q","4th Q")
barplot(Data,names.arg = names,col=color)
legend("topright",c("A","B","C"),fill=color,cex=0.6)

# Question 4
hist(mtcars$mpg)

# Question 5
plot.new()
plot.window(xlim=c(0,10),ylim=c(0,10))
axis(1)
axis(2)
abline(h=0)
abline(v=0)
data=sample(1:8,5)
points(data)
plot(data,type="b",col="red")
abline(h=max(data),col="green")
abline(v=length(data),col="green")

# Question 6
drugA <- c(16, 20, 27, 40, 60)
drugB <- c(15, 18, 25, 31, 40)

plot.new()
plot.window(xlim=c(0,50),ylim=c(0,70))
axis(1)
axis(2)
plot(drugA,type="b",col="blue")
lines(drugB,type="b",col="red")

# Questtion 7
?airquality
boxplot(Temp~Month,data=airquality)

# Question 8
plot.new()
plot.window(xlim=c(0,150),ylim=c(0,8))
plot(iris$Sepal.Length,iris$Sepal.Width,col="red")

# Question 9
pairs(~Sepal.Length+Sepal.Width+Petal.Length+Petal.Width,data=iris,main="Scatter Plot",col="blue")
