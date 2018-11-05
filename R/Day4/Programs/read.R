read.table("marks.txt")
read.table(file.choose())

p<-data.frame(read.csv("Pizza.csv"))
print(is.data.frame(p))
head(p)
max(p$Rating)
                        