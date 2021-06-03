def descomp():
    x=input("Introduce el numero a descomponer: ")
    y=""
    n=0
    k = len(x)-1
    while n<len(x):
        if n!=len(x)-1:
            y = y+str(x[n])+"*10**"+str(k)+" + "
        else:
            y = y+str(x[n])+"*10**"+str(k)
        k=k-1
        n+=1
    return(y)