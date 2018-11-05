result <- array((1:18),dim = c(3,3,2))
a <- (1:4)
b <- letters[1:4]
d <- LETTERS[1:4]
df <- data.frame(a,b,d)
df[1,]
a <- c("1","2","3")
row.names(df) <- c("one","two","three","four")
row.names(df)=c(1,2,3,4)
head(df)

# Question 1
Age <- c(25,31,23)
Height <- c(177,163,190)
Weight <- c(57,69,83)
Sex <- c("F","F","M")
res <- data.frame(Age,Height,Weight,Sex)
row.names(res) <- c("Alex","Lilly","Mark")

# Question 2
Working <- c("Yes","No","No")
frame <- data.frame(Working)
row.names(frame) <- c("Alex","Lilly","Mark")

  ## 
?rbind
cbind(res,frame)
mean(res$Height)
bmi <- res$Weight/((res$Height/100)^2)
Healthy <- bmi > 25
cbind(res,Healthy)

# Read Input
getwd()
r1 <- read.table(file.choose())
r2 <- read.csv(file.choose())

# Array
r <- paste("row",1:2)
c <- paste("col",1:3)
m <- paste("mat",1:3)
arr <- array((1:20),c(2,3,3),list(r,c,m))

# Built in DF
dfn <- data.frame(mtcars$mpg,mtcars$cyl,mtcars$hp)
dfn2 <- data.frame(mtcars[1:5],mtcars[-5:0])

# Functions
add = function(a=1,b=1){
  print(a)
  print(a+b)
}
add(b=2,a=3)