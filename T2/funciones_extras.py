# Archivo donde se definen funciones útiles para "main.py"

# IMPORTS
from combatientes import Guerrero, Caballero, Mago, Paladin, MagoDeBatalla, CaballeroArcano

# Imprime menú de inicio
def menu_inicio(oro, ronda) -> None:
    print("*** Menú de inicio ***")
    print()
    print(f"Dinero disponible: {oro}")
    print(f"Ronda actual: {ronda}")
    print()
    print("[1] Tienda")
    print("[2] Ejercito")
    print("[3] Combatir")
    print()
    print("[0] Salir del programa")
    print()
    print("Indique su opción:")

# Imprime menú de tienda
def menu_tienda(oro) -> None:
    print("*** Tienda ***")
    print()
    print(f"Dinero disponible: {oro}")
    print()
    print("       Producto          Precio")
    print("[1] Gato Mago             10")
    print("[2] Gato Guerrero         10")
    print("[3] Gato Caballero        10")
    print("[4] Ítem Armadura          5")
    print("[5] Ítem Pergamino         5")
    print("[6] Ítem Lanza             5")
    print("[7] Curar ejercito         7")
    print()
    print("[0] Volver al Menú de inicio")
    print()
    print("Indique su opción:")

# Verifica si en ejercito de jugador hay algún combatiente de cierto tipo
def revisar_exist_tipo_combatiente(ejercito_jugador, tipo):
    condicion = False
    for elemento in ejercito_jugador.combatientes:
        if elemento.tipo == tipo:
            condicion = True
    
    return condicion

# Crear sublistas de los combatientes del ejército del jugador según el tipo de combatiente
def combatiente_cierto_tipo(ejercito_jugador, tipo):
    combatientes_tipo = []
    for elemento in ejercito_jugador.combatientes:
        if elemento.tipo == tipo:
            combatientes_tipo.append(elemento)

    return combatientes_tipo

# Imprimir menú de gatos disponibles para cierto ítem
def menu_gatos_disponibles(lista_1, lista_2) -> None:
    print("*** Selecciona un gato ***")
    print()
    print("       Clase         Nombre")
    lista_total = lista_1 + lista_2
    for i in range(len(lista_total)):
        if lista_total[i].tipo == "Mago":
            print(f"[{i + 1}] Gato {lista_total[i].tipo}       {lista_total[i].nombre}")
        elif lista_total[i].tipo == "Guerrero":
            print(f"[{i + 1}] Gato {lista_total[i].tipo}   {lista_total[i].nombre}")
        else:
            print(f"[{i + 1}] Gato {lista_total[i].tipo}  {lista_total[i].nombre}")

    print()
    print("Indique su opción:")

# Revisar vida de los combatientes
def vida_actual_combatientes(ejercito_jugador):
    condicion = False
    for elemento in ejercito_jugador.combatientes:
        if elemento.vida < elemento.vida_max:
            condicion = True

    return condicion