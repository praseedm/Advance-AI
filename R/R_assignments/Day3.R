# Question 1
student <- list(sname="Ali",roll_no=2,gender="male",marks=c(1,2,3,4,5))


class(student)
mean(student$marks)

rm_list <- list(student$roll_no,student$marks)
student$marks[5]=100
subjects=c("1SB","2SB","3SB","4SB","5SB")

student[[5]]=subjects

# Question 2
mat <- matrix(2:5,nrow=2)
2*mat

# Question 3
mat3 <- matrix(1,nrow=3,ncol=3)
mat3[1,]=c(1,1,3)
mat3[2,]=c(5,2,6)
mat3[3,]=c(-2,-1,-3)

mat3%*%mat3%*%mat3

# Question 4
matb <- matrix(10,nrow=3,ncol=3)
matb[,2] <- rep(-10,3) 
t(matb)%*%matb

# Question 5
mat <- matrix(1:15,nrow=3)
r_names <- paste('p',1:5)
c_names <- c("Alice","Bill","Sara")

dimnames(mat) <- list(c_names,r_names)

mean(mat[,1])
mean(mat[,2])
mean(mat[,3])
mean(mat[,4])
mean(mat[,5])

# Question 6
categories <- c(rep('one',3),rep("next",7),"wee",rep("bee",4))
cat_factor <- factor(categories)
summary(cat_factor)
cat_factor[2]
