#https://replit.com/join/epgdsnpcqu-frida-paulinapa

info_nutricional = {}
num_ingredientes = int(input("Ingrese el número de ingredientes en la receta: "))

for i in range(num_ingredientes):
    nombre_ingrediente = input("Ingrese el nombre del ingrediente: ")
    calorias = float(input(f"Ingrese las calorías por cada 100 gramos de {nombre_ingrediente}: "))
    proteina = float(input(f"Ingrese la cantidad de proteína por cada 100 gramos de {nombre_ingrediente}: "))
    carbohidratos = float(input(f"Ingrese la cantidad de carbohidratos por cada 100 gramos de {nombre_ingrediente}: "))
    grasas = float(input(f"Ingrese la cantidad de grasas por cada 100 gramos de {nombre_ingrediente}: "))
    info_nutricional[nombre_ingrediente] = {'calorias': calorias, 'proteina': proteina, 'carbohidratos': carbohidratos, 'grasas': grasas}

receta = {}

total_calorias = 0
total_proteina = 0
total_carbohidratos = 0
total_grasas = 0

for ingrediente, cantidad in receta.items():
    info = info_nutricional[ingrediente]
    total_calorias += (info['calorias'] * cantidad) / 100
    total_proteina += (info['proteina'] * cantidad) / 100
    total_carbohidratos += (info['carbohidratos'] * cantidad) / 100
    total_grasas += (info['grasas'] * cantidad) / 100

print("\nNutrientes totales en la receta:")
print(f"Calorías totales: {total_calorias} kcal")
print(f"Proteína total: {total_proteina} gramos")
print(f"Carbohidratos totales: {total_carbohidratos} gramos")
print(f"Grasas totales: {total_grasas} gramos")
