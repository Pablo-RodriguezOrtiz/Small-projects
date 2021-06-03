x<- as.numeric(readline("Introduce el numero decimal a convertir en octal: "))
y<- x
resto<-0
repeat{
  if (y>8 & y/8>8) {
    resto<- as.character(paste(floor(y%%8),resto,sep=""))
    y<- y/8}
  else {resto<- as.character(paste(floor(y/8),floor(y%%8),resto,sep=""))
  break}
}
z<- substr(resto,1,(nchar(resto)-1))
cat("Tu numero en octal es",z)