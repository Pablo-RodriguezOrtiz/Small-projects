# ------------------------------------------------------------------------
#
#
# Made with python 3.8.8
#
#
# ------------------------------------------------------------------------

def odecimal():
    x= input("Introduce el numero octal para convertirlo en decimal: ")
    n=0
    while n<len(x):                                           #Recorremos el número para comprobar que no hay 8 ni 9.
        if x[n]=="8" or x[n]=="9":                            #Si encontramos un 8 o 9, pedimos un nuevo número y comprobamos.
            print("El número no está en base octal.")
            x= input("Introduce un número en base octal: ")
            n=0                                               #Reseteamos 0 para leer el número de nuevo desde el principio.
        else:
            n+=1
    y=0                                                       #Cuando el número no tiene 8 ni 9, calculamos.
    posicion = len(x)-1                                       #La posición es el número al que hay que elevar cada cifra.
    for i in x:                                               #Recorremos todo el número.
        k = posicion
        y = y + (int(i)*8**k)                                 #Vamos sumando el resultado de elevar el número a su posición-1.
        posicion=posicion-1                                   #Actualizamos el valor de posición para el siguiente valor.

    return("Tu número en base decimal es "+str(y))
