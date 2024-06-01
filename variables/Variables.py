 #las variables se declaran y luego se definan
 
 
#definiendo variables 
nombre ="David"
edad = 23

#definiendo variables con calmelCase 
primerNombre ="David"
tuEdad = 23

#definiendo variables con snake_case 
primer_nombre ="David"
tu_edad = 23

#cuando tenemos un INT podemos utilizar los f-strings los que tenemos que poner al principio antes de las comillas
#concatenar con f-strings

bienvenida = f"hola {nombre} de {edad} años de edad"

#si ya no queremos que una variable este mas declarada 
# del bienvenida (quitar #)

#luego ya solamente imprimimos con print la variable donde tenemos el mensaje de bienvenida
#podemos tener operadores de pertenencia con (in / not in)
print("david" in bienvenida)#true
print("david" not in bienvenida)#false

#imprimir la variable
print(bienvenida)



