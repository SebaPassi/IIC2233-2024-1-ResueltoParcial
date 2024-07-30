# PARTE 2 de tarea

# IMPORTS
import red
import sys
import os
from pathlib import Path
import funciones_extras
import dcciudad

# CÓDIGO
lista_argumentos = sys.argv
nombre_archivo_texto = lista_argumentos[1] + ".txt"
ruta_archivo = os.path.join("data", nombre_archivo_texto)
estacion = " ".join(lista_argumentos[2:])

    # Crear instancia de la clase Path
instancia_archivo = Path(ruta_archivo)

    # Si nombre de red existe como un archivo dentro de la carpeta "data/"
if instancia_archivo.is_file() and instancia_archivo.exists():
    # Obtener una lista con el nombre de las estaciones y una lista de listas de la red
    with open(ruta_archivo, "r", encoding = "utf-8") as f:
                lista = f.readlines()
    for i in range(0, len(lista)):
        lista[i] = lista[i].strip("\n")

    tamaño_nueva_red = int(lista[0])
    estaciones = lista[1:tamaño_nueva_red + 1]
    red_como_str = lista[tamaño_nueva_red + 1]
    lista_de_red = red_como_str.split(",")

    for i in range(0, len(lista_de_red)):
        lista_de_red[i] = int(lista_de_red[i])
    
    lista_de_listas_red = []
    i = 0
    while i < len(lista_de_red):
        fila_actual = lista_de_red[i:i + tamaño_nueva_red]
        lista_de_listas_red.append(fila_actual)
        i += tamaño_nueva_red

    parametro_red = lista_de_listas_red

    # Si estación existe en la red entregada, luego comenzar con el Menú de Acciones
    if estacion in estaciones:
        # Se imprime el menú de acciones completo
        funciones_extras.imprimir_menu_acciones_completo(nombre_archivo_texto, estacion)
        # Se crea una instancia de la clase RedMetro
        instancia_red_metro = red.RedMetro(parametro_red, estaciones)
        condicion = True

        while condicion is True:
            # Se pide una respuesta al usuario
            respuesta_usuario = input()
            # Si respuesta no es válida
            if respuesta_usuario not in "1234":
                print("Introduce una opción válida por favor:")
            
            else:
                # Si respuesta es 1
                if int(respuesta_usuario) == 1:
                    dcciudad.imprimir_red(parametro_red, estaciones)
                    funciones_extras.imprimir_menu_acciones()
                
                # Si respuesta es 2
                elif int(respuesta_usuario) == 2:
                    est_inter = instancia_red_metro.ciclo_mas_corto(estacion)
                    print()
                    print(f"El valor retornado por la función ciclo_mas_corto es: {est_inter}")
                    print()
                    funciones_extras.imprimir_menu_acciones()

                # Si respuesta es 3
                elif int(respuesta_usuario) == 3:
                    destino = input("Por favor introduce la estación de destino: ")
                    e_int = input("Por favor introduce la cantidad de estaciones intermedias: ")
                    nueva_red = instancia_red_metro.asegurar_ruta(estacion, destino, int(e_int))
                    print("La nueva red retornada por la función asegurar_ruta es:")
                    print(nueva_red)
                    funciones_extras.imprimir_menu_acciones()
                
                # Si respuesta es 4
                elif int(respuesta_usuario) == 4:
                    break


    # Si estación no existe en la red entregada
    else:
        print("La estación entregada no existe")

    # Si nombre de red NO existe como un archivo dentro de la carpeta "data/"
else:
    print("La red entregada no existe")