#declaracion de la matriz 
matriz=[]
#peticion del usuario para los renglones y columnas
renglones=int(input("numero de renglones "))
columnas=int(input("numero de columnas "))
#creacion de una matriz vacia con los renglones y columnas del usuario
#primer for para recorrer los renglones
for i in range(renglones):
	#.append para agregar el elemento dentro del parentesis al ultimo elemento de la lista
	matriz.append([])
	#segundo for es para recorrer las columnas
	for j in range(columnas):
		#esta ves se agregara un elemento vacio con el .append
		matriz[i].append(None)	
#creacion de la matriz con los valores que ingrese el usuario
for i in range(renglones):
	for j in range(columnas):
		print("escribe el elemento ",i,j)
		matriz[i][j]=input()
#imprimir la matriz 
print("Matriz a resolver:")
for i in range(renglones):
	print("|",end=" ")
	for j in range(columnas):
		print(matriz[i][j],end=" ")
	print("|")
#obtener el renglon pivote
#para recorrer el renglon se hara una lista que tenga los elementos al reves
recorrido=[]
#se hace una lista con los elementos necesarios
for j in range(columnas):
	recorrido.append(None)
#se llenan en orden desencente
for j in range(columnas):
	recorrido[j]=columnas-j-1
print(recorrido)

