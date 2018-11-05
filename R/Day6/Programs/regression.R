x <- c(151, 174, 138, 186, 128, 136, 179, 163, 152, 131)
y <- c(63, 81, 56, 91, 47, 57, 76, 72, 62, 48)

plot(x,y)
abline(lm(y~x))

x <- c(7,6,8,5,6,9)
y <- c(12,8,12,10,11,13)
# Apply the lm() function.
relation <- lm(y~x)

print(relation)





x=c(20,43,23,66,53,31,58,46,58,70,46,53,60,20,63,43,26,19,31,23)
y=c(120,128,141,126,134,128,136,132,140,144,128,136,146,124,143,130,124,121,126,123)
plot(x,y)
abline(lm(y~x))

# Apply the lm() function.
relation <- lm(y~x)

print(relation)

x=1:100
y=1:100

relation <- lm(y~x)

print(relation)

dev.off()

?lm