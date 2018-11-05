install.packages(reshape2)
require(reshape2)
x = data.frame(name = c("John", "Mary"), 
               time = c(1,1),
               age = c(33,32),
               weight = c(90, 80),
               height = c(2,2),
               marks=c(45,47))
x


molten = melt(x, id = c("name", "time","marks"))
s=dcast(molten, formula =  name + time + marks ~ variable)



?dcast



molten
s


dcast(molten, formula =  subject ~ variable)
dcast(molten, formula = subject + time  ~ variable)
p=dcast(molten, formula = subject + time + marks  ~ variable)
?dcast