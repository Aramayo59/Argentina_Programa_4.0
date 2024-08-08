
total_efectivo = 0
total_tarjeta = 0
total_cheque = 0
total_ventas = 0

codigo = ""

while codigo != "F":
    
    importe = float(input("Ingrese el importe total de la venta: "))

    
    codigo = input("Ingrese la forma de pago (C: cheque, E: efectivo, T: tarjeta, F: finalizar): ").upper()
    
    if codigo == "E":
        
        importe_final = importe * 0.90
        total_efectivo += importe_final
    elif codigo == "T":
       
        importe_final = importe * 1.12
        total_tarjeta += importe_final
    elif codigo == "C":
        
        importe_final = importe * 1.20
        total_cheque += importe_final
    elif codigo == "F":
        break
    else:
        print("Código de forma de pago no válido. Intente nuevamente.")
        continue
    
    total_ventas += importe_final


iva = total_ventas * 0.21

print("Resumen del Día:")
print("| Forma de Pago    | Total     |")
print("| ---------------- | --------- |")
print("| Efectivo en Caja | $ %.2f |" % total_efectivo)
print("| Tarjeta Crédito  | $ %.2f |" % total_tarjeta)
print("| Cheques          | $ %.2f |" % total_cheque)
print("| Total de Venta   | $ %.2f |" % total_ventas)
print("| Importe del IVA  | $ %.2f |" % iva)
