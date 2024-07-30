# Archivo donde se definen más funciones útiles para "main.py"

# IMPORTS
from combatientes import Guerrero, Caballero, Mago, Paladin, MagoDeBatalla, CaballeroArcano
from parametros import (
    VIDA_MAX,
    VIDA_MIN,
    PODER_MAX,
    PODER_MIN,
    DEFEN_MAX,
    DEFEN_MIN,
    AGIL_MAX,
    AGIL_MIN,
    RESIS_MAX,
    RESIS_MIN
)
# Abrir archivo dificultad
def abrir_archivo_dificultad(ruta_archivo, nombre_archivo):

    with open(ruta_archivo, "r", encoding = "utf-8") as f:
        lista = f.readlines()
    for i in range(0, len(lista)):
        lista[i] = lista[i].strip("\n").split(";")

    # Se revisa si archivo entregado tiene menos o más ejercitos que rondas
    if len(lista) != 3:
        print(f"El archivo {nombre_archivo} entregado no es válido")
        exit()

    ejercito_1 = lista[0]
    ejercito_2 = lista[1]
    ejercito_3 = lista[2]
    list_ejer_1 = []
    list_ejer_2 = []
    list_ejer_3 = []

    for i in range(0, len(ejercito_1)):
        list_ejer_1.append(ejercito_1[i].split(","))

    for i in range(0, len(ejercito_2)):
        list_ejer_2.append(ejercito_2[i].split(","))

    for i in range(0, len(ejercito_3)):
        list_ejer_3.append(ejercito_3[i].split(","))

    # Se revisa que tenga el número correcto de argumentos
    for i in range(0, len(list_ejer_1)):
        if len(list_ejer_1[i]) != 7:
            print(f"El archivo {nombre_archivo} entregado no es válido")
            exit()
    
    for i in range(0, len(list_ejer_2)):
        if (len(list_ejer_2[i])) != 7:
            print(f"El archivo {nombre_archivo} entregado no es válido")
            exit()

    for i in range(0, len(list_ejer_3)):
        if (len(list_ejer_3[i])) != 7:
            print(f"El archivo {nombre_archivo} entregado no es válido")
            exit()

    # Se revisa que los argumentos estén dentro de los intervalos válidos para cada atributo
    validez_parametros = True
    combat_val = [
        "CAB",
        "MAG",
        "GUE",
        "PAL",
        "CAR",
        "MDB"
    ]
    for i in range(0, len(list_ejer_1)):
        # Nombre no tiene restricciones
        # Tipo de combatiente debe ser válido
        if list_ejer_1[i][1] not in combat_val:
            validez_parametros = False
        
        # Vida máxima debe ser un int y estar dentro del rango permitido
        if not (list_ejer_1[i][2].isdigit() and "." not in list_ejer_1[i][2]):
            validez_parametros = False
        else:
            if int(list_ejer_1[i][2]) < VIDA_MIN or int(list_ejer_1[i][2]) > VIDA_MAX:
                validez_parametros = False

        # Defensa debe ser un int y estar dentro del rango permitido
        if not (list_ejer_1[i][3].isdigit() and "." not in list_ejer_1[i][3]):
            validez_parametros = False
        else:
            if int(list_ejer_1[i][3]) < DEFEN_MIN or int(list_ejer_1[i][3]) > DEFEN_MAX:
                validez_parametros = False

        # Poder debe ser un int y estar dentro del rango permitido
        if not (list_ejer_1[i][4].isdigit() and "." not in list_ejer_1[i][4]):
            validez_parametros = False
        else:
            if int(list_ejer_1[i][4]) < PODER_MIN or int(list_ejer_1[i][4]) > PODER_MAX:
                validez_parametros = False

        # Agilidad debe ser un int y estar dentro del rango permitido
        if not (list_ejer_1[i][5].isdigit() and "." not in list_ejer_1[i][5]):
            validez_parametros = False
        else:
            if int(list_ejer_1[i][5]) < AGIL_MIN or int(list_ejer_1[i][5]) > AGIL_MAX:
                validez_parametros = False

        # Resistencia debe ser un int y estar dentro del rango permitido
        if not (list_ejer_1[i][6].isdigit() and "." not in list_ejer_1[i][6]):
            validez_parametros = False
        else:
            if int(list_ejer_1[i][6]) < RESIS_MIN or int(list_ejer_1[i][6]) > RESIS_MAX:
                validez_parametros = False

    for i in range(0, len(list_ejer_2)):
        # Nombre no tiene restricciones
        # Tipo de combatiente debe ser válido
        if list_ejer_2[i][1] not in combat_val:
            validez_parametros = False
        
        # Vida máxima debe ser un int y estar dentro del rango permitido
        if not (list_ejer_2[i][2].isdigit() and "." not in list_ejer_2[i][2]):
            validez_parametros = False
        else:
            if int(list_ejer_2[i][2]) < VIDA_MIN or int(list_ejer_2[i][2]) > VIDA_MAX:
                validez_parametros = False

        # Defensa debe ser un int y estar dentro del rango permitido
        if not (list_ejer_2[i][3].isdigit() and "." not in list_ejer_2[i][3]):
            validez_parametros = False
        else:
            if int(list_ejer_2[i][3]) < DEFEN_MIN or int(list_ejer_2[i][3]) > DEFEN_MAX:
                validez_parametros = False

        # Poder debe ser un int y estar dentro del rango permitido
        if not (list_ejer_2[i][4].isdigit() and "." not in list_ejer_2[i][4]):
            validez_parametros = False
        else:
            if int(list_ejer_2[i][4]) < PODER_MIN or int(list_ejer_2[i][4]) > PODER_MAX:
                validez_parametros = False

        # Agilidad debe ser un int y estar dentro del rango permitido
        if not (list_ejer_2[i][5].isdigit() and "." not in list_ejer_2[i][5]):
            validez_parametros = False
        else:
            if int(list_ejer_2[i][5]) < AGIL_MIN or int(list_ejer_2[i][5]) > AGIL_MAX:
                validez_parametros = False

        # Resistencia debe ser un int y estar dentro del rango permitido
        if not (list_ejer_2[i][6].isdigit() and "." not in list_ejer_2[i][6]):
            validez_parametros = False
        else:
            if int(list_ejer_2[i][6]) < RESIS_MIN or int(list_ejer_2[i][6]) > RESIS_MAX:
                validez_parametros = False
    
    for i in range(0, len(list_ejer_3)):
        # Nombre no tiene restricciones
        # Tipo de combatiente debe ser válido
        if list_ejer_3[i][1] not in combat_val:
            validez_parametros = False
        
        # Vida máxima debe ser un int y estar dentro del rango permitido
        if not (list_ejer_3[i][2].isdigit() and "." not in list_ejer_3[i][2]):
            validez_parametros = False
        else:
            if int(list_ejer_3[i][2]) < VIDA_MIN or int(list_ejer_3[i][2]) > VIDA_MAX:
                validez_parametros = False

        # Defensa debe ser un int y estar dentro del rango permitido
        if not (list_ejer_3[i][3].isdigit() and "." not in list_ejer_3[i][3]):
            validez_parametros = False
        else:
            if int(list_ejer_3[i][3]) < DEFEN_MIN or int(list_ejer_3[i][3]) > DEFEN_MAX:
                validez_parametros = False

        # Poder debe ser un int y estar dentro del rango permitido
        if not (list_ejer_3[i][4].isdigit() and "." not in list_ejer_3[i][4]):
            validez_parametros = False
        else:
            if int(list_ejer_3[i][4]) < PODER_MIN or int(list_ejer_3[i][4]) > PODER_MAX:
                validez_parametros = False

        # Agilidad debe ser un int y estar dentro del rango permitido
        if not (list_ejer_3[i][5].isdigit() and "." not in list_ejer_3[i][5]):
            validez_parametros = False
        else:
            if int(list_ejer_3[i][5]) < AGIL_MIN or int(list_ejer_3[i][5]) > AGIL_MAX:
                validez_parametros = False

        # Resistencia debe ser un int y estar dentro del rango permitido
        if not (list_ejer_3[i][6].isdigit() and "." not in list_ejer_3[i][6]):
            validez_parametros = False
        else:
            if int(list_ejer_3[i][6]) < RESIS_MIN or int(list_ejer_3[i][6]) > RESIS_MAX:
                validez_parametros = False

    if validez_parametros == False:
        print(f"Los argumentos entregados en archivo {nombre_archivo} no son válidos")
        exit()
    
    enemigos_1 = []
    enemigos_2 = []
    enemigos_3 = []

    # EJERCITO RONDA 1 #
    for elemento in list_ejer_1:
        nombre = elemento[0]
        vid_max = int(elemento[2])
        defen = int(elemento[3])
        poder = int(elemento[4])
        agil = int(elemento[5])
        resis = int(elemento[6])

        if elemento[1] == "GUE":
            enemigos_1.append(Guerrero(nombre, vid_max, vid_max, poder, defen, agil, resis))
        elif elemento[1] == "CAB":
            enemigos_1.append(Caballero(nombre, vid_max, vid_max, poder, defen, agil, resis))
        elif elemento[1] == "MAG":
            enemigos_1.append(Mago(nombre, vid_max, vid_max, poder, defen, agil, resis))
        elif elemento[1] == "PAL":
            enemigos_1.append(Paladin(nombre, vid_max, vid_max, poder, defen, agil, resis))
        elif elemento[1] == "MDB":
            enemigos_1.append(MagoDeBatalla(nombre, vid_max, vid_max, poder, defen, agil, resis))
        else:
            enemigos_1.append(CaballeroArcano(nombre, vid_max, vid_max, poder, defen, agil, resis))

    # EJERCITO RONDA 2 #
    for elemento in list_ejer_2:
        nombre = elemento[0]
        vid_max = int(elemento[2])
        defen = int(elemento[3])
        poder = int(elemento[4])
        agil = int(elemento[5])
        resis = int(elemento[6])

        if elemento[1] == "GUE":
            enemigos_2.append(Guerrero(nombre, vid_max, vid_max, poder, defen, agil, resis))
        elif elemento[1] == "CAB":
            enemigos_2.append(Caballero(nombre, vid_max, vid_max, poder, defen, agil, resis))
        elif elemento[1] == "MAG":
            enemigos_2.append(Mago(nombre, vid_max, vid_max, poder, defen, agil, resis))
        elif elemento[1] == "PAL":
            enemigos_2.append(Paladin(nombre, vid_max, vid_max, poder, defen, agil, resis))
        elif elemento[1] == "MDB":
            enemigos_2.append(MagoDeBatalla(nombre, vid_max, vid_max, poder, defen, agil, resis))
        else:
            enemigos_2.append(CaballeroArcano(nombre, vid_max, vid_max, poder, defen, agil, resis))

    # EJERCITO RONDA 3 #
    for elemento in list_ejer_3:
        nombre = elemento[0]
        vid_max = int(elemento[2])
        defen = int(elemento[3])
        poder = int(elemento[4])
        agil = int(elemento[5])
        resis = int(elemento[6])

        if elemento[1] == "GUE":
            enemigos_3.append(Guerrero(nombre, vid_max, vid_max, poder, defen, agil, resis))
        elif elemento[1] == "CAB":
            enemigos_3.append(Caballero(nombre, vid_max, vid_max, poder, defen, agil, resis))
        elif elemento[1] == "MAG":
            enemigos_3.append(Mago(nombre, vid_max, vid_max, poder, defen, agil, resis))
        elif elemento[1] == "PAL":
            enemigos_3.append(Paladin(nombre, vid_max, vid_max, poder, defen, agil, resis))
        elif elemento[1] == "MDB":
            enemigos_3.append(MagoDeBatalla(nombre, vid_max, vid_max, poder, defen, agil, resis))
        else:
            enemigos_3.append(CaballeroArcano(nombre, vid_max, vid_max, poder, defen, agil, resis))

    return enemigos_1, enemigos_2, enemigos_3

# Abrir archivo unidades
def abrir_archivo_unidades(ruta_archivo_2):
    with open(ruta_archivo_2, "r", encoding = "utf-8") as f:
        combatientes_tienda = f.readlines()

    for i in range(0, len(combatientes_tienda)):
        combatientes_tienda[i] = combatientes_tienda[i].strip("\n").split(",")

    # Se revisa que tenga el número correcto de argumentos
    for elemento in combatientes_tienda:
        if len(elemento) != 7:
            print("El archivo \"unidades.txt\" entregado no es válido")
            exit()

    # Se revisa que los argumentos estén dentro de los intervalos válidos para cada atributo
    validez_parametros = True
    combat_val = [
        "CAB",
        "MAG",
        "GUE"
    ]
    for i in range(0, len(combatientes_tienda)):
        # Nombre no tiene restricciones
        # Tipo de combatiente debe ser válido
        if combatientes_tienda[i][1] not in combat_val:
            validez_parametros = False
        # Vida máxima debe ser un int y estar dentro del rango permitido
        if not (combatientes_tienda[i][2].isdigit() and "." not in combatientes_tienda[i][2]):
            validez_parametros = False
        else:
            if int(combatientes_tienda[i][2]) < VIDA_MIN or \
               int(combatientes_tienda[i][2]) > VIDA_MAX:
                validez_parametros = False
        # Defensa debe ser un int y estar dentro del rango permitido
        if not (combatientes_tienda[i][3].isdigit() and "." not in combatientes_tienda[i][3]):
            validez_parametros = False
        else:
            if int(combatientes_tienda[i][3]) < DEFEN_MIN or \
               int(combatientes_tienda[i][3]) > DEFEN_MAX:
                validez_parametros = False
        # Poder debe ser un int y estar dentro del rango permitido
        if not (combatientes_tienda[i][4].isdigit() and "." not in combatientes_tienda[i][4]):
            validez_parametros = False
        else:
            if int(combatientes_tienda[i][4]) < PODER_MIN or \
               int(combatientes_tienda[i][4]) > PODER_MAX:
                validez_parametros = False
        # Agilidad debe ser un int y estar dentro del rango permitido
        if not (combatientes_tienda[i][5].isdigit() and "." not in combatientes_tienda[i][5]):
            validez_parametros = False
        else:
            if int(combatientes_tienda[i][5]) < AGIL_MIN or \
               int(combatientes_tienda[i][5]) > AGIL_MAX:
                validez_parametros = False
        # Resistencia debe ser un int y estar dentro del rango permitido
        if not (combatientes_tienda[i][6].isdigit() and "." not in combatientes_tienda[i][6]):
            validez_parametros = False
        else:
            if int(combatientes_tienda[i][6]) < RESIS_MIN or \
               int(combatientes_tienda[i][6]) > RESIS_MAX:
                validez_parametros = False

    if validez_parametros == False:
        print(f"Los argumentos entregados en archivo \"unidades.txt\" no son válidos")
        exit()

    return combatientes_tienda