
nota = int(input("Ingrese la nota del examen (debe estar entre 0 y 10): "))


while (nota != 0 and nota != 2 and not (4 <= nota <= 10)):
    print("Nota inválida. Debe ser 0, 2, o un valor entre 4 y 10.")
    nota = int(input("Ingrese la nota del examen (debe estar entre 0 y 10): "))


print("La nota ingresada es:", nota)
