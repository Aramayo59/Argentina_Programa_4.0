
USUARIO_CORRECTO = "admin"
CONTRASENA_CORRECTA = "123456"


MAX_INTENTOS = 3


intentos = 0
acceso_concedido = False


while intentos < MAX_INTENTOS and not acceso_concedido:
    
    usuario = input("Ingrese el nombre de usuario: ")
    contrasena = input("Ingrese la contraseña: ")

    
    if usuario == USUARIO_CORRECTO and contrasena == CONTRASENA_CORRECTA:
        acceso_concedido = True
    else:
        intentos += 1
        if intentos < MAX_INTENTOS:
            print("Credenciales incorrectas. Te quedan " + str(MAX_INTENTOS - intentos) + " intentos.")
        else:
            print("Se ha bloqueado la cuenta")


if acceso_concedido:
    print("Acceso concedido")
