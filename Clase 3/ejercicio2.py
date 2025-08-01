
#validar descuento
# si el cliente es vip y el monto es mayor a 10000 (2 valore ingresados)
# aplicar descuento del 15%
# no aplicar descuento pero informar

#anidamiento de condiciones
cliente_vip = int(input("El cliente es vip? (1.sí /2. no)"))
monto = float(input("Ingrese monto de la compra: "))

if cliente_vip == 1 or cliente_vip == 2:
    if cliente_vip == 1 and monto > 10000: 
        print("Aplicar descuento del 15%")
    else:
        print("No aplica descuento")
else:
    print("Opción incorrecta.")

    