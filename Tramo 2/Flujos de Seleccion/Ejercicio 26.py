
invitados = int(input("Ingrese la cantidad de invitados: "))
asientos = int(input("Ingrese la cantidad de asientos disponibles: "))


if asientos >= invitados:
    print("¡Todos los invitados pueden sentarse!")
else:
    asientos_faltantes = invitados - asientos
    print(f"Faltan {asientos_faltantes} asientos para que todos los invitados puedan sentarse.")
