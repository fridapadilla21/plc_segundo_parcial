#https://replit.com/join/epgdsnpcqu-frida-paulinapa

distancia = float(input("¿Cual es la distancia a recorrer en millas? "))
rendi = int(input("¿Cual es el rendimiento en millas por galon? "))
precio_gasolina = float(input("¿Cual es el precio actual de gasolina por galon? "))
dias = int(input("¿Cuantos dias planeas viajar? "))

costo_gasolina = distancia / rendi * precio_gasolina
costo_total = costo_gasolina * dias
print("Tu costo total del viaje es de: ", costo_total)
