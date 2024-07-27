
sueldo_basico = float(input("Ingrese el sueldo básico: $"))
antiguedad = int(input("Ingrese la antigüedad en años: "))
estado_civil = input("Ingrese el estado civil (S: Soltero / C: Casado): ").strip().upper()


JUBILACION_PORCENTAJE = 0.11
OBRA_SOCIAL_PORCENTAJE = 0.03
SINDICATO_PORCENTAJE = 0.03
INCREMENTO_SOLTERO = 0.05
INCREMENTO_CASADO = 0.07


if estado_civil == 'S':
    incremento = INCREMENTO_SOLTERO * sueldo_basico * antiguedad
else:
    incremento = INCREMENTO_CASADO * sueldo_basico * antiguedad


sueldo_bruto = sueldo_basico + incremento

descuento_jubilacion = JUBILACION_PORCENTAJE * sueldo_bruto
descuento_obra_social = OBRA_SOCIAL_PORCENTAJE * sueldo_bruto
descuento_sindicato = SINDICATO_PORCENTAJE * sueldo_bruto


sueldo_neto = sueldo_bruto - (descuento_jubilacion + descuento_obra_social + descuento_sindicato)


print("Estado Civil: " + ("Soltero" if estado_civil == 'S' else "Casado"))
print("Sueldo básico: $" + str(round(sueldo_basico, 2)))
print("Antigüedad: " + str(antiguedad) + " años")
print("\nDescuentos:")
print("Jubilación - $" + str(round(descuento_jubilacion, 2)))
print("Obra Social - $" + str(round(descuento_obra_social, 2)))
print("Sindicato - $" + str(round(descuento_sindicato, 2)))
print("\nSueldo Neto - $" + str(round(sueldo_neto, 2)))
