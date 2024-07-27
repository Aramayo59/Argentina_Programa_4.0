
numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))
operacion = input("Ingrese la operación (+, -, *, /): ")


def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "ERROR"
    else:
        return a / b


operaciones = {
    '+': sumar,
    '-': restar,
    '*': multiplicar,
    '/': dividir
}


if operacion in operaciones:
    resultado = operaciones[operacion](numero1, numero2)
    print("Resultado:", resultado)
else:
    print("Operación no válida")
