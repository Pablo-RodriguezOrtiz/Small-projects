# ------------------------------------------------------------------------
#
#
# Made with python 3.8.8
#
#
# ------------------------------------------------------------------------

def bdecimal():
    x= input("Introduce el numero binario para convertirlo en decimal: ")
    y= 0
    posicion = len(x)-1
    for i in x:
        k = posicion
        y = y + (int(i)*2**k)
        posicion=posicion-1

    return("Tu número en base decimal es "+str(y))
