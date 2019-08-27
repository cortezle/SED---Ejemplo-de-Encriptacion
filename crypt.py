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