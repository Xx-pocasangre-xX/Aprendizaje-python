#con la condicional (elif) si no se ejecuta el if por que no es valido se va ejecutar la siguiente y en este ejemplo 
#estariamos diciendo que si no tiene 10000 dolares o mas puedes ser que tenga 1000 o mas 
dinero_ingreso = 10000
dinero_gasto = 4000

#otra de la maneras en la cual podemos hacer un condicion es poniendo un if en otro if (ifs anidados)
if dinero_ingreso >= 10000 :
    if dinero_ingreso - dinero_gasto >= 3000:
        print("Tienes bastante dinero")
    else:
        print("estas gastando demasiado dinero")
    
elif dinero_ingreso >= 1000:
    print("estas bien economicamente en el pais")
    
    
else:
    print("esfuerzate mas por conseguir mas dinero")