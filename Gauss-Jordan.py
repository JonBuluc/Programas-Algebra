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
		matriz[i][j]=int(input())
#imprimir la matriz 
print("Matriz a resolver:")
for i in range(renglones):
	print("|",end=" ")
	for j in range(columnas):
		if j==columnas-1:
			print("|",end=" ")
		print(matriz[i][j],end=" ")
	print("|")
print()
#obtener el renglon pivote
#el proceso de Gauss Jordan es por los renglones el for nos servira para hacer las respectivas operaciones
for i in range(renglones):
	#este for sera para que el elemento i de la columna se divida entre los demas y asi mismo al final
	#se guardara el elemento en un espacio para que cuando se divida entre si misma no se pierda su  valor
	#orginal y asi no afecte los elementos que van despues de el
	memoria=matriz[i][i]
	for j in range(columnas):
		matriz[i][j]=matriz[i][j]/memoria
	#condicion especial de una accion que se hara si el renglon que se esta trabajando no es el ultimo
	#ya que si es el ultimo no tiene que restar sus elementos a un renglon inferior porque no existe un renglon inferior
	if i!=renglones-1:
		#este for es para que recorra los renglones inferiores asi si se encuentra en el renglon 0 de 2 
		#hara la accion para el renglon 1 y 2 y si se encuentra en el renglon  2 de 3 hara la accion para el renglon 3 
		for k in range(renglones-i-1):
			#se guardara en un espacio el elemento debajo del pivote que queremos que sea 0 para que cuando se continue
			#no se borre la informacion original
			memoria=matriz[i+k+1][i]
			#este for es para haga la resta elemento a elemento y que debajo de la diagonal principal queden solo 0
			for j in range(columnas):
				matriz[i+k+1][j]=(matriz[i][j]*(-memoria))+matriz[i+k+1][j]
#se imprime la matriz resuelta
print("Matriz resuelta")
for i in range(renglones):
	print("|",end=" ")
	for j in range(columnas):
		if j==columnas-1:
			print("|",end=" ")
		print(matriz[i][j],end=" ")
	print("|")
