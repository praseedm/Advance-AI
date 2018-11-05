input <- mtcars[,c('mpg','cyl')]
print(head(input))


# Plot the chart.
boxplot(mpg ~ cyl, data = mtcars, xlab = "Number of Cylinders",
        ylab = "Miles Per Gallon", main = "Mileage Data")

# Save the file.
dev.off()




# Plot the chart.
boxplot(mpg ~ cyl, data = mtcars, 
        xlab = "Number of Cylinders",
        ylab = "Miles Per Gallon", 
        main = "Mileage Data",
        notch = TRUE, 
        col = c("green","yellow","purple"),
        names = c("High","Medium","Low")
)
# Save the file.
dev.off()