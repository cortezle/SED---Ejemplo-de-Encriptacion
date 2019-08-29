def ConvertirLista(frase):
	return list(frase)

def ReverseLista(lst): 
    lst.reverse() 
    return lst

def ConvertirAFrase(lst):
	return "".join(lst)

def CifrarCesar(frase,k):
	if fraseInvertida==fraseInvertida.upper():
		abc="ABCDEFGHIJKLMNÑOPQRSTUVXYZ"
	else:
		abc="abcdefghijklmnñopqrstuvxwyz"
	cifrad=""
	for c in frase:
		if c in abc:
			cifrad += abc[ (abc.index(c)+k)%(len(abc))]
		else:
			cifrad+=c
	return cifrad

#recibimos nuestro modo, mensaje y clave
def obtenerMensajeTraducido(modo, mensaje, clave):
    #validamos si quiere desencriptar 
    if modo[0] == 'd':
        #para desencriptar un mensaje se usa la versión negativa de la clave
        clave= -clave
    traduccion = ''
    for simbolo in mensaje:
        # isalpha() devolverá True si la cadena es una letra mayúscula o minúscula entre A y Z
        # Si la cadena contiene algún caracter no alfabético, entonces isalpha() devolverá False
        if simbolo.isalpha():
            num = ord(simbolo)
            num += clave
            #isupper() devuelve True si la cadena sobre la cual es llamado contiene al menos una letra mayúscula y ninguna minúscula.
            #islower() devuelve True si la cadena sobre la cual es llamado contiene al menos una letra minúscula y ninguna mayúscula.
            if simbolo.isupper():
                #Comprobamos si num tiene un valor mayor que el valor ordinal de “Z”. Si es así, restamos 26 a num (porque hay 26 letras en total)
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


def obtenerModo():
    while True:
        print('¿Deseas encriptar o desencriptar un mensaje?')
        modo = input().lower()
        if modo in 'encriptar e desencriptar d'.split():
            return modo 
        else:
            print('Ingresa "encriptar" o "e" o "desencriptar" o "d"')

def obtenerFrase():
	return input("Ingrese frase: ")

def obtenerDesplazamiento():
	i=False
	k=0
	while(not i):
		try:
			k=int(input("Valor desplazamiento: "))
			i=True
		except ValueError:
			print('Error, introduce un numero entero')
	return k


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
           

