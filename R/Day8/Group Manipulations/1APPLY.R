#Apply

M<-matrix(1,nrow=4,ncol=3)
apply(M,1,sum)  # to get row sum   
apply(M,2,sum)  # to get column sum  / colSums



x <- cbind(x1 = 3, x2 = c(1:8))
#obtain the row means
apply(x, 1, mean)
#obtain the column means
apply(x, 2, mean)

#obtain the row sum
row.sums <- apply(x, 1, sum)
#obtain the column sum
col.sums <- apply(x, 2, sum)


N=rbind(cbind(x, Rtot = row.sums), Ctot = c(col.sums, sum(col.sums)))
N

#Applying apply to an Array

A<-array(1,c(2,3,4))
apply(A, 1, sum)
apply(A, 2, sum)
apply(A, 3, sum)



