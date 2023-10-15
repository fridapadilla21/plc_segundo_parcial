#https://replit.com/join/epgdsnpcqu-frida-paulinapa

peso = float(input("¿Cual es tu peso en kilogramos? "))
print(" ")

min = int(input("¿Cuantos minutos dura la actividad? "))
print(" ")

actividad = input("¿Que actividad vas a realizar a)nadar, b)bicicleta, c) correr ")
print(" ")


if actividad == "a":
  calorias1 = peso * 0.8
  print("La calorias que quemaste son ", calorias1)
elif actividad == "b":
  calorias2 = peso * 6.4
  print("Las calorias que quemaste son ", calorias2)
elif actividad == "c":
  calorias3 = peso * 39.6
  print("Las calorias que quemaste son ", calorias3)
else:
  print("No corresponde a la actividad pedida")
