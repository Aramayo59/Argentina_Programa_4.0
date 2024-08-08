
numeros = []
numero = input("Ingresa un número (0 para terminar): ")

while numero != "0":
    numeros.append(float(numero))
    numero = input("Ingresa un número (0 para terminar): ")

if numeros:
    numero_maximo = max(numeros)
    numero_minimo = min(numeros)
    print(f"El número máximo ingresado es: {numero_maximo}")
    print(f"El número mínimo ingresado es: {numero_minimo}")
else:
    print("No se ingresaron números.")
