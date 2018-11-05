
MultiplybyTwo<-function(x)
{ return (x*2)   }


M<-matrix(1:12,nrow=4,ncol=3)
N = apply(M, c(1,2), MultiplybyTwo)



#More Examples

# Create the matrix
m<-matrix(c(seq(from=-98,to=100,by=2)),nrow=10,ncol=10)

# Return the sum of each of the columns
apply(m,2,sum)

# Return the product of each of the rows
apply(m,1,prod)

apply(m,1,sum)


# Return a new matrix whose entries are those of 'm' modulo 10
apply(m,c(1,2),function(x) x%%10) 
