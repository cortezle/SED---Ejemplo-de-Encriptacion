"""def ConvertirLista(frase):
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


def DesCifrarCesar(frase,k)
#frase = "hola esta es mi contraseña"
#fraseInvertida = "añesartnoc im se atse aloh"

#Se pide la frase 
frase = input("Ingrese : ")

#se convierte en lista para poder trabajarla
lista = ConvertirLista(frase)

#se invierte la lista
listaInvertida = ReverseLista(lista)

#se crea un string de la lista invertida
fraseInvertida = ConvertirAFrase(listaInvertida)
print(fraseInvertida)
print("#################################")

#valor de desplazamiento
k = int( input( "Valor desplazamiento: "))

cifrado = CifrarCesar(fraseInvertida,k)

print("eso es: ",cifrado)"""



#Aqui comienza lo que agregue, deje lo otro porque puede servir luego

TAM_MAX_CLAVE = 26

#Lucho

def ConvertirLista(frase):
	return list(frase)

def ReverseLista(lst): 
    lst.reverse() 
    return lst

def ConvertirAFrase(lst):
	return "".join(lst)

#Lucho

def obtenerModo():
    while True:
        print('¿Deseas encriptar o desencriptar un mensaje?')
        modo = input().lower()
        if modo in 'encriptar e desencriptar d'.split():
            return modo
        else:
            print('Ingresa "encriptar" o "e" o "desencriptar" o "d"')

def obtenerMensaje():
    print('Ingresa tu mensaje:')
    return input()

def obtenerClave():
    clave = 0
    while True:
        print('Ingresa el número de clave (1-%s)' % (TAM_MAX_CLAVE))
        clave = int(input())
        if (clave >= 1 and clave <= TAM_MAX_CLAVE):
            return clave

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

modo = obtenerModo()   
mensaje = obtenerMensaje()
clave = obtenerClave()
traduc = obtenerMensajeTraducido(modo, mensaje, clave)

print('Tu texto traducido con clave cesar es:')
print(traduc)


#se convierte en lista para poder trabajarla
lista = ConvertirLista(traduc)

#se invierte la lista
listaInvertida = ReverseLista(lista)

#se crea un string de la lista invertida
fraseInvertida = ConvertirAFrase(listaInvertida)
print("fraseInvertida + clave Cesar es: ")
print(fraseInvertida)
print("#################################")
