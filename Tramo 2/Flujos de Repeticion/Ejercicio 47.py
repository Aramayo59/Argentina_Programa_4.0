
nota = float(input("Ingrese la nota del examen (debe estar entre 0 y 10): "))


while nota < 0 or nota > 10:
    print("Nota inválida. Debe estar entre 0 y 10.")
    nota = float(input("Ingrese la nota del examen (debe estar entre 0 y 10): "))


print("La nota ingresada es:", nota)
