library(caret)
library(e1071)
dataset<-iris
v<-createDataPartition(dataset$Species,p=0.8,list=FALSE)
trainData<-dataset[v,]
testData<-dataset[-v,]
fit.knn<-train(Species~.,data=trainData,method="knn")
predict(fit.knn,iris[1,1:4])

?createDataPartition