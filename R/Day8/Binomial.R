# Create a sample of 50 numbers which are incremented by 1.
x <- seq(0,50,by = 1)

# Create the binomial distribution.
y <- dbinom(x,50,0.5)

# Give the chart file a name.
#png(file = "dbinom.png")

# Plot the graph for this sample.
plot(x,y)

# Save the file.
dev.off()




# Probability of getting 26 or less heads from a 51 tosses of a coin.
p <- pbinom(26,51,0.5)
print(p) 


# How many heads will have a probability of 0.25 , when a coin is tossed 51 times.
x <- qbinom(0.25,51,1/2) 
print(x) 

x <- qbinom(1,51,1/2) 

# Find 8 random values from a sample of 150 with probability of 0.4.
x <- rbinom(8,150,.4) 
print(x) 


#calculations

p=28/52
choose(6,3)*(p^3)*((1-p)^(6-3))
dbinom(3, 6, 28/52)
