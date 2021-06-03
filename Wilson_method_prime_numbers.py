def primos(x):                                                    #Método de Wilson
    import math
    nprimos=[]
    for i in range(2,x+1):                                        #Sacamos todos los números primos entre 2 y el que digamos.
        if (math.factorial(i-1)+1)%i==0:                          #Si (número-1)! más 1 entre el número tiene como resto 0:
            nprimos.append(i)                                     #Ese número es primo y lo añadimos a la lista.
        else:
            continue
    print(nprimos)

primos(100)