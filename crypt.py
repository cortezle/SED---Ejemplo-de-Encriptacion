#esta funcion recibe un string, y lo devuelve en una lista separado por caracter
def ConvertirLista(frase):
	return list(frase)


#esta funcion recibe una lista y el metodo reverse la invierte, la retornamos
def ReverseLista(lst): 
    lst.reverse() 
    return lst


#recibe una lista y la vulve a unir como una string
def ConvertirAFrase(lst):
	return "".join(lst)

def obtenerMensajeTraducido(modo, mensaje, clave):
    if modo[0] == 'd':
        clave= -clave
    traduccion = ''
    for simbolo in mensaje:
        if simbolo.isalpha():
            num = ord(simbolo)
            num += clave

            if simbolo.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif simbolo.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            traduccion += chr(num)

        else:
            traduccion += simbolo
    return traduccion 

#siempre esta pidiendo si se desea encriptar o desencriptar
def obtenerModo():
    while True:
        print('¿Deseas encriptar o desencriptar un mensaje?')
        modo = input().lower()
	#aca cuando encuentre algunas de las siguientes que lo separe, practicamente es una validacion si se ingreso e o d
        if modo in 'encriptar e desencriptar d'.split():
            return modo 
        else:
            print('Ingresa "encriptar" o "e" o "desencriptar" o "d"')

#funcion que devuelve la frase ingresada
def obtenerFrase():
	return input("Ingrese frase: ")

#funcion que pide el valor de desplazamiento del cifrado cesar
def obtenerDesplazamiento():
	i=False
	k=0
	#validacion que ingrese un entero
	while(not i):
		try:
			k=int(input("Valor desplazamiento: "))
			i=True
		except ValueError:
			print('Error, introduce un numero entero')
	return k



#MAIN
while True:
        #Flujo programa

        #Primero se pide el modo (encriptar || desencriptar)
        modo = obtenerModo()

        #Se pide la frase 
        frase = obtenerFrase()

        #valor de desplazamiento
        k = obtenerDesplazamiento()

        #se convierte en lista para poder trabajarla
        lista = ConvertirLista(frase)

        #se invierte la lista
        listaInvertida = ReverseLista(lista)

        #se crea un string de la lista invertida
        fraseInvertida = ConvertirAFrase(listaInvertida)

        #se encripta con Cesar la fraseInvertida
        traduc = obtenerMensajeTraducido(modo, frase, k)

        #se imprime la respuesta del sistema
        print("#######################################")
        print("Resultado: ",traduc)
        print("Si deseas terminar digita salir si deseas continuar presiona cualquier tecla")
        salir = input()
        if salir == "salir":
            break
           

