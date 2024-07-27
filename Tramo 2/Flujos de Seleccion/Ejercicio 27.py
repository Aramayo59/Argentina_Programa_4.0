
edad = int(input("Ingrese su edad (entre 1 y 120 años): "))
genero = input("Ingrese su género ('F' para mujeres, 'M' para hombres): ").upper()
nombre = input("Ingrese su nombre: ")


if edad < 1 or edad > 120:
    print("Datos incorrectos. " + nombre + ", la edad debe estar entre 1 y 120 años.")
else:
    if genero != 'F' and genero != 'M':
        print("Datos incorrectos. " + nombre + ", el género debe ser 'F' para mujeres o 'M' para hombres.")
    else:
       
        if genero == 'F':
            if edad >= 60:
                print(nombre + " está en edad de jubilarse.")
            else:
                print(nombre + " no está en edad de jubilarse.")
        else:  
            if edad >= 65:
                print(nombre + " está en edad de jubilarse.")
            else:
                print(nombre + " no está en edad de jubilarse.")
