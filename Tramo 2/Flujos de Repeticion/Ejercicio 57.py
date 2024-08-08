
cantidad_aprobados = 0
cantidad_desaprobados = 0
cantidad_aplazados = 0
total_alumnos = 0


legajo = int(input("Ingrese el número de legajo del alumno (-1 para finalizar): "))

while legajo != -1:
    
    nota = float(input("Ingrese la nota del examen final (entre 1 y 10): "))
    
    while nota < 1 or nota > 10:
        print("Nota no válida. Debe estar entre 1 y 10.")
        nota = float(input("Ingrese la nota del examen final (entre 1 y 10): "))
    
   
    if nota >= 4:
        cantidad_aprobados += 1
    else:
        cantidad_desaprobados += 1
    
    if nota == 1:
        cantidad_aplazados += 1
    
    total_alumnos += 1
    
    
    legajo = int(input("Ingrese el número de legajo del alumno (-1 para finalizar): "))


porcentaje_aplazados = (cantidad_aplazados / total_alumnos) * 100 if total_alumnos > 0 else 0


print("Cantidad de alumnos que aprobaron:", cantidad_aprobados)
print("Cantidad de alumnos que desaprobaron:", cantidad_desaprobados)
print("Porcentaje de alumnos que están aplazados (nota == 1)".format(porcentaje_aplazados))
