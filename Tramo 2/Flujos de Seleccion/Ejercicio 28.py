
numero_mes = int(input("Ingrese el número del mes (1-12): "))

meses = [
    "enero",   
    "febrero", 
    "marzo",   
    "abril",   
    "mayo",    
    "junio",   
    "julio",   
    "agosto",  
    "septiembre", 
    "octubre", 
    "noviembre", 
    "diciembre"  
]


if 1 <= numero_mes <= 12:
   
    nombre_mes = meses[numero_mes - 1]
    print("El mes es:", nombre_mes)
else:
    print("Número de mes inválido. Debe estar entre 1 y 12.")
