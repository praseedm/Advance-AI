library(caret)
library(e1071)
dataset<-iris
v<-createDataPartition(dataset$Species,p=0.8,list=FALSE)

fit.knn<-train(Species~.,data=dataset,method="knn")
predict(fit.knn,iris[1,1:4])

?createDataPartition