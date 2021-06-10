# ------------------------------------------------------------------------
#
#
# Made with python 3.8.8
#
#
# ------------------------------------------------------------------------

fact={}                                                          #Definimos las 3 variables globales.
deb=0
money=0

def añadir():
    global fact, deb, money                                      #Decimos a la función que use las variables globales.
    print("Ha elegido añadir factura.")
    x=input("Introduzca el número de factura: ")                 #Se pide el número de factura.
    while x in fact:                                             #Se comprueba que dicha factura no existe.
        print("Ese número de factura ya existe.")                #Si existe, se pide de nuevo.
        x=input("Introduzca el número de factura: ")
    y=input("Introduzca el importe de la factura: ")             #Se pide el importe de la factura.
    n=0
    while n<len(y):                                              #Se recorre el valor introducido.
        if y.count(".")>1:
            print("El importe introducido no es un número como tal.")
            y=input("Introduzca el importe de la factura: ")
            n=0
        if y[n] not in "0123456789.":                            #Si se detecta algo diferente a un número:
            print("El importe solo puede contener números.")
            y=input("Introduzca el importe de la factura: ")     #Se pide introducir de nuevo y se vuelve a recorrer.
            n=0
        else:
            n+=1
    y=float(y)
    while y <=0.00:                                              #Se comprueba que el valor es mayor a 0.
        print("El importe debe ser mayor a 0€")
        y=float(input("Introduzca el importe de la factura: "))
    fact.update({x:y})                                           #Se añade al diccionario.
    deb+=y
    return ("Actualmente en caja hay "+str(money)+"€ y se deben "+str(deb)+"€.")

def pagar():
    global fact, deb, money                                      #Decimos a la función que use las variables globales.
    print("Ha elegido pagar factura.")
    x=input("Introduzca el número de factura: ")                 #Se pide el número de factura.
    while x not in fact:                                         #Se comprueba que ese número existe.
        print("Dicha factura no existe, pruebe de nuevo.")
        x=input("Introduzca el número de factura: ")
    deb-=fact[x]                                                 #Se actualiza el contador de dinero debido.
    money+=fact[x]                                               #Se actualiza el contador de dinero pagado.
    fact.pop(x)                                                  #Se elimina la factura pagada del diccionario.
    return ("Actualmente en caja hay "+str(money)+"€ y se deben "+str(deb)+"€.")

def menu():                                                    
    while True:                                                  #Bucle infinito hasta que decidamos terminar.
        print("Bienvenido.")
        print("Opciones disponibles:")                           #Mostramos las opciones disponibles.
        print("1. Añadir factura.")
        print("2. Pagar factura.")
        print("3. Terminar.")
        op=["1","2","3"]                                         #Almacenamos opciones disponibles.
        x=input("Seleccione una de las opciones disponibles: ")
        while x not in op:                                       #Comprobamos que existe la opción, si no se pide de nuevo.
            print("Opción no disponible, pruebe de nuevo.")
            x=input("Seleccione una de las opciones disponibles: ")
        if x=="1":                                               #Si elige añadir, invocamos la función.
            while True:                                          #Bucle infinito hasta que no quiera añadir más.
                añadir()
                print("Actualmente en caja hay "+str(money)+" € y se deben "+str(deb)+" €.")   #Mostramos como queda la caja.
                x=input("Desea añadir una nueva factura? <Si>/<No> ").lower().replace("í","i")
                if x=="no":
                    break
        elif x=="2" and len(fact)==0:                            #Si elige pagar y no hay factura, vuelve al inicio.
            print("No existen facturas por pagar.")
        elif x=="2":                                             #Si elige pagar, invocamos la función.
            while True:                                          #Bucle infinito hasta que no quiera pagar más.
                pagar()
                print("Actualmente en caja hay "+str(money)+" € y se deben "+str(deb)+" €.")   #Mostramos como queda la caja.
                x=input("Desea pagar una nueva factura? <Si>/<No> ").lower().replace("í","i")
                if x=="no":
                    break
        elif x=="3":
            print("La operación ha finalizado. En caja hay "+str(money)+" € y se deben "+str(deb)+" €.")
            break                                                #Invocamos al comando break para detener por completo.
