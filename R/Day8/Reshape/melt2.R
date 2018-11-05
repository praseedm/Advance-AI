install.packages("reshape2")
require(reshape2)
aql <- melt(airquality, id = c("Month", "Day"))
aqw <- dcast(aql, Month + Day ~ variable)
head(aqw)
head(aql)
head(airquality)

