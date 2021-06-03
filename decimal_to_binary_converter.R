x<- as.numeric(readline("Introduce el numero decimal a convertir en binario: "))
y<- x
resto<-0
repeat{
  if (y>2 & y/2>2) {
    resto<- as.character(paste(floor(y%%2),resto,sep=""))
    y<- y/2}
  else {resto<- as.character(paste(floor(y/2),floor(y%%2),resto,sep=""))
  break}
}
z<- substr(resto,1,(nchar(resto)-1))
cat("Tu numero en binario es",z)