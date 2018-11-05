# Create the data for the chart.
H <- c(7,12,28,3,41)


# Plot the bar chart.
barplot(H)

dev.off()

# Create the data for the chart.
H <- c(7,12,28,3,41)
M <- c("Mar","Apr","May","Jun","Jul")


# Plot the bar chart.
barplot(H,names.arg = M,xlab = "Month",ylab = "Revenue",col = "blue",
        main = "Revenue chart",border = "red")


dev.off()


# Create the input vectors.
colors <- c("green","orange","brown")
months <- c("Mar","Apr","May","Jun","Jul")
regions <- c("East","West","North")

# Create the matrix of the values.
Values <- matrix(c(2,9,3,11,9,4,8,7,3,12,5,2,8,10,11),nrow = 3,ncol = 5,byrow = TRUE)


# Create the bar chart.
barplot(Values,main = "total revenue",names.arg = months,xlab = "month",ylab = "revenue",
        col = colors)

# Add the legend to the chart.
legend("topleft", regions, cex = 1.3, fill = colors)

# Save the file.
dev.off()