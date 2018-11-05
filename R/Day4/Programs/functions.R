new.function <- function(a)
{ for(i in 1:a)
{ b <- i^2
    print(b) } } 
# Call the function new.function supplying 6 as an argument.
new.function(6)


new.function <- function(a,b,c)
{ result <- a * b + c 
  print(result) }
# Call the function by position of arguments. 
new.function(5,3,11)
# Call the function by names of the arguments.
new.function(a = 11, b = 5, c = 3)




# Create a function with arguments.
new.function <- function(a = 3, b = 6) 
{ result <- a * b
print(result)
#return(result)
} 
# Call the function without giving any argument.
new.function()
# Call the function with giving new values of the argument.
new.function(9,5)




new.function <- function(a,b,c)
{ result <- a * b + c 
return(result) }
# Call the function by position of arguments. 
k=new.function(5,3,11)
print(k)




