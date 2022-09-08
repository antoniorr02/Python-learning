def precioFinal(factura, porcentaje, personas):
    porcentaje /= 100
    preciofinal = (factura + factura*porcentaje)/personas
    return preciofinal

factura = float(input("Introduzca el precio de la factura "))
porcentaje = int(input("Introduzca el porcentaje de propina que se quiere dejar "))
personas = int(input("Introduzca el numero de personas "))

print(f"El precio final por persona es de {precioFinal(factura, porcentaje, personas)}")