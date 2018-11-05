# Question 1
R <- read.csv(file.choose())
head(R)
class(R)
studentwise_total <- apply(R,1,sum)
studentwise_total - R$Roll.No
subjectwise_total <- apply(R,2,sum)

cbind(R,studentwise_total)
rbind(R,subjectwise_total)
sum(R$Roll.No)

# Question 2
list1 <- list(observationA = c(1:5, 7:3),
              observationB=matrix(1:6,nrow=2))
lapply(list1, length)
lapply(list1, sum)
lapply(list1, class)

##d
f1 <- function(x) { log10(x) + 1 }
lapply(list1, f1)
lapply(list1, unique)
lapply(list1, range)

# Question 3
x<-list(A=matrix(1:9,3),B=1.4,C=matrix(1:10,2),D=21)
lapply(list1, mean)
sapply(list1, mean)
