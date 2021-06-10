# ------------------------------------------------------------------------
#
#
# Made with python 3.8.8
#
# As professor requested, we used "/" to separate characters and "//" to separate words.
# ------------------------------------------------------------------------

def amorse():
    codigo_morse = {                                                              #Introducimos el diccionario con el c.morse.
        "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.",
        "g": "--.", "h": "....", "i": "..", "j": "·---", "k": "-.-", "l": ".-..",
        "m": "--", "n": "-.", "ñ": "--.--", "o": "---", "p": ".__.", "q": "--.-",
        "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--",
        "x": "-..-", "y": "-.--", "z": "--..",
        "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
        "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
        ".": ".-.-.-", ",": "--..--", "?": "..--..","!": "-.-.--", "\"": ".-..-.",
        "\'": ".----.","+": ".-.-.","-": "-....-",   "/": "-..-.", ":": "---...",
        "=": "-...-", "_": "..--.-","$": "..._.._", "@": ".--.-.", "&": ".-...",
        "(": "-.--.", ")": "-.--.-"}
    codif=""                                                                     #Variable donde almacenamos el mensaje.
    x=input("Introduce la frase a codificar: ").lower()
    x= x.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u") #Homogeneizamos la frase.
    for i in range(len(x)):                                                      #Recorremos la frase introducida.
        if x[i] in codigo_morse and i==len(x)-1:                                 #Si es la última letra, no ponemos / al final.
            codif+=codigo_morse[x[i]]
        elif x[i] in codigo_morse:                                                   #La buscamos en el dicc y...
            codif+=codigo_morse[x[i]]+"/"                                            #... la cambiamos por su traducción y...
        elif x[i]==" ":                                                              #... el separador de letras al final.
            codif+="/"                                                            #Si es espacio, añadimos "/" y hacemos doble.
        else:                                                                     #Doble / = espacio entre palabras.
            codif+=x[i]
    return codif.strip()                                                          #Devolvemos el resultado.

amorse()