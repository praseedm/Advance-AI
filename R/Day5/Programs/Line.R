# Create the data for the chart.
v <- c(7,12,28,3,41)


# Plot the  chart. 
plot(v,type = "o")

# Save the file.
dev.off()



# Create the data for the chart.
v <- c(7,12,28,3,41)


# Plot the bar chart.
plot(v,type = "o", col = "red", xlab = "Month", ylab = "Rain fall",
     main = "Rain fall chart")

# Plot the bar chart.
plot(v,type = "s", col = "red", xlab = "Month", ylab = "Rain fall",
     main = "Rain fall chart")

?plot
# Save the file.
dev.off()




# Create the data for the chart.
v <- c(7,12,28,3,41)
t <- c(14,7,6,19,3)


# Plot the bar chart.
plot(v,type = "o",col = "red", xlab = "Month", ylab = "Rain fall", 
     main = "Rain fall chart")

lines(t, type = "o", col = "blue")

# Save the file.
dev.off()