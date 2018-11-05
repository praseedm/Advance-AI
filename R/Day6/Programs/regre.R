dev.off()

x <- c(63, 81, 56, 91, 47, 57, 76, 72, 62, 48)
y <- c(151, 174, 138, 186, 128, 136, 179, 163, 152, 131)


cor(x,y)

# Apply the lm() function.
relation <- lm(y~x)

?lm

plot(y,x)

print(relation)

#Visualise the relation

plot(x,y,col = "blue",main = "Height & Weight Regression",
     cex = 1.3,pch = 16,xlab = "Weight in Kg",ylab = "Height in cm")
abline(lm(y~x))



# Find height of a person with weight 70.
#predict(relation,70)


# Apply the lm() function.
relation <- lm(y~x)

a <- data.frame(x = 70)
height <-  predict(relation,a)
dev.off()
# Find weight of a person with height 160.

relation <- lm(x~y)
plot(y,x,col = "blue",main = "Height & Weight Regression",
     cex = 1.3,pch = 16,xlab = "Weight in Kg",ylab = "Height in cm")
abline(lm(x~y))
b <- data.frame(y = 160)
weight <-  predict(relation,b)


