# -*- coding: utf-8 -*-
"""
Created on Thu Nov 27 21:20:33 2025

@author: equipo 1
"""

NEGRO   = "\033[30m"
ROJO    = "\033[31m"
VERDE   = "\033[32m"
AMARILLO = "\033[33m"
AZUL    = "\033[34m"
MORADO  = "\033[35m"
CIAN    = "\033[36m"
BLANCO  = "\033[37m"

# Reset
RESET = "\033[0m"

# TALLER 3

import random as r
import numpy as np

import time

turno_jugador = 0

# ------JUEGO DE MESA------

# ---LISTAS Y MATRICES----
# TABLERO

tablero = np.empty((5, 5), dtype="U20") #tablero que almacene hasta 20 caracteres por los emojis

tablero_copia = np.full((5, 5), "  ", dtype="U20") #Crear tablero vacio con " "

#En la posicion de los jugadores representarlos


globos_lista = ["Real", "Falso"]
# -------------------Rellenar tablero-----------------

# Rellenar casillas de la primera fila
tablero[0][0] = "🏠"
tablero[0][1] = "➡"
tablero[0][2] = "🧺"
tablero[0][3] = "🏪"
tablero[0][4] = "💲"

# Rellenar ultima columna
tablero[1][4] = "➡"
tablero[2][4] = "🧺"
tablero[3][4] = "🏪"
tablero[4][4] = "💲"

# Ultima fila
tablero[4][0] = "💲"
tablero[4][1] = "🏪"
tablero[4][2] = "🧺"
tablero[4][3] = "🤐"  # no se que emoji poner jkjsks (escondite)
tablero[4][4] = "💲"

# Primera columna dando casi toda la vuelta
tablero[3][0] = "🎲"
tablero[2][0] = "💲"
tablero[1][0] = "🤐"

# Rellenar espacios vacios

tablero[1][1] = "⬜"
tablero[2][2] = "⬜"
tablero[3][3] = "⬜"
tablero[1][2] = "⬜"
tablero[1][3] = "⬜"
tablero[2][1] = "⬜"
tablero[2][3] = "⬜"
tablero[3][1] = "⬜"
tablero[3][2] = "⬜"

# Matriz globos-------------------------------------------BORRAR---------
#globos = np.zeros([3, 3])

#N = len(globos)

#for i in range(len(globos)):
 #   for j in range(len(globos[0])):
  #      globos[i][j] = r.randint(0, 1)
#----------------------------------------------------------------------------
# Dado
dado = [1, 2, 3, 4]

# ---------------Jugadores parametros---------




# ____JUGADOR 01 (TURNO 0)

Jugador1_vidas = 3
monedas_Jugador1 = 0
inventario_J1 = []  # Aun no se si dejarlo como lista o como numeros y hacer condiciones con eso
paraguas_J1 = 0  # Si el paraguas es igual a 1 aplicara la defensa
escondite_J1 = 0  # si es igual a 0 no estara escondido mientras que si es 1 si

jugador_1_x = 0
jugador_1_y = 0

# ____JUGADOR 02 (TURNO 1)

Jugador2_vidas = 3
monedas_Jugador2 = 0
inventario_J2 = []
paraguas_J2 = 0
escondite_J2 = 0

jugador_2_x = 0
jugador_2_y = 0

#--------------------------------representar jugadores
tablero_copia[jugador_1_x][jugador_1_y] = "🟦"  #esto representa a los jugadores
tablero_copia[jugador_2_x][jugador_2_y] = "🟥"

# ------------------SUBPROGRAMAS---------
def mostrar_tablero():
    global tablero_copia, jugador_1_x, jugador_1_y, jugador_2_x, jugador_2_y

    limpiar_tableroCopia()

    tablero_copia[jugador_1_x][jugador_1_y] = "🟦"
    tablero_copia[jugador_2_x][jugador_2_y] = "🟥"
    
    if jugador_1_x == jugador_2_x and jugador_1_y == jugador_2_y:
        tablero_copia[jugador_1_x][jugador_1_y] = "👥"  # si ambos estan en la misma posicion

    print("\n")
    print(tablero_copia)


def limpiar_tableroCopia():
    global tablero_copia
    for i in range(5):
        for j in range(5):
            tablero_copia[i][j] = tablero[i][j]

def introduccion():
    print("-----------------Bienvenido a la guerra de globos de agua--------\n")
    print("Iniciar juego?: \n")


def jugar_bienvenida():
    if elegir == "si":
        print("\nIniciando juego..\n")


def cubo(turno_jugador):
    global inventario_J1, inventario_J2 #Para obtenerlas fuera del subprograma

    print("\n¡Has caido en la casilla de globos! 🎈")
    print("Recogiendo globo")
    tomar_globo = input("NO para cancelar: ").lower()
    
    if tomar_globo != "no":

        if turno_jugador == 0:
            print("¡Has recogido un globo! 🎈\n")
            inventario_J1.append("Globo")
        
        elif turno_jugador ==1:
            print("¡Has recogido un globo!\n")
            inventario_J2.append("Globo")

    elif tomar_globo == "no":
        print("No obtuviste nada 😕\n")
    

def avanzar(turno_jugador, tablero, pos_x, pos_y):

    global jugador_1_x, jugador_1_y, jugador_2_x, jugador_2_y

    input("¿Deseas avanzar?: \n")
    avanzar_cantidad = r.choice(dado)

    # Variable para comprobar casillas
    # avanzar_cantidad = 2
    print("Has obtenido un " + str(avanzar_cantidad) + " en el dado")

    print("Avanzas " + str(avanzar_cantidad) + " casillas")

    # Revisar. By: Sofía Molina <sofia.molina@alumnos.ucn.cl>

    for i in range(avanzar_cantidad):  #--Revisar if convirtiendolos a elif por que hay condiciones que se cumpliran dos veces y a si evitar que
        if pos_x == 0 and pos_y == 4:   #avanzara de mas pero bastante bien.
            pos_x += 1                  #Si la posicion es primera fila ultima columna baja una fila

        elif pos_x == 4 and pos_y == 4: #Lo mismo para una de las 4 esquinas en los demas if
            pos_y -= 1

        elif pos_x == 4 and pos_y == 0:
            pos_x -= 1

        elif pos_x == 0 and pos_y == 0:
            pos_y += 1

        elif pos_x == 0: #avanzando por columnas si es la primera fila avanzar hacia la derecha
            pos_y += 1

        elif pos_y == 4: #si esta en columna 5 baja uno 
            pos_x += 1

        elif pos_x == 4: #si esta en la ultima fila avanza hacia la izquierda
            pos_y -= 1

        elif pos_y == 0: #si esta en la primera columna comienza a subir 
            pos_x -= 1

    print("Has avanzado\n")
    print(f"Te encuentras en la casilla ({pos_x}, {pos_y})\n")

    simbolo_matriz = tablero[pos_x][pos_y]

    if simbolo_matriz == "🏠": #Inicio
        print("¡Estas en la casilla de inicio!\n")
        pass
        
    elif simbolo_matriz == "➡": #solo continuar
        print("Esta casilla no hace nada ¡UPS!\n")

    elif simbolo_matriz == "🧺": #Balde de globos
        cubo(turno_jugador)
        pass

    elif simbolo_matriz == "🏪": #Tienda
        if turno_jugador == 0:
            kiosco_1(turno_jugador)
        else:
            kiosco_2(turno_jugador)

    elif simbolo_matriz == "🤐":
        escondite(turno_jugador)

    
    elif simbolo_matriz == "💲":
        casilla_moneda(turno_jugador)

        pass
    
    if turno_jugador == 0:
        jugador_1_x, jugador_1_y = pos_x, pos_y 
    else:
        jugador_2_x, jugador_2_y = pos_x, pos_y
        
    mostrar_tablero()

    return (pos_x, pos_y)

    

#Turno de los jugadores 1 o 2              

#                       ¡IMPORTANTE EN ESTO SE BASA EL CAMBIANTE DE TURNOS!


def siguienteTurno(turnoJugador): 
    if turnoJugador == 0: #si el jugador al terminar el turno es 0 (Jugador01) cambiara el valor a 1 (Jugador02)
        turnoJugador += 1
    else:
        turnoJugador -= 1 #En caso contrario el valor sera 0 (si el Jugador02 termino su turno)

    return turnoJugador


    #¡IMPORTANTE! REVISAR turno_jugador y si no funciona cambiar por turnoJugador



#MENU DEL JUEGO

def menu_juego(turno_jugador,
    monedas_Jugador1, Jugador1_vidas,
    monedas_Jugador2, Jugador2_vidas,
    jugador_1_x, jugador_1_y,
    jugador_2_x, jugador_2_y):
    

    while True:
        print("\n")

        if turno_jugador == 0:
            print(ROJO +  "Jugador 1" + RESET)
        else:
            print(AZUL + "Jugador 2" + RESET)

        print(VERDE + "Que deseas hacer? / Jugador")
        print("(1) Lanzar dado")
        print("(2) Usar globo")
        print("(3) Usar objeto")
        print("(4) Ver estado\n" + RESET)

        elegir = input("Eliga una opcion: ")

        #opcion 1 
        if elegir == "1":
                        
            if turno_jugador == 0:
                jugador_1_x, jugador_1_y = avanzar(turno_jugador, tablero, jugador_1_x, jugador_1_y)
            else:
                jugador_2_x, jugador_2_y = avanzar(turno_jugador, tablero, jugador_2_x, jugador_2_y)

            turno_jugador = siguienteTurno(turno_jugador)

            return turno_jugador, jugador_1_x, jugador_1_y, jugador_2_x, jugador_2_y
            

        #opcion 2
        elif elegir == "2":

            if turno_jugador == 0 and "Globo" in inventario_J1: 
                
            #Revisar que este en el inventario y el turno sea del jugador 1
                usar_globo(turno_jugador)
                turno_jugador = siguienteTurno(turno_jugador)
                return turno_jugador, jugador_1_x, jugador_1_y , jugador_2_x, jugador_2_y
            
            elif turno_jugador == 1 and "Globo" in inventario_J2: 
                
            #Revisar que este en el inventario y el turno sea del jugador 1
                usar_globo(turno_jugador)
                turno_jugador = siguienteTurno(turno_jugador)
                return turno_jugador, jugador_1_x, jugador_1_y , jugador_2_x, jugador_2_y
            
            else: 
                print("No tienes globos ahora mismo \n")
            
            

        #opcion 3
        elif elegir == "3":
            print("\nHas elegido usar objeto\n")
            if len(inventario_J1) == 0 and turno_jugador == 0: #TURNO JUGADOR = 0 SIGNIFICA JUGADOR 1 Y EL 1 ES EL 2 PARA QUE VAYA VARIANDO
                print("No tienes ningun objeto disponible\n")
            elif len(inventario_J2) == 0 and turno_jugador == 1:
                print("No tienes ningun objeto disponible\n")
            
            else:
                print("Tienes objetos disponibles!\n")
                if turno_jugador == 0:
                    print("objetos:", inventario_J1, "\n") 

                elif turno_jugador == 1:
                    print("objetos:", inventario_J2, "\n")

            pass

        
        

        #opcion 4
        elif elegir == "4":
            print("\nHas elegido ver estado\n")
            if turno_jugador == 0:
                print("Estadisticas Jugador 01")
                print("Vidas❤:", str(Jugador1_vidas))
                print("Monedas: $" + str(monedas_Jugador1))
                print("Inventario: ", inventario_J1)
                print("Posicion", jugador_1_x, jugador_1_y, "\n")
            
            #EN CASO DE QUERER UNIR SOLO ELIMINAR LAS CONDICIONES
            elif turno_jugador == 1:
                print("Estadisticas Jugador 02")
                print("Vidas❤:", str(Jugador2_vidas))
                print("Monedas: $" + str(monedas_Jugador2))
                print("Inventario: ", inventario_J2)
                print("Posicion", jugador_2_x, jugador_2_y, "\n")

            pass

        else:
            print("Opcion Invalida, Eliga nuevamente \n")
            elegir = input("Eliga una opcion: ")



def casilla_moneda(turno_jugador):
    global monedas_Jugador1, monedas_Jugador2

    print("\nHas caido en la casilla de monedas! ")
    print("Has obtenido: $1.000\n")                 #Cambiar por la cantidad que se quiera o un random
    
    if turno_jugador == 0:
        monedas_Jugador1 += 1000
    elif turno_jugador ==1:
        monedas_Jugador2 += 1000


def kiosco_1(turno_jugador):
    inicio_tienda = time.time()

    global inventario_J1, monedas_Jugador1, Jugador1_vidas, paraguas_J1 

    if turno_jugador == 0:  # añadir al programa
        paragua_1 = 0
        globo_1 = 0

        print("\nHaz caido en la casilla ")  # agregar la posicion del jugador
        print("Bienvenido al kiosco!\n")
        opcion = input("Quieres ver los productos disponibles? (SI/NO): \n").lower()
        while True:
            if time.time() - inicio_tienda > 90:
                print("\n⏰ Tiempo agotado en la tienda")
                break
            if opcion == "si":
                print("Tu dinero actual es de: " + "$" + str(monedas_Jugador1))  # agregar 'def dinero' y si es necesario str()

                print("(1) Comprar paragua: $7000")
                print("    Una excelente opcion si quieres evitar perder")
                print("    vidas gracias al otro jugador! (USOS: 3) \n")

                print("(2) Comprar globo: $3000")
                print("    Ideal para atacar al otro jugador y tener mas chances de ganar!")
                print("    pero OJO: hay una probabilidad de que ud. reciba el ataque. (USOS: 1)\n")

                print("(3) Comprar vida extra: $6000")
                print("    Haz perdido alguna vida? Esta es una excelente opcion si quieres")
                print("    dar vuelta la partida! (USOS: 1)\n")

                print("(4) Salir del kiosco\n")

                compra = input("Escoga una opcion (1/2/3/4): ")

                if compra == "1":
                    print("\nPrecio paragua: $7000")
                    print("Solo puede comprar hasta 2 paraguas por kiosko.")
                    print("Si desea regresar al menu anterior, escriba 'SALIR \n")
                    cantidad = input("Cuantos paraguas desea comprar?: ").lower()

                    if cantidad == "salir":
                        return

                    try:
                        cantidad = int(cantidad)
                    except:
                        print("Debe ingresar un numero o 'SALIR'\n")
                        continue

                    if cantidad not in [1, 2]:
                        print("Solo puede comprar entre 1 y 2 paraguas.\n")
                        continue
                    elif cantidad in [1, 2]:
                        precio = 7000 * cantidad
                        if monedas_Jugador1 >= precio:
                            paragua_1 += cantidad
                            monedas_Jugador1 -= precio
                            paraguas_J1 = 1
                            print("Has comprado " + str(cantidad) + " paragua(s).\n")
                        else:
                            print("No tienes suficientes monedas.\n")
                            continue

                elif compra == "2":
                    print("\nPrecio globo: $3000")
                    print("Solo puede comprar hasta 5 globos por kiosko.")
                    print("Si desea regresar al menu anterior, escriba 'SALIR' \n")
                    cantidad = input("Cuantos globos desea comprar?: ").lower()
                    if cantidad == "salir":
                        return

                    try:
                        cantidad = int(cantidad)
                    except:
                        print("Debe ingresar un numero o 'SALIR'\n")
                        continue

                    if cantidad not in [1, 2, 3, 4, 5]:
                        print("Solo puede comprar entre 1 y 5 globos.\n")
                        continue
                    elif cantidad in [1, 2, 3, 4, 5]:
                        precio = 3000 * cantidad
                        if monedas_Jugador1 >= precio:
                            globo_1 += cantidad
                            monedas_Jugador1 -= precio
                            for i in range(cantidad):
                                inventario_J1.append("Globo")
                            print("Has comprado " + str(cantidad) + " globo(s).\n")
                        else:
                            print("No tienes suficientes monedas.\n")
                            continue

                elif compra == "3":
                    print("\nPrecio vida extra: $6000")
                    print("Solo puede comprar hasta 2 vidas extras por kiosko.")
                    print("Si desea regresar al menu anterior, escriba 'SALIR \n'")
                    cantidad = input("Cuantas vidas extras desea comprar?: ").lower()
                    if cantidad == "salir":
                        return

                    try:
                        cantidad = int(cantidad)
                    except:
                        print("Debe ingresar un numero o 'SALIR'\n")
                        continue

                    if cantidad not in [1, 2]:
                        print("Solo puede comprar entre 1 y 2 vidas extras.\n")
                        continue
                    elif cantidad in [1, 2]:
                        precio = 6000 * cantidad
                        if monedas_Jugador1 >= precio:
                            Jugador1_vidas += cantidad
                            monedas_Jugador1 -= precio
                            print("Has comprado " + str(cantidad) + " vida(s) extra(s).\n")
                        else:
                            print("No tienes suficientes monedas.\n")
                            continue

                elif compra == "4":
                    print("\nGracias por visitar el kiosco!\n")
                    break

            if opcion == "no":
                print("\nGracias por visitar el kiosco!\n")
                break


def kiosco_2(turno_jugador):
    inicio_tienda = time.time()

    global inventario_J2, monedas_Jugador2, Jugador2_vidas, paraguas_J2

    if turno_jugador == 1:
        paragua_2 = 0
        globo_2 = 0
        print("\nHaz caido en la casilla del kiosco")  
        print("Bienvenido al kiosco!\n")
        opcion = input("Quieres ver los productos disponibles? (SI/NO): ").lower()
        while True:
            if time.time() - inicio_tienda > 90:
                print("\n⏰ Tiempo agotado en la tienda")
                break
             
            if opcion == "si":
                print("Tu dinero actual es de: " + "$" + str(
                    monedas_Jugador2))  

                print("(1) Comprar paragua: $7000")
                print("Una excelente opcion si quieres evitar perder")
                print("vidas gracias al otro jugador! (USOS: 3)\n")

                print("(2) Comprar globo: $3000")
                print("Ideal para atacar al otro jugador y tener mas chances de ganar!")
                print("pero OJO: hay una probabilidad de que ud. reciba el ataque. (USOS: 1)\n")

                print("(3) Comprar vida extra: $6000")
                print("Haz perdido alguna vida? Esta es una excelente opcion si quieres")
                print("dar vuelta la partida! (USOS: 1)\n")

                print("(4) Salir del kiosco\n")

                compra = input("Escoga una opcion (1/2/3/4): ")

                if compra == "1":
                    print("\nPrecio paragua: $7000")
                    print("Solo puede comprar hasta 2 paraguas por kiosko.")
                    print("Si desea regresar al menu anterior, escriba 'SALIR'\n")
                    cantidad = input("Cuantos paraguas desea comprar?: ").lower()
                    if cantidad == "salir":
                        return

                    try:
                        cantidad = int(cantidad)
                    except:
                        print("Debe ingresar un numero o 'SALIR'\n")
                        continue

                    if cantidad not in (1, 2):
                        print("Solo puede comprar entre 1 y 2 paraguas.\n")
                        continue
                    elif cantidad in (1, 2):
                        precio = 7000 * cantidad
                        if monedas_Jugador2 >= precio:
                            paragua_2 += cantidad
                            monedas_Jugador2 -= precio
                            paraguas_J2 = 1
                            print("Has comprado " + str(cantidad) + " paragua(s).\n")
                        else:
                            print("No tienes suficientes monedas.\n")
                            continue

                elif compra == "2":
                    print("\nPrecio globo: $3000")
                    print("Solo puede comprar hasta 5 globos por kiosko.")
                    print("Si desea regresar al menu anterior, escriba 'SALIR'\n")

                    cantidad = input("Cuantos globos desea comprar?: ").lower()

                    if cantidad == "salir":
                        return

                    try:
                        cantidad = int(cantidad)
                    except:
                        print("Debe ingresar un numero o 'SALIR'\n")
                        continue

                    if cantidad not in (1, 2, 3, 4, 5):
                        print("Solo puede comprar entre 1 y 5 globos.\n")
                        continue

                    elif cantidad in (1, 2, 3, 4, 5):
                        precio = 3000 * cantidad

                        if monedas_Jugador2 >= precio:
                            globo_2 += cantidad
                            monedas_Jugador2 -= precio
                            for i in range(cantidad):
                                inventario_J2.append("Globo")
                            print("Has comprado " + str(cantidad) + " globo(s).\n")
                        else:
                            print("No tienes suficientes monedas.\n")
                            continue

                elif compra == "3":
                    print("\nPrecio vida extra: $6000")
                    print("Solo puede comprar hasta 2 vidas extras por kiosko.")
                    print("Si desea regresar al menu anterior, escriba 'SALIR\n'")
                    cantidad = input("Cuantas vidas extras desea comprar?: ").lower()
                    if cantidad == "salir":
                        return

                    try:
                        cantidad = int(cantidad)
                    except:
                        print("Debe ingresar un numero o 'SALIR'\n")
                        continue

                    if cantidad not in (1, 2):
                        print("Solo puede comprar entre 1 y 2 vidas extras.\n")
                        continue
                    elif cantidad in (1, 2):
                        precio = 6000 * cantidad
                        if monedas_Jugador2 >= precio:
                            Jugador2_vidas += cantidad
                            monedas_Jugador2 -= precio
                            print("Has comprado " + str(cantidad) + " vida(s) extra(s).\n")
                        else:
                            print("No tienes suficientes monedas.\n")
                            continue
                elif compra == "4":
                    print("\nGracias por visitar el kiosco!\n")
                    break

            if opcion == "no":
                print("\nGracias por visitar el kiosco!\n")
                break


# Aplicar condiciones con if sobre la cantidad de monedas para guardar en objetos
# y descontar monedas


def escondite(turno_jugador):
    global escondite_J1, escondite_J2

    print("\nTe has escondido")
    print("Actualmente no te pueden atacar\n")
    
    if turno_jugador == 0:
        escondite_J1 = 1
    elif turno_jugador == 1:
        escondite_J2 = 1

#Usar el globo

def usar_globo(turno_jugador):
    global Jugador1_vidas, Jugador2_vidas, inventario_J1, inventario_J2
    global escondite_J1, escondite_J2, paraguas_J1, paraguas_J2
    #Se usa global debido a que son variables fuera del subprograma


    if turno_jugador == 0:
        if "Globo" not in inventario_J1:
            print("\nNo tienes globos disponibles\n")
            return
    elif turno_jugador == 1:
        if "Globo" not in inventario_J2:
            print("\nNo tienes globos disponibles\n")
            return

    resultado_globo = r.choice(globos_lista)
    
    print("\n¿Estas seguro de querer usarlo? Te podria quitar una vida.. 🤔😰" )
    desconfianza_globo = input("Presione cualquier tecla para confirmar, ''NO'' para desechar: ").lower()
    
    if desconfianza_globo == "no":
        print("\nCancelaste el uso del globo\n")
        return

    if turno_jugador == 0:
        if resultado_globo == "Real":
            if escondite_J2 == 1 or paraguas_J2 == 1:
                print("\nNo puedes atacar al otro jugador en este momento\n")
                if paraguas_J2 == 1:
                    paraguas_J2 = 0
                return
            inventario_J1.remove("Globo")
            print("¡El globo era real!😮")
            print("¡Le ha explotado a tu rival! 💥 ¡le has quitado una vida!\n")
            Jugador2_vidas -= 1

        elif resultado_globo == "Falso":
            inventario_J1.remove("Globo")
            print("El globo era especial! 😨")
            print("Te ha rebotado y explotado quitandote una vida! 💥😨🤯 \n")
            Jugador1_vidas -= 1

    elif turno_jugador == 1:
        if resultado_globo == "Real":
            if escondite_J1 == 1 or paraguas_J1 == 1:
                print("\nNo puedes atacar al otro jugador en este momento\n")
                if paraguas_J1 == 1:
                    paraguas_J1 = 0
                return
            inventario_J2.remove("Globo")
            print("¡El globo era real!😮")
            print("¡Le ha explotado a tu rival! 💥 ¡le has quitado una vida!\n")
            Jugador1_vidas -= 1

        elif resultado_globo == "Falso":
            inventario_J2.remove("Globo")
            print("El globo era especial! 😨")
            print("Te ha rebotado y explotado quitandote una vida! 💥😨🤯 \n")
            Jugador2_vidas -= 1

def turno_ahora(turno_jugador):
    print("Turno del jugador", turno_jugador, "\n")




# -------------------------------------------PROGRAMA PRINCIPAL---------------------------------------

introduccion()  # llama al subprograma para pedir iniciar el juego
tiempo_total = 30 * 60  #30 minutos en segundos , tiempo limite del juego
inicio_juego = time.time()


#----------------------Ciclo while para mantener el juego en curso------------------

elegir = input("Si/No: ").lower()
if elegir == "si":
    turnos = 0 #contador de turnos 
    mostrar_tablero()

    while Jugador1_vidas >0 and Jugador2_vidas > 0 and turnos < 30 and (time.time() - inicio_juego) < tiempo_total:
    # o cualquier otra condicion para acabar el juego

        
        print("¡Comenzando el juego!")
        print("turno actual:", turno_jugador)
        inicio_turno = time.time()


        turno_jugador, jugador_1_x, jugador_1_y, jugador_2_x, jugador_2_y = menu_juego(
            turno_jugador,
            monedas_Jugador1, Jugador1_vidas,
            monedas_Jugador2, Jugador2_vidas,
            jugador_1_x, jugador_1_y,
            jugador_2_x, jugador_2_y
        )

        if time.time() - inicio_turno > 60:
            print("\n⏰ Se acabó el tiempo del turno")
            turno_jugador = siguienteTurno(turno_jugador)
            continue

        #reiniciar escondites
        if turno_jugador == 0:
            escondite_J2 = 0
        else:
            escondite_J1 = 0 

        


        turnos += 1 #aumentar el turno 

    #Al terminar el juego 

    if Jugador1_vidas <= 0:
        print("\nJugador 2 Gano la guerra!\n")
    
    elif Jugador2_vidas <= 0:
        print("\nJugador 01 Gano la guerra!\n")

    else:
        print("\nse acabaron los turnos, gano el jugador con mas cantidad de vidas\n")
    

elif elegir == "no":
    print("\nBueno.. :( ¡hasta luego!)\n")
    

else:
    print("\nEliga una opcion valida porfavor..\n")



