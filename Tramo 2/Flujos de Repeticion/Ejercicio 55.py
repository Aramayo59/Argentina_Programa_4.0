
primer_cliente = None
ultimo_cliente = None


documento = int(input("Ingrese el número de documento del cliente (-1 para finalizar): "))


while documento != -1:
    
    if primer_cliente == None:
        primer_cliente = documento

 
    ultimo_cliente = documento

  
    documento = int(input("Ingrese el número de documento del cliente (-1 para finalizar): "))


if primer_cliente != None and ultimo_cliente != None:
    print("El primer cliente atendido tuvo el número de documento:", primer_cliente)
    print("El último cliente atendido tuvo el número de documento:", ultimo_cliente)
else:
    print("No se atendió a ningún cliente.")
