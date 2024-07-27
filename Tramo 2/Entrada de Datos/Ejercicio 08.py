
valor_hora = float(input("Ingrese el valor monetario de una hora de trabajo: "))


horas_trabajadas_por_dia = float(input("Ingrese la cantidad de horas trabajadas por día: "))


dias_habiles = 5


salario_diario = valor_hora * horas_trabajadas_por_dia


salario_semanal_habiles = salario_diario * dias_habiles


horas_sabado = horas_trabajadas_por_dia / 2


salario_sabado = valor_hora * horas_sabado


salario_semanal_total = salario_semanal_habiles + salario_sabado


print("El salario semanal total del trabajador es: " + str(salario_semanal_total))
