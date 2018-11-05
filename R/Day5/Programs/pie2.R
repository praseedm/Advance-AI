# Create data for the graph.
x <- c(21, 62, 10, 53)
x
labels <- c("London", "New York", "Singapore", "Mumbai")
labels
pie(x, labels, main = "City pie chart", col = rainbow(length(x)))

# Give the chart file a name.
png(file = "city_title_colours.jpg")

# Plot the chart with title and rainbow color pallet.
pie(x, labels, main = "City pie chart", col = rainbow(length(x)))

# Save the file.
dev.off()