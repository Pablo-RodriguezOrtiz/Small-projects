x<- as.character(readline("Introduce el numero en base octal para convertirlo en decimal:"))
y<-0
for (i in (nchar(x)-1):0) {
  k<- nchar(x)-i
  y<- y+as.numeric(substr(x,k,k))*(8^i)}
cat("Tu n�mero en base decimal es",y)