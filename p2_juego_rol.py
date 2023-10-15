#https://replit.com/join/epgdsnpcqu-frida-paulinapa

personajes = {
     "guerrero": {"vida": 100, "ataque": 10, "defensa": 5},
     "mago": {"vida": 80, "ataque": 12, "defensa": 3},
     "ladrón": {"vida": 90, "ataque": 8, "defensa": 7},
 }

def lanzar_dado():
     return random.randint(1, 6)

def combatir(jugador, enemigo):
     while jugador["vida"] > 0 and enemigo["vida"] > 0:
         ataque_jugador = jugador["ataque"] + lanzar_dado()
         defensa_enemigo = enemigo["defensa"] + lanzar_dado()

         if ataque_jugador > defensa_enemigo:
             dano = ataque_jugador - defensa_enemigo
             enemigo["vida"] -= dano
             print("Has infligido", dano, "puntos de daño al enemigo. Vida del enemigo: ", {enemigo['vida']})
         else:
             print("El enemigo ha bloqueado tu ataque.")

         if enemigo["vida"] <= 0:
             print("¡Has derrotado al enemigo!")
             break

         ataque_enemigo = enemigo["ataque"] + lanzar_dado()
         defensa_jugador = jugador["defensa"] + lanzar_dado()

         if ataque_enemigo > defensa_jugador:
             dano = ataque_enemigo - defensa_jugador
             jugador["vida"] -= dano
             print("El enemigo te ha infligido", {dano}, "puntos de daño. Tu vida: ", {jugador['vida']})
         else:
             print("Has bloqueado el ataque del enemigo.")

         if jugador["vida"] <= 0:
             print("¡Has sido derrotado por el enemigo!")
             break

print("Elige un personaje: guerrero, mago o ladrón")
personaje_elegido = input().lower()
if personaje_elegido not in personajes:
     print("Personaje no válido. Elige entre guerrero, mago o ladrón.")
     exit()

jugador = personajes[personaje_elegido]

enemigo = {"vida": 60, "ataque": 9, "defensa": 4}
print("Has elegido al", personaje_elegido, ".Comienza el combate contra un enemigo.")
combatir(jugador, enemigo)
