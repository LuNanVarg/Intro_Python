mes = 1 #contador
suma_ingresos = 0.0 #acumulador
ingresos = [] #lista
while mes <= 6:
    # solicitamos ingreso
    ingreso_str = input(f"Ingreso del mes {mes}: ").strip()
    # validamos que sea numérico - flotante
    # 12.3 -> 123
    # 5876.63 -> 587663
    if not ingreso_str.replace(".", '', 1).isdigit():
        print("Valor inválido, ingrese un numéro")
        continue
    ingreso = float(ingreso_str)
    # validamos valor no sea negativo
    if ingreso < 0:
        print("Valor inválido!")
        continue
    # acumulamos en suma_ingresos
    suma_ingresos += ingreso
    ingresos.append(ingreso) #agrego item a la lista
    mes += 1 

#imprimo resultados y lista creada
for item in ingresos:
    print(item)
print(suma_ingresos) #usar máscara para los decimales o la función round()
