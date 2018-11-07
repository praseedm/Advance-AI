library(caret)
library(e1071)
dataset<-read.table(file.choose())
dataset=dataset[,-1]
v<-createDataPartition(dataset$V9,p=0.8,list=FALSE)
trainData<-dataset[v,]
testData<-dataset[-v,]

control <- trainControl(method="cv", number=10)
metric <- "Accuracy"

fit.knn<-train(V9~.,data=trainData,method="lda",metric=metric, trControl=control)
predictions<-predict(fit.knn,testData)
confusionMatrix(testData[,"V9"],predictions)

?createDataPartition