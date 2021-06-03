def eratostenes(x):
    multiplos=[]
    primos=[]
    for i in range(2,x+1):
        if i not in multiplos:                                 #Si i no está ya almacenada en multiplos:
            M=[i* k for k in range(2,int(x/3))]                #Generamos los multiplos de i con lista compresiva.    
            multiplos.extend(M)                                #Almacenamos en la lista multiplos todos los multiplos de i.
        if i not in multiplos: 
            primos.append(i)                                   #Si i no está en la lista de multiplos, lo añadimos a primos.
    return print(primos)

eratostenes(100)