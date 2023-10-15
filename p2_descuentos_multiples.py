# https://replit.com/join/epgdsnpcqu-frida-paulinapa

print("¿Cual es el precio de tu producto? ")
precio = float(input())
print("¿De que categoria es? A,B o C")
categoria = input()
print("¿cual es el numero de productos que llevas?")
productos = int(input())

if productos >10:
  extra = 0.05
else:
  extra = 0
  
if categoria == "a":
  des1 = precio -(precio * (0.10 + extra))
  print("Tu producto costaria: ",des1)
elif categoria == "b":
  des2 = precio -(precio * (0.05 + extra))
  print("Tu producto costaria: ",des2)
elif categoria == "c":
  des3 = precio - (precio * (0.02 + extra))
  print("Tu producto costaria: ", des3)
else:
  print("No sabemos de que tipo es")
