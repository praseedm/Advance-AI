head(mtcars)
table(mtcars$mpg)
cyl=table(mtcars$cyl)
prop.table(cyl)
prop.table(cyl)*100

table(mtcars$mpg,mtcars$cyl)

head(airquality)
head(CO2)
table(CO2$Plant,CO2$Treatment)