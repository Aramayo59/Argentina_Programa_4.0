
segundos = int(input("Ingrese el período de tiempo en segundos: "))

dias = segundos // 86400
horas = (segundos % 86400) // 3600
minutos = (segundos % 3600) // 60
segundos_restantes = segundos % 60


print(str(segundos) + " segundos equivalen a " + str(dias) + " días, " +
      str(horas) + " horas, " + str(minutos) + " minutos y " +
      str(segundos_restantes) + " segundos.")