x<- as.character(readline("Introduce el numero binario para convertirlo en decimal:"))
y<-0
for (i in (nchar(x)-1):0) {
  k<- nchar(x)-i
  y<- y+as.numeric(substr(x,k,k))*(2^i)}
cat("Tu número en base decimal es",y)