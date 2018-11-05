#1Generate random numbers whose distribution is normal


x <- rnorm(50,25,1)

# Plot the histogram for this sample.
hist(x, main = "Normal DIstribution")
m=mean(x)
s=sd(x)

# 2) Probability distribution
y <- dnorm(x, m, s)
round(y,2)
plot(x,y)



#3) cumulative distribution
z <- pnorm(x, mean = m, sd = s)

# Plot the graph.
plot(x,z)
dev.off()


# 4) quantile distribution
k <- qnorm(z, mean = (x), sd = sd(x))
k



