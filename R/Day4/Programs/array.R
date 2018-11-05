result <- array((1:9),dim = c(3,3,2)) 
?array


column.names <- c("COL1","COL2","COL3")
row.names <- c("ROW1","ROW2","ROW3")
matrix.names <- c("Matrix1","Matrix2")

array(1:9,c(3,3,2),list(column.names,row.names,matrix.names))
