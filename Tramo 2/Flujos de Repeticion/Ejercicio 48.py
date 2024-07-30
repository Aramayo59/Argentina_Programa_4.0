
operacion = ''


operacion = input("Ingrese la operación a realizar ('+', '-', '*', '/', 'F' para finalizar): ")


while operacion != 'F':
    if operacion in ['+', '-', '*', '/']:
        
        num1 = int(input("Ingrese el primer número entero: "))
        num2 = int(input("Ingrese el segundo número entero: "))
        
      
        if operacion == '+':
            resultado = num1 + num2
        elif operacion == '-':
            resultado = num1 - num2
        elif operacion == '*':
            resultado = num1 * num2
        elif operacion == '/':
            if num2 != 0:
                resultado = num1 / num2
                print("El resultado de", num1, operacion, num2, "es:", resultado)
            else:
                print("Error: División por cero no permitida.")
        else:
            
            print("Operación inválida. Por favor, ingrese una operación válida.")
    else:
        print("Operación inválida. Por favor, ingrese una operación válida.")
    
    
    operacion = input("Ingrese la operación a realizar ('+', '-', '*', '/', 'F' para finalizar): ")


print("Finalizando el programa.")
