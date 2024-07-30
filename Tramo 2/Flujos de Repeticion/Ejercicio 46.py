
cant = int(input("Ingrese la cantidad de números a ingresar: "))


if cant > 0:
    mayor = int(input("Ingrese el primer número entero: "))
    posicion_mayor = 1  
 
    for i in range(1, cant):
        numero = int(input("Ingrese el número entero: "))
        
        if numero > mayor:
            mayor = numero
            posicion_mayor = i + 1  

   
    print("El mayor número ingresado es:", mayor)
    print("Apareció en la posición:", posicion_mayor)
else:
    print("La cantidad debe ser mayor que 0.")
