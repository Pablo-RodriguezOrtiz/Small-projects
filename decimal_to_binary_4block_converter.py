# ------------------------------------------------------------------------
#
#
# Made with python 3.8.8
#
#
# ------------------------------------------------------------------------

def dbinario():
    x = input("¿Qué número quieres pasar a binario? ")
    if "." in x:                                                #Si el número tiene parte decimal:
        y = int(x[0:x.find(".")])                               #Separamos la parte entera de la parte decimal.
        z = x[x.find(".")+1:]
        v = int(input("¿Cuántos dígitos quieres en la parte fraccionaria? "))   #Preguntamos el número de dígitos.
        fraccion=""                                             #Generamos la variable donde se almacena la parte fraccionaria.
    else:
        y = int(x)
    resto = ""                                                  #EMPEZAMOS PARTE ENTERA.
    if y==0 or y==1:                                            #Si x es 1 o 0, no operamos. El resto es directamente x.
        resto=str(y)
    else:
        while (y>=2):                                           #Vamos dividiendo entre 2 y guardando los restos.
            if (y//2>=2):
                resto=str(y%2)+str(resto)
                y=y//2
            else:                                               #Cuando no se puede seguir dividiendo entero, se coge todo.
                resto = str(y//2)+ str(y%2)+ str(resto)
                break
    esp=[4*i for i in range(1,len(resto)*2)]                    #Generamos múltiplos de 4 en función del resto.
    while len(resto) not in esp:                                #Usando los múltiplos, rellenamos con 0 a la izq hasta llegar...
        resto="0"+resto                                         #...  a uno de los múltiplos.
    presto=""
    for i in range(len(resto)):                                 #Recorremos el resto.
        if i in esp:                                            #Añadimos espacios en los índices múltiplos de 4.
            presto=presto+" "+resto[i]
        else:
            presto=presto+resto[i]
    if "." in x:                                                #Si es fraccionario, EMPEZAMOS PARTE FRACCIONARIA.
        n=0
        z=float("0."+z)                                         #Se genera z, que es 0. + más la parte fraccionaria.
        while n<v:                                              #Se va multiplicando *2 y guardando la parte entera.
            z=z*2
            if z==1.00:                                         #Rompemos manualmente cuando el resultado es 1.00 o n = digitos.
                fraccion=fraccion+str(int(z))
                break
            elif z>1.00:                                        #Si el resultado del z*2 es mayor a uno:
                fraccion=fraccion+str(int(z))                   #Nos quedamos la parte entera y restamos 1.
                z-=1
            else:                                               #Si el resultado del z*2 es menor a uno:
                fraccion=fraccion+str(int(z))                   #Nos quedamos la parte entera.
            n+=1
        esp=[4*i for i in range(1,len(fraccion)*2)]
        while len(fraccion) not in esp:                         #Usando los múltiplos, rellenamos con 0 a la dch hasta llegar...
            fraccion=fraccion+"0"                               #...  a uno de los múltiplos.
        pfraccion=""
        for i in range(0,len(fraccion)):                        #Recorremos el resto.
            if i in esp:                                        #Añadimos espacios en los índices múltiplos de 4.
                pfraccion=pfraccion+" "+fraccion[i]
            else:
                pfraccion=pfraccion+fraccion[i]
        resto=presto+"."+pfraccion                              #Unimos la parte entera con la parte fraccionaria y presentamos.
    return("Tu número en binario es "+resto)

dbinario()
