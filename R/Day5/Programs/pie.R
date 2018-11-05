# Create data for the graph.
x <- c(21, 62, 10, 53)
labels <- c("London", "New York", "Singapore", "Mumbai2")
# Give the chart file a name.
png(file = "city1.jpg")
# Plot the chart.
pie(x,labels)
# Save the file.
dev.off()
getwd()