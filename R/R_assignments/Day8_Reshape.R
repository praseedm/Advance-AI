install.packages(reshape2)
require(reshape2)
#Question 1

table <-  data.frame(City=c("Sydney","Londan"),
                     Month = c("January","January"),
                     Min_Temp = c(19,15),
                     Max_Temp = c(26,5),
                     Max_Wind = c(10,6))

t1 <- melt(table,id=c("City","Month"))

t2 <- dcast(t1,formula = City+Month~variable)

# Question 2
rand <- sample(1:20,100,replace = T)
table(rand)

# Question 3
table(mtcars[c("mpg","gear")])