# ------------------------------------------------------------------------
#
#
# Made with python 3.8.8
#
#
# ------------------------------------------------------------------------

def doctal():
    x = input("¿Qué número quieres pasar a octal? ")
    y = int(x)
    resto = ""
    while (y>8):
        if (y//8>8):                                       #Si el resultado de dividir entre 8 es mayor a 8:
            resto=str(y%8)+str(resto)                      #Guardamos el resto de la división a la izquierda de lo anterior.
            y=y//8                                         #Actualizamos y con el resultado de la división entera entre 8.
        else:                                              #Cuando el resultado no es mayor a 8:
            resto = str(y//8)+ str(y%8)+ str(resto)        #Guardamos el cociente, luego el resto y al lado lo anterior.
            break
    return("Tu número en octal es "+resto)

doctal()
