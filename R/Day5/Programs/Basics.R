#Draw a graph 
 plot.new()
 plot.window(xlim=c(0,10), ylim=c(0,10))
 axis(1)
 axis(2)
 #Plot a point
 points(8,8)
 title(main="The Overall Title")
 title(xlab="An x-axis label")
 title(ylab="A y-axis label")
 box()
 abline(a=6, b=1)
 abline(a = 2, b = 1, col = 6) #a=intercept,b=slop

 dev.off()
 
 #Plot a point
 plot.new()
 plot.window(xlim=c(0,10), ylim=c(0,10))
 axis(1)
 axis(2)
 x=5
 y=7
 points(x, y)
 #Plot a point using a special symbol
 points(x, y,pch=11 )
 points(x, y,pch=11,col=2)
 

 #Adding Connected Line Segments To A Plot
 plot.new()
 plot.window(xlim=c(1,4), ylim=c(0,3))
 x = c(1,2,3,4)
 y = c(0,2,1,3)
 lines(x, y)
 axis(1)
 axis(2)
 box()
 
 #draws vertical lines at the x values
 abline(v=1:4)
 
 #draws horizontal lines across the plot at y values
 abline(h=1:4)
 
 
 
 