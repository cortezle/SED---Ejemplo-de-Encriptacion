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

print("eso es: ",cifrado)
