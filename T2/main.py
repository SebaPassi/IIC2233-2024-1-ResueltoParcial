# Archivo que se debe correr para interactuar con consola

# IMPORTS
import os
import parametros
from pathlib import Path
from copy import deepcopy
from sys import argv
from random import choice
from combatientes import Guerrero, Caballero, Mago, Paladin, MagoDeBatalla, CaballeroArcano
from ejercito import Ejercito
from items import Item
from funciones_extras import (
    menu_inicio,
    menu_tienda,
    revisar_exist_tipo_combatiente,
    combatiente_cierto_tipo,
    menu_gatos_disponibles,
    vida_actual_combatientes
)
from funciones_extras_2 import abrir_archivo_dificultad, abrir_archivo_unidades

# CÓDIGO
lista_argumentos = argv
if len(lista_argumentos) == 1:
    print("El número de argumentos escritos en consola es menor al pedido")
    print("Vuelve a introducir un input válido por favor")
    exit()

dificultad_elegida = lista_argumentos[1]

if len(lista_argumentos) == 2 and dificultad_elegida in ["facil", "intermedio", "dificil"]:

    ## INICIALIZACIÓN EJERCITOS POR RONDA SEGÚN DIFICULTAD ELEGIDA ##
    
    if dificultad_elegida == "facil":
        archivo_dif_abierto = abrir_archivo_dificultad(parametros.RUTA_FACIL, "facil.txt")
    elif dificultad_elegida == "intermedio":
        archivo_dif_abierto = abrir_archivo_dificultad(parametros.RUTA_INTERMEDIO, "intermedio.txt")
    else:
        archivo_dif_abierto = abrir_archivo_dificultad(parametros.RUTA_DIFICIL, "dificil.txt")

    enemigos_1 = archivo_dif_abierto[0]
    enemigos_2 = archivo_dif_abierto[1]
    enemigos_3 = archivo_dif_abierto[2]

    ## TÉRMINO INICIALIZACIÓN EJERCITOS POR RONDA SEGÚN DIFICULTAD ELEGIDA ##

    ## OBTENCIÓN UNIDADES / COMBATIENTES DISPONIBLES ##

    combatientes_tienda = abrir_archivo_unidades(parametros.RUTA_UNIDADES)

    tienda_guerreros = []
    tienda_caballeros = []
    tienda_magos = []

    for elemento in combatientes_tienda:
        nombre = elemento[0]
        vid_max = int(elemento[2])
        defen = int(elemento[3])
        poder = int(elemento[4])
        agil = int(elemento[5])
        resis = int(elemento[6])

        if elemento[1] == "GUE":
            tienda_guerreros.append(Guerrero(nombre, vid_max, vid_max, poder, defen, agil, resis))
        elif elemento[1] == "CAB":
            tienda_caballeros.append(Caballero(nombre, vid_max, vid_max, poder, defen, agil, resis))
        elif elemento[1] == "MAG":
            tienda_magos.append(Mago(nombre, vid_max, vid_max, poder, defen, agil, resis))

    ## TÉRMINO OBTENCIÓN UNIDADES / COMBATIENTES DISPONIBLES ##

    # Se hace una copia profunda de cada una de las variables que serán modificados a lo largo
    # del flujo
    enemigos_1_copy = deepcopy(enemigos_1)
    enemigos_2_copy = deepcopy(enemigos_2)
    enemigos_3_copy = deepcopy(enemigos_3)
    tienda_guerreros_copy = deepcopy(tienda_guerreros)
    tienda_caballeros_copy = deepcopy(tienda_caballeros)
    tienda_magos_copy = deepcopy(tienda_magos)

    ## INICIO "JUEGO" ##
    condicion = True
    ronda = 1
    ejercito_jugador = Ejercito()
    menu_inicio(ejercito_jugador.oro_disponible, ronda)
    while condicion is True:
        entrada = input()

        ## OPCIÓN TIENDA ##
        if entrada == "1":
            menu_tienda(ejercito_jugador.oro_disponible)
            condicion_2 = True
            while condicion_2 is True:
                entrada_2 = input()
                # Compra mago
                if entrada_2 == "1":
                    if ejercito_jugador.oro_disponible >= parametros.PRECIO_MAG:
                        if len(tienda_magos_copy) > 0:
                            ejercito_jugador.oro_disponible -= parametros.PRECIO_MAG
                            combat_comprado = choice(tienda_magos_copy)
                            ejercito_jugador.anadir_combatiente(combat_comprado)
                            tienda_magos_copy.remove(combat_comprado)
                            print("Has comprado un combatiente tipo mago!")
                            menu_tienda(ejercito_jugador.oro_disponible)
                        else:
                            print("No quedan combatientes tipo mago en la tienda!")
                    else:
                        print(f"No tienes el dinero disponible para realizar esta compra")
                # Compra guerrero
                elif entrada_2 == "2":
                    if ejercito_jugador.oro_disponible >= parametros.PRECIO_GUE:
                        if len(tienda_guerreros_copy) > 0:
                            ejercito_jugador.oro_disponible -= parametros.PRECIO_GUE
                            combat_comprado = choice(tienda_guerreros_copy)
                            tienda_guerreros_copy.remove(combat_comprado)
                            ejercito_jugador.anadir_combatiente(combat_comprado)
                            print("Has comprado un combatiente tipo guerrero!")
                            menu_tienda(ejercito_jugador.oro_disponible)
                        else:
                            print("No quedan combatientes tipo guerrero en la tienda!")
                    else:
                        print(f"No tienes el dinero disponible para realizar esta compra")
                # Compra Caballero
                elif entrada_2 == "3":
                    if ejercito_jugador.oro_disponible >= parametros.PRECIO_CAB:
                        if len(tienda_caballeros_copy) > 0:
                            ejercito_jugador.oro_disponible -= parametros.PRECIO_CAB
                            combat_comprado = choice(tienda_caballeros_copy)
                            tienda_caballeros_copy.remove(combat_comprado)
                            ejercito_jugador.anadir_combatiente(combat_comprado)
                            print("Has comprado un combatiente tipo caballero!")
                            menu_tienda(ejercito_jugador.oro_disponible)
                        else:
                            print("No quedan combatientes tipo caballero en la tienda!")
                    else:
                        print(f"No tienes el dinero disponible para realizar esta compra")
                # Compra armadura
                elif entrada_2 == "4":
                    if ejercito_jugador.oro_disponible >= parametros.PRECIO_ARMADURA:
                        condic_1 = revisar_exist_tipo_combatiente(ejercito_jugador, "Mago")
                        condic_2 = revisar_exist_tipo_combatiente(ejercito_jugador, "Guerrero")
                        condicion_3 = True
                        if condic_1 == True or condic_2 == True:
                            while condicion_3 is True:
                                combat_mago = combatiente_cierto_tipo(ejercito_jugador, "Mago")
                                combat_gue = combatiente_cierto_tipo(ejercito_jugador, "Guerrero")
                                combat_compat = combat_mago + combat_gue
                                menu_gatos_disponibles(combat_mago, combat_gue)
                                inputs_validos = [str(i + 1) for i in range(0, len(combat_compat))]
                                opcion_elegida = input()
                                if opcion_elegida in inputs_validos:
                                    combat_elegido = combat_compat[int(opcion_elegida) - 1]
                                    print(f"Has evolucionado a {combat_elegido.nombre}")
                                    item_comprado = Item("Armadura")
                                    combat_elegido.evolucionar(item_comprado, ejercito_jugador)
                                    condicion_3 = False
                                    ejercito_jugador.oro_disponible -= parametros.PRECIO_ARMADURA
                                    menu_tienda(ejercito_jugador.oro_disponible)
                                else:
                                    print("La opción elegida no es válida. Introduce otra opción:")

                        else:
                            print("No tienes gatos disponibles para evolucionar con una Armadura")
                    else:
                        print("No tienes el dinero disponible para realizar esta compra")

                # Compra pergamino
                elif entrada_2 == "5":
                    if ejercito_jugador.oro_disponible >= parametros.PRECIO_PERGAMINO:
                        condic_1 = revisar_exist_tipo_combatiente(ejercito_jugador, "Guerrero")
                        condic_2 = revisar_exist_tipo_combatiente(ejercito_jugador, "Caballero")
                        condicion_3 = True
                        if condic_1 == True or condic_2 == True:
                            while condicion_3 is True:
                                combat_gue = combatiente_cierto_tipo(ejercito_jugador, "Guerrero")
                                combat_cab = combatiente_cierto_tipo(ejercito_jugador, "Caballero")
                                combat_compat = combat_gue + combat_cab
                                menu_gatos_disponibles(combat_gue, combat_cab)
                                inputs_validos = [str(i + 1) for i in range(0, len(combat_compat))]
                                opcion_elegida = input()
                                if opcion_elegida in inputs_validos:
                                    combat_elegido = combat_compat[int(opcion_elegida) - 1]
                                    print(f"Has evolucionado a {combat_elegido.nombre}")
                                    item_comprado = Item("Pergamino")
                                    combat_elegido.evolucionar(item_comprado, ejercito_jugador)
                                    condicion_3 = False
                                    ejercito_jugador.oro_disponible -= parametros.PRECIO_PERGAMINO
                                    menu_tienda(ejercito_jugador.oro_disponible)
                                else:
                                    print("La opción elegida no es válida. Introduce otra opción:")
                        else:
                            print("No tienes gatos disponibles para evolucionar con un Pergamino")
                    else:
                        print("No tienes el dinero disponible para realizar esta compra")
                # Compra lanza
                elif entrada_2 == "6":
                    if ejercito_jugador.oro_disponible >= parametros.PRECIO_LANZA:
                        condic_1 = revisar_exist_tipo_combatiente(ejercito_jugador, "Mago")
                        condic_2 = revisar_exist_tipo_combatiente(ejercito_jugador, "Caballero")
                        condicion_3 = True
                        if condic_1 == True or condic_2 == True:
                            while condicion_3 is True:
                                combat_mago = combatiente_cierto_tipo(ejercito_jugador, "Mago")
                                combat_cab = combatiente_cierto_tipo(ejercito_jugador, "Caballero")
                                combat_compat = combat_mago + combat_cab
                                menu_gatos_disponibles(combat_mago, combat_cab)
                                inputs_validos = [str(i + 1) for i in range(0, len(combat_compat))]
                                opcion_elegida = input()
                                if opcion_elegida in inputs_validos:
                                    combat_elegido = combat_compat[int(opcion_elegida) - 1]
                                    print(f"Has evolucionado a {combat_elegido.nombre}")
                                    item_comprado = Item("Lanza")
                                    combat_elegido.evolucionar(item_comprado, ejercito_jugador)
                                    condicion_3 = False
                                    ejercito_jugador.oro_disponible -= parametros.PRECIO_LANZA
                                    menu_tienda(ejercito_jugador.oro_disponible)
                                else:
                                    print("La opción elegida no es válida. Introduce otra opción:")
                        else:
                            print("No tienes gatos disponibles para evolucionar con una Lanza")
                    else:
                        print("No tienes el dinero disponible para realizar esta compra")
                # Compra curación
                elif entrada_2 == "7":
                    if ejercito_jugador.oro_disponible >= parametros.PRECIO_CURA:
                        if len(ejercito_jugador.combatientes) == 0:
                            print("Aún no tienes combatientes para curar!")
                        else:
                            curar = vida_actual_combatientes(ejercito_jugador)
                            if curar == True:
                                ejercito_jugador.oro_disponible -= parametros.PRECIO_CURA
                                vida_extra = parametros.CURAR_VIDA
                                print(f"Curaste a tu ejército con {vida_extra} puntos de vida!")

                                for combatiente in ejercito_jugador.combatientes:
                                    combatiente.curarse(vida_extra)

                                menu_tienda(ejercito_jugador.oro_disponible)
                            else:
                                print("Todos tus combatientes están con vida máxima!")
                    else:
                        print("No tienes el dinero disponible para realizar esta compra")

                elif entrada_2 == "0":
                    condicion_2 = False
                    menu_inicio(ejercito_jugador.oro_disponible, ronda)
                else:
                    print("La opción elegida no es correcta. Vuelve a introducir una opción:")

        ## OPCIÓN MOSTRAR EJÉRCITO ##
        elif entrada == "2":
            print(ejercito_jugador)
            menu_inicio(ejercito_jugador.oro_disponible, ronda)

        ## OPCIÓN COMBATIR ##
        elif entrada == "3":
            if len(ejercito_jugador.combatientes) == 0:
                print("Tu ejército está vacío actualmente.")
                print("Anda a tienda y suma combatientes de tu lado!")
            else:
                # Primera ronda
                if ronda == 1:
                    resultado_combate = ejercito_jugador.combatir(enemigos_1_copy)
                    # Si gana primera ronda
                    if resultado_combate == True:
                        ronda += 1
                        ejercito_jugador.oro_disponible += parametros.ORO_GANADO
                        menu_inicio(ejercito_jugador.oro_disponible, ronda)
                    # Si pierde primera ronda
                    else:
                        print("Has perdido en primera ronda :(")
                        ejercito_jugador = Ejercito()
                        ronda = 1
                        menu_inicio(ejercito_jugador.oro_disponible, ronda)

                        enemigos_1_copy = deepcopy(enemigos_1)
                        enemigos_2_copy = deepcopy(enemigos_2)
                        enemigos_3_copy = deepcopy(enemigos_3)
                        tienda_guerreros_copy = deepcopy(tienda_guerreros)
                        tienda_caballeros_copy = deepcopy(tienda_caballeros)
                        tienda_magos_copy = deepcopy(tienda_magos)

                # Segunda ronda
                elif ronda == 2:
                    resultado_combate = ejercito_jugador.combatir(enemigos_2_copy)
                    # Si gana segunda ronda
                    if resultado_combate == True:
                        ronda += 1
                        ejercito_jugador.oro_disponible += parametros.ORO_GANADO
                        menu_inicio(ejercito_jugador.oro_disponible, ronda)
                    # Si pierde segunda ronda
                    else:
                        print("Has perdido en segunda ronda :(")
                        ejercito_jugador = Ejercito()
                        ronda = 1
                        menu_inicio(ejercito_jugador.oro_disponible, ronda)

                        enemigos_1_copy = deepcopy(enemigos_1)
                        enemigos_2_copy = deepcopy(enemigos_2)
                        enemigos_3_copy = deepcopy(enemigos_3)
                        tienda_guerreros_copy = deepcopy(tienda_guerreros)
                        tienda_caballeros_copy = deepcopy(tienda_caballeros)
                        tienda_magos_copy = deepcopy(tienda_magos)

                # Tercera ronda
                else:
                    resultado_combate = ejercito_jugador.combatir(enemigos_3_copy)
                    # Si gana tercera ronda
                    if resultado_combate == True:
                        print("Has ganado las tres rondas, por lo que te has \"pasado\" el juego.")
                        print("Felicitaciones!")
                        exit()
                    # Si pierde tercera ronda
                    else:
                        print("Has perdido en tercera ronda :(")
                        ejercito_jugador = Ejercito()
                        ronda = 1
                        menu_inicio(ejercito_jugador.oro_disponible, ronda)
                        
                        enemigos_1_copy = deepcopy(enemigos_1)
                        enemigos_2_copy = deepcopy(enemigos_2)
                        enemigos_3_copy = deepcopy(enemigos_3)
                        tienda_guerreros_copy = deepcopy(tienda_guerreros)
                        tienda_caballeros_copy = deepcopy(tienda_caballeros)
                        tienda_magos_copy = deepcopy(tienda_magos)
        
        ## OPCIÓN SALIR DEL PROGRAMA ##
        elif entrada == "0":
            print("Has salido del juego. ¡Vuelve pronto!")
            exit()

        ## OPCIÓN NO VÁLIDA ##
        else:
            print("La opción elegida no es correcta. Vuelve a introducir una opción válida:")


else:
    if len(lista_argumentos) > 2:
        print("El número de argumentos escritos en consola es mayor al pedido")
    else:
        print("La dificultad elegida no se encuentra disponible")
    print("Vuelve a introducir un input válido por favor")