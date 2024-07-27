
nota1 = float(input("Ingrese la nota del primer parcial (0-10): "))
nota2 = float(input("Ingrese la nota del segundo parcial (0-10): "))


if (0 <= nota1 <= 10) and (0 <= nota2 <= 10):
    
    estado = ""
    
   
    if nota1 >= 7 and nota2 >= 7:
        estado = "promocionó"
    
    
    if nota1 >= 4 and nota2 >= 4 and estado != "promocionó":
        estado = "aprobó"
    
    
    if estado == "":
        estado = "debe recuperar"
    
    
    print("El alumno", estado + ".")
else:
    print("Error: Las notas deben estar entre 0 y 10.")
