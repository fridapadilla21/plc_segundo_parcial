#https://replit.com/join/epgdsnpcqu-frida-paulinapa

def calcular_promedio(notas):
    return sum(notas) / len(notas)

def encontrar_nota_mas_alta(notas):
    return max(notas)

def encontrar_nota_mas_baja(notas):
    return min(notas)

num_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))
notas = []

for i in range(num_estudiantes):
    nota = float(input(f"Ingrese la nota del estudiante {i + 1}: "))
    notas.append(nota)

promedio = calcular_promedio(notas)
nota_maxima = encontrar_nota_mas_alta(notas)
nota_minima = encontrar_nota_mas_baja(notas)

aprobados = sum(1 for nota in notas if nota >= 60)
reprobados = num_estudiantes - aprobados

print("Promedio de las notas: ", promedio)
print("Nota más alta: ", nota_maxima)
print("Nota más baja: ", nota_minima)
print("Estudiantes que aprobaron: ", aprobados)
print("Estudiantes que reprobaron: ", reprobados)
