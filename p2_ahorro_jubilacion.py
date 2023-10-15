# https://replit.com/join/epgdsnpcqu-frida-paulinapa

edad_actual = int(input("Edad actual: "))
edad_jubilacion = int(input("Edad de jubilación: "))
cantidad_deseada = float(input("Cantidad deseada para la jubilación: "))
rendimiento_anual = float(input("Rendimiento anual esperado (%): "))

años_hasta_jubilacion = edad_jubilacion - edad_actual

n_pagos_mensuales = años_hasta_jubilacion * 12

tasa_interes_mensual = (rendimiento_anual / 12) / 100

pago_mensual = (cantidad_deseada * tasa_interes_mensual) / (((1 + tasa_interes_mensual) ** n_pagos_mensuales) - 1)


print("Ahorre aproximadamente", pago_mensual)
