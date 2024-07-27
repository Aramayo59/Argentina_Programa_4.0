
edad = int(input("Ingrese su edad: "))
estatura = float(input("Ingrese su estatura en metros: "))

if edad >= 10 and estatura > 1.60:
    
    print("¡Puede acceder!")
else:
    
    if edad < 10:
        print("Lo siento, eres demasiado joven para acceder.")
    else:  
        if estatura <= 1.60:
            print("Lo siento, eres demasiado bajo para acceder.")
