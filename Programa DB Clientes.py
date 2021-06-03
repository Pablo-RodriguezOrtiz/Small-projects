clientes={}                                                                 #Creamos el diccionario vacío como variable global.
def empresa():
    global clientes
    while True:                                                             #Mostramos el menú.
        print("-"*35)
        print("   Bienvenido.")
        print("-"*35)
        print("1. Añadir cliente.")
        print("2. Eliminar cliente.")
        print("3. Mostrar cliente.")
        print("4. Listar todos los clientes.")
        print("5. Listar clientes preferentes.")
        print("6. Terminar. \n")
        ops=["1","2","3","4","5","6"]
        x=input("Seleccione una de las opciones anteriores: ")
        while x not in ops:                                                 #Comprobamos que la opción está disponible.
            print("Opción no disponible.")
            x=input("Introduzca la opción deseada: ")                       #Si no lo está, la pedimos de nuevo.
            
############# Añadir.

        if x=="1":                                                          #Si elige añadir:
            while True:
                print("Ha seleccionado: Añadir cliente.")
                x=input("Introduzca el NIF del cliente: ").upper().replace(" "," ")  #Pedimos introducir el NIF del cliente.
                while True:
                    if len(x)!=9:
                        print("NIF no válido. Debe contener 8 dígitos y una letra.")
                        x=input("Introduzca un NIF válido: ").upper().replace(" "," ")
                    else:
                        break
                r=""
                while x in clientes:                                        #Si ya existe, se pide de nuevo.
                    print("Ese NIF ya se encuentra en la base.")
                    r=input("¿Desea intentarlo de nuevo?: <S>/<N>").lower() #Se pregunta si quiere intentarlo de nuevo.
                    if r=="s":
                        x=input("Introduzca el NIF del cliente: ")
                    if r=="n":
                        break
                if r=="no":                                                 #Si no quiere intentarlo otra vez, salimos.
                    break
                a=input("Introduza el nombre del cliente: ").strip().title()
                direcc=input("Introduzca la dirección del cliente: ")
                n=0
                while n<len(direcc):
                    if direcc[n] in "@#!¡?¿=><+_:;%&$)(":
                        print("La dirección contiene carácteres incorrectos.")
                        direcc=input("Introduzca una dirección correcta: ")
                        n=0
                    else:
                        n+=1
                b=[direcc]
                while True:                                                 #Preguntamos si quiere añadir otra direcc.
                    resp=input("¿Quiere añadir alguna dirección más? <S>/<N>: ").lower()
                    if resp=="s":
                        direcc=input("Introduzca la siguiente dirección del cliente: ")
                        n=0
                        while n<len(direcc):
                            if direcc[n] in "@#!¡?¿=><+_:;%&$)(":
                                print("La dirección contiene carácteres incorrectos.")
                                direcc=input("Introduzca una dirección correcta: ")
                                n=0
                            else:
                                n+=1
                        b.append(direcc)
                    else:
                        break
                telf=input("Introduzca el teléfono del cliente: ")
                while True:
                    if len(telf)!=9:
                        print("El teléfono debe tener 9 dígitos.")
                        telf=input("Introduce un número de teléfono válido: ")
                    else:
                        break
                n=0
                while n<len(telf):
                    if telf[n] not in "0123456789":
                        print("Error. Solo puede contener números.")
                        telf=input("Introduce un número de teléfono válido: ")
                        n=0
                    else:
                        n+=1
                c=[telf]
                while True:                                                 #Preguntamos si quiere añadir otro telf.
                    resp=input("¿Quiere añadir algún teléfono más? <S>/<N>: ").lower()
                    if resp=="s":
                        telf=input("Introduzca el siguiente teléfono del cliente: ")
                        while True:
                            if len(telf)!=9:
                                print("El teléfono debe tener 9 dígitos.")
                                telf=input("Introduce un número de teléfono válido: ")
                            else:
                                break
                        n=0
                        while n<len(telf):
                            if telf[n] not in "0123456789":
                                print("Error. Solo puede contener números.")
                                telf=input("Introduce un número de teléfono válido: ")
                                n=0
                            else:
                                n+=1
                        c.append(telf)
                    else:
                        break
                correoraw=input("Introduzca el correo del cliente: ")
                while True:
                    if correoraw.count("@")!=1:
                        print("El correo introducido no es válido.")
                        correoraw=input("Introduzca un correo válido: ")
                    else:
                        break
                correoraw=correoraw.lower().strip().split("@")
                n=0
                correo1=[]
                banned="*^!¡?¿ªº;:+,=)(%$#·&"
                while n<len(correoraw[0]):                                  #Eliminamos los caracteres prohibidos en el correo.
                    if correoraw[0][n] not in banned:                       #Recorriendolo 1 a 1.
                        correo1.append(correoraw[0][n])
                    n+=1
                correo1="".join(correo1)                                    #Lo transformamos en texto.
                correo2="".join(correoraw[len(correoraw)-1]).split(".")     #Dividimos la segunda parte del correo.
                if correo2[0][0]=="h":                                      #Según por la letra que empiece la ext.
                    correo2[0]="hotmail"                                   #Sustituimos por la extensión correcta.
                elif correo2[0][0]=="g":
                    correo2[0]="gmail"
                elif correo2[0][0]=="y":
                    correo2[0]="yahoo"
                if correo2[1][0]=="c":                                      #Y lo mismo con .com y .es
                    correo2[1]="com"
                elif correo2[1][0]=="e":
                    correo2[1]="es"
                correo2=".".join(correo2)                                   #Lo transformamos a texto.
                correo=str(correo1)+"@"+str(correo2)                        #Y lo pegamos todo listo para guardar.
                d=[correo]
                while True:                                                 #Preguntamos si quiere añadir otro correo.
                    resp=input("¿Quiere añadir algún correo más? <S>/<N>: ").lower()
                    if resp=="s":
                        correoraw=input("Introduzca el siguiente correo del cliente: ")
                        while True:
                            if correoraw.count("@")!=1:
                                print("El correo introducido no es válido.")
                                correoraw=input("Introduzca un correo válido: ")
                            else:
                                break
                        correoraw=correoraw.lower().strip().split("@")
                        n=0
                        correo1=[]
                        while n<len(correoraw[0]):                           #Eliminamos los caracteres prohibidos en el correo.
                            if correoraw[0][n] not in banned:                #Recorriendolo 1 a 1.
                                correo1.append(correoraw[0][n])
                            n+=1
                        correo1="".join(correo1)                             #Lo transformamos en texto.
                        correo2="".join(correoraw[len(correoraw)-1]).split(".")    #Dividimos la segunda parte del correo.
                        servicios=["hotmail","outlook","gmail","yahoo","gmx"]
                        if correo2[0] not in servicios:
                            if correo2[0][0]=="h":                            #Según por la letra que empiece la ext.
                                correo2[0]="hotmail"                          #Sustituimos por la extensión correcta.
                            elif correo2[0][0]=="g":
                                correo2[0]="gmail"
                            elif correo2[0][0]=="y":
                                correo2[0]="yahoo"
                        if correo2[1][0]=="c":                                #Y lo mismo con .com y .es
                            correo2[1]="com"
                        elif correo2[1][0]=="e":
                            correo2[1]="es"
                        correo2=".".join(correo2)                             #Lo transformamos a texto.
                        correo=str(correo1)+"@"+str(correo2)
                        d.append(correo)                                      #Y anexamos a la lista de correos.
                    else:
                        break
                e=input("¿Cliente preferente? <S>/<N>: ").lower()             #Preguntamos si es cliente VIP.
                if e=="s":
                    e=True
                else:
                    e=False
                datos={"Nombre":a,"Dirección":b,"Teléfono":c,"Correo":d,"Preferente":e}   #Formateamos los datos.
                clientes.update({x:datos})
                z=input("¿Desea añadir otro cliente? <S>/<N>: ").lower()    #Preguntamos si quiere añadir otro cliente.
                if z=="n":
                    break
                    
############# Eliminar.

        if x=="2":                                                          #Si elige eliminar:
            while True:
                if len(clientes)==0:                                        #Comprobamos que existen clientes.
                    print("Error. No existen clientes en la base de datos. \n")
                    break
                print("Ha seleccionado: Eliminar cliente.")
                x=input("Introduzca el NIF del cliente a eliminar: ").upper()   #Pedimos el NIF del cliente.
                r=""
                while x not in clientes:                                    #Comprobamos que  el cliente existe.
                    print("Ese cliente no existe.")
                    r=input("¿Desea intentarlo de nuevo?: <S>/<N>").lower() #Si no existe, preguntamos si quiere intentarlo.
                    if r=="s":
                        x=input("Introduzca el NIF del cliente a eliminar: ").upper()
                    if r=="n":                                              #Si dice que no, salimos.
                        break
                if r=="n":                                                  #Y volvemos a salir.
                    break
                confirm=input("Seguro que desea eliminar los datos de "+x+"? <S>/<N> ").lower()
                if confirm=="s":
                    clientes.pop(x)
                    print("Cliente "+x+" eliminado correctamente.")
                else:
                    break
                z=input("¿Desea eliminar otro cliente? <S>/<N>: ").lower()  #Preguntamos si quiere eliminar otro cliente.
                if z=="n":
                    break
                    
############# Mostrar.

        if x=="3":                                                          #Si elige mostrar clientes:
            while True:
                if len(clientes)==0:                                        #Si no hay clientes, da error y sale.
                    print("Error. No existen clientes en la base de datos. \n")
                    break
                print("Ha seleccionado: Mostrar cliente.")
                print("Estos son los clientes existentes:")
                for i in clientes:                                          #Mostramos todos NIF:Nombre existentes.
                    print(str(i)+": "+str(clientes[i]["Nombre"]))
                x=input("Introduzca el NIF del cliente a mostrar: ")        #Preguntamos cual de todos quiere mostrar completo.
                x=x.upper()
                r=""
                while x not in clientes:                                    #Comprobamos que el cliente escrito existe.
                    print("Ese cliente no existe.")
                    r=input("¿Desea intentarlo de nuevo?: <S>/<N>").lower() #Si no, preguntamos si quiere intentarlo de nuevo.
                    if r=="s":
                        x=input("Introduzca el NIF del cliente a mostrar: ").upper()
                    if r=="n":                                              #Si no quiere, rompemos.
                        break
                if r=="n":                                                  #Rompemos para salir del todo si r=no.
                    break
                for i in clientes[x]:                                       #Recorremos los valores de esa clave de x.
                    if type(clientes[x][i])==list:                          #Si es una lista, lo mostramos como str.
                        print("\t "+str(i)+": "+", ".join(clientes[x][i]))
                    elif type(clientes[x][i])==bool:                        #Si es booleano, cambiamos True a VIP...
                        if clientes[x][i]==True:
                            clientes[x][i]="VIP"
                            print("\t "+str(i)+": "+str(clientes[x][i]))
                        else:                                               #... y False a No VIP.
                            clientes[x][i]="No VIP"
                            print("\t "+str(i)+": "+str(clientes[x][i]))
                    else:
                        print("\t "+str(i)+": "+str(clientes[x][i]))        #Si no, lo mostramos como tal.
                z=input("¿Desea mostrar otro cliente? <S>/<N>: ").lower()
                if z=="n":
                    break
                    
############# Mostrar todos.
        if x=="4" and len(clientes)==0:                                     #Si no hay clientes, da error.
            print("No existen clientes para mostrar. \n")
        if x=="4":                                                          #Si elige mostrar clientes:
            print("Ha seleccionado: Mostrar listado completo de clientes.")
            for i in clientes:                                              #Recorre la lista mostrando NIF y Nombre.
                print(str(i)+": "+str(clientes[i]["Nombre"]))
                
############# Mostrar preferentes.

        if x=="5":                                                          #Si elige mostrar preferentes:
            pref={}                                                         #Almacenamos preferentes.
            nopref={}                                                       #Almacenamos no preferentes.
            for i in clientes:                                              #Recorremos la lista.
                if clientes[i]["Preferente"]==True:                         #Si es VIP lo añadimos a pref.
                    pref.update({i:clientes[i]["Nombre"]})
                else:                                                       #Si no es VIP lo añadimos a nopref.
                    nopref.update({i:clientes[i]["Nombre"]})
            if len(pref)==0:
                print("No existen clientes preferentes. \n")
            else:                                                           #Recorremos pref mostrando a los clientes.
                print("Clientes preferentes:")
                for i in pref:
                    print(str(i)+": "+str(pref[i]))
                    print("\n")
            v=input("¿Quieres ver los no preferentes? <S>/<N>").lower()     #Preguntamos si quiere ver también no preferentes.
            if v=="s":
                if len(nopref)==0:
                    print("No existen clientes no preferentes. \n")
                else:                                                       #Recorremos nopref mostrando a los clientes.
                    print("Clientes no preferentes:")
                    for i in nopref:
                        print(str(i)+": "+str(nopref[i]))
                        print("\n")
                        
############# Terminar.

        if x=="6":                                                          #Si elige terminar, return y listo.
            return("Finalizando...")
empresa()