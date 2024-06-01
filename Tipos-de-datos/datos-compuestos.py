#creamos una lista (array) o (arreglos) con []
#las listas se pueden modificar los datos

lista = ["David Gutierres","Soy David",True,1.85]

#esto es valido
#lista[2] = "hola mundo"

#el indice (elemtos) se empiezan a contar desde el 0 entre []
print(lista[0])


#las tuplas se escriben con con ()
#Las tuplas se tienen tipos de datos que nunca se van a poder cambiar

tupla = ("David Gutierres","Soy David",True,1.85)

#esto no es valido
#tupla[3] = "hola mundo"

print(tupla[0])

#creando un conjunto (set)
#no se puede acceer a elementos por indice y no almacena datos duplicados
conjunto = {"David Gutierres","Soy David",True,1.85}

#no se puede acceder a un elemento
#print (conjunto[3])  

print(conjunto)

#creando un diccionario (dict)
#se crea el nombre del elemento
diccionario = {
    'nombre' : "David Gutierres",
    'esta_feliz' : True,
    'altura' : 1.75,
    'dato_duplicado' : 1.75
}

print(diccionario["altura"])