# En este archivo hay funciones que consideré oportunas para modularizar mi trabajo


    # Función 1: imprime el menú de acciones completo. Recibe como argumento el nombre de la red y el
    # nombre de la estación

def imprimir_menu_acciones_completo(nombre_archivo_texto: str, estacion: str) -> None:
    print(f"¡Se cargó la red {nombre_archivo_texto}!")
    print(f"La estación elegida es: {estacion}")
    print()
    print("*** Menú de Acciones ***")
    print()
    print("[1] Mostrar red")
    print("[2] Encontrar ciclo más corto")
    print("[3] Asegurar ruta")
    print("[4] Salir del programa")
    print()
    print("Indique su opción (1, 2, 3, 4):")

    # Función 2: imprime el menú de acciones. No recibe argumentos.

def imprimir_menu_acciones() -> None:
    print("*** Menú de Acciones ***")
    print()
    print("[1] Mostrar red")
    print("[2] Encontrar ciclo más corto")
    print("[3] Asegurar ruta")
    print("[4] Salir del programa")
    print()
    print("Indique su opción (1, 2, 3, 4):")