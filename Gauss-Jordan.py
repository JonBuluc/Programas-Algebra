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
		#esta ves se agregara un el elemento por el usuario con el .append
		print("Ingrese el valor ",i,j)
		matriz[i].append(float(input()))	
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
#Se repetira el proceso anterior en la parte especifica donde se obtiene el 0 pero esta vez desde el ultimo renglon hacia arriba
#Se crea una lista en orden descendente para que los renglones se recorran alrevez
recorrido=[]
for i in range(renglones):
	recorrido.append(int(renglones-i-1))
#aqui empieza la obtencion de los demas 0 solo se haran operaciones en el elemento que esta arriba de i,i y en el resultado
for i in recorrido:
	#la accion se ejecutara solo si es diferente al primer renglon
	if i!=0:
		#el for es para ejecutar la accion a cada renglon superior
		for k in range(i):
			#se guarda la informacion para obtener el 0 y cuando se multiplique por el resultado no se borre la informacion
			memoria=matriz[i-k-1][i]
			#estas dos acciones son para que se haga la resta en el elemento superior y el resultado del renglon superior
			matriz[i-k-1][i]=(matriz[i][i]*(-memoria))+matriz[i-k-1][i]
			matriz[i-k-1][columnas-1]=(matriz[i][columnas-1]*(-memoria))+matriz[i-k-1][columnas-1]
#se imprime la matriz resuelta
print("Matriz resuelta")
for i in range(renglones):
	print("|",end=" ")
	for j in range(columnas):
		if j==columnas-1:
			print("|",end=" ")
		print(matriz[i][j],end=" ")
	print("|")
