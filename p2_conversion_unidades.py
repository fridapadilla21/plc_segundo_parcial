#https://replit.com/join/epgdsnpcqu-frida-paulinapa

cantidad = int(input("¿cuanto es la cantidad que quieres convertir? <"))
unidad = input("¿Que unidad de medida es? (millas, metros, kilometros) ")
destino = input("¿A que unidad lo quieres convertir (millas, metros, kilometros) ")

if unidad == "millas" and destino == "metros":
  resultado1 = cantidad * 1609.34
  print(cantidad, "millas son", resultado1, "metros")
elif unidad == "millas" and destino == "kilometros":
  resultado2 = cantidad * 1.60934
  print(cantidad, "millas son", resultado2, "kilometros")
elif unidad == "metros" and destino == "millas":
  resultado3 = cantidad * 0.000621371
  print(cantidad, "metros son", resultado3, "millas")
elif unidad == "metros" and destino == "kilometros":
  resultado4 = cantidad * 0.001
  print(cantidad, "metros son", resultado4, "kilometros")
elif unidad == "kilometros" and destino == "millas":
  resultado5 = cantidad * 0.621371
  print(cantidad, "kilometros son", resultado5, "millas")
elif cantidad == "kilometros" and destino == "metros":
  resultado6 = cantidad * 1000
  print(cantidad, "kilometros son", resultado6, "metros")
else:
  print("Esta unidad no es posible, intente denuevo")
