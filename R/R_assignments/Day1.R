
# Question 1
x<-3
y<-4
x*y
a<-(8/2)-(3*4)
a
b<-8/(2-3)*4
b

# Question 2
x<-(1:20)
x
y<-(20:1)
y
#rev(x)

# Question 3
x<-(1:30)
x
paste('label',x)

# Question 4
x<-"The quick brown fox jumps over the lazy dog"
x
y<-sub("brown","red",x)
y
substr(y,15,17)

# Question 5
b<-3
h<-4
peri<-2*(b+h)
peri
class(peri)

# Question 6
?rep
pattern<-c(4,6,3)
pattern
rep(pattern,10)


###############

string_Date<-"2018-10-24"
string_Date
class(string_Date)

x_date<-as.Date(string_Date)
x_date
class(x_date)

y<-as.POSIXct("2018-10-24 5:30")
y
class(y)

letters
x<-(1:10)
which(x<3)