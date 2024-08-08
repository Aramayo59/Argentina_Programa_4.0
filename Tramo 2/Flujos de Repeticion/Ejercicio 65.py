
subtotal = 0
items_seleccionados = []
menu = {
    "Combo 1": 1550,
    "Combo 2": 1650,
    "Hamburguesa sola": 1300,
    "Hamburguesa con queso": 1400,
    "Gaseosa": 700,
    "Postre": 600,
    "Agregar aderezo": 100
}


print("Menú:")
for item, precio in menu.items():
    print("{} - ${}".format(item, precio))


opciones = ['1', '2', '3', '4', '5', '6', '7']
contador_viajes = 0


while contador_viajes < 10:
    eleccion = input("Seleccione una opción (1-7) o 'Terminar' para finalizar: ").strip()
    
    if eleccion == 'Terminar':
        break
    
    if eleccion in opciones:
        if eleccion == '1':
            subtotal += menu["Combo 1"]
            items_seleccionados.append("Combo 1")
        elif eleccion == '2':
            subtotal += menu["Combo 2"]
            items_seleccionados.append("Combo 2")
        elif eleccion in ['3', '4', '5', '6', '7']:
            if eleccion == '3':
                item = "Hamburguesa sola"
            elif eleccion == '4':
                item = "Hamburguesa con queso"
            elif eleccion == '5':
                item = "Gaseosa"
            elif eleccion == '6':
                item = "Postre"
            elif eleccion == '7':
                item = "Agregar aderezo"
            
            cantidad = int(input("Ingrese la cantidad deseada de '{}': ".format(item)))
            while cantidad <= 0:
                print("Cantidad inválida. Debe ser mayor a 0.")
                cantidad = int(input("Ingrese la cantidad deseada de '{}': ".format(item)))
            
            subtotal += menu[item] * cantidad
            items_seleccionados.append("{} x{}".format(item, cantidad))
    else:
        print("Opción no válida. Intente de nuevo.")
    
    
    print("Subtotal actual: ${}".format(subtotal))
    
    contador_viajes += 1


if subtotal < 1550:
    print("Pedido cancelado")
else:
    print("Monto total a pagar: ${}".format(subtotal))
    
    
    if items_seleccionados:
        item_mas_caro = max(items_seleccionados, key=lambda x: menu.get(x.split(' ')[0], 0) * int(x.split('x')[-1].strip() if 'x' in x else 1))
        print("Ítem más caro: {}".format(item_mas_caro))
    else:
        print("No se seleccionaron ítems.")
