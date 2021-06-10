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
        fraccion="."                                            #Generamos la variable donde se almacena la parte fraccionaria.
    else:
        y = int(x)
    if y==0 or y==1:                                            #Si x es 1 o 0 no operamos. El resto es directamente x.
        resto=str(y)
    else:
        resto = ""
        while (y>=2):                                           #Vamos dividiendo entre 2 y guardando los restos.
            if (y//2>=2):
                resto=str(y%2)+str(resto)
                y=y//2
            else:                                               #Cuando no se puede seguir dividiendo entero, se coge todo.
                resto = str(y//2)+ str(y%2)+ str(resto)
                break
    if "." in x:                                                #Si es fraccionario, se calcula la parte fraccionaria.
        n=0
        z=float("0."+z)                                    #Se genera z, que es 0. + más la parte fraccionaria.
        while n<v:                                              #Se va multiplicando *2 y guardando la parte entera.
            z=z*2
            if z==1.00:                                         #Rompemos manualmente cuando el resultado es 1.00 o n = digitos.
                fraccion=fraccion+str(int(z))
                break
            elif z>1.00:
                fraccion=fraccion+str(int(z))
                z-=1
            else:
                fraccion=fraccion+str(int(z))
            n+=1
        resto=resto+fraccion                                    #Se le suma al resultado la parte fraccionaria y se presenta.
    return("Tu número en binario es "+resto)

dbinario()
