library(caret)
# Question 1
?createDataPartition
partition <-  createDataPartition(iris$Species,p=0.75,list=FALSE)
trainSet <- iris[partition,]
dim(trainSet)
testSet <- iris[-partition,]
dim(testSet)
model <- train(Species~.,data=trainSet,method="knn")

predictions <- predict(model,testSet)

# Question 2
confusionMatrix(testSet[,5],predictions)
?caretFuncs

# Question 3
ecoliData <- read.table(file.choose())
data <- ecoliData[,-1]
dim(data[,8])
partition <- createDataPartition(data$V2,p=0.8,list=F)
dim(partition)
trainSet <- data[partition,]
testSet <- data[-partition,]
dim(testSet)
model <- train(V9~.,data=trainSet,method="knn")
predictions <- predict(model,testSet)

confusionMatrix(testSet[,8],predictions)
# Question 4
ionData <- read.table(file.choose())

part <- createDataPartition(ionData$V1,p=.9,list=F)
trainSet = ionData[part,]
dim(trainSet)
testSet = ionData[-part,]
dim(testSet)
model <- train(V35~.,data=trainSet,method="knn")
predicts <- predict(model,testSet)
confusionMatrix(testSet[,35],predicts)