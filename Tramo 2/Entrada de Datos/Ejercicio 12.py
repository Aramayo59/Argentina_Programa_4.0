
angulo1 = float(input("Ingrese el primer ángulo en grados: "))
angulo2 = float(input("Ingrese el segundo ángulo en grados: "))


if angulo1 <= 0 or angulo2 <= 0:
    print("Error: Los ángulos deben ser mayores a 0 grados.")
else:
    if angulo1 + angulo2 >= 180:
        print("Error: La suma de los dos ángulos debe ser menor a 180 grados.")
    else:
        
        angulo_restante = 180 - (angulo1 + angulo2)
        print("El valor del ángulo restante es: " + str(angulo_restante) + " grados.")
