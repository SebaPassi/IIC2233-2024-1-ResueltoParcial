import dcciudad
from pathlib import Path
import os
import copy

class RedMetro:
    def __init__(self, red: list, estaciones: list) -> None:
        self.red = red
        self.estaciones = estaciones


    def informacion_red(self) -> list:
        cantidad_estaciones = len(self.estaciones)
        cantidad_tuneles_por_estacion = []
        for elemento in self.red:
            cantidad_tuneles_estacion_actual = elemento.count(1)
            cantidad_tuneles_por_estacion.append(cantidad_tuneles_estacion_actual)
        
        return [cantidad_estaciones, cantidad_tuneles_por_estacion]

    def agregar_tunel(self, inicio: str, destino: str) -> int:
        fila_estacion_inicio = self.estaciones.index(inicio)
        columna_estacion_destino = self.estaciones.index(destino)

        if self.red[fila_estacion_inicio][columna_estacion_destino] == 1:
            return -1
        else:
            self.red[fila_estacion_inicio][columna_estacion_destino] = 1
            cantidad_tuneles_salida_estacion_inicio = self.red[fila_estacion_inicio].count(1)
            return cantidad_tuneles_salida_estacion_inicio

    def tapar_tunel(self, inicio: str, destino: str) -> int:
        fila_estacion_inicio = self.estaciones.index(inicio)
        columna_estacion_destino = self.estaciones.index(destino)

        if self.red[fila_estacion_inicio][columna_estacion_destino] == 0:
            return -1
        
        else:
            self.red[fila_estacion_inicio][columna_estacion_destino] = 0
            cantidad_tuneles_salida_estacion_inicio = self.red[fila_estacion_inicio].count(1)
            return cantidad_tuneles_salida_estacion_inicio

    def invertir_tunel(self, estacion_1: str, estacion_2: str) -> bool:
        posicion_1 = self.estaciones.index(estacion_1)
        posicion_2 = self.estaciones.index(estacion_2)

        if self.red[posicion_1][posicion_2] == self.red[posicion_2][posicion_1] == 1:
            return True

        elif self.red[posicion_1][posicion_2] == 1 and self.red[posicion_2][posicion_1] == 0:
            self.red[posicion_1][posicion_2] = 0
            self.red[posicion_2][posicion_1] = 1
            return True
        
        elif self.red[posicion_1][posicion_2] == 0 and self.red[posicion_2][posicion_1] == 1:
            self.red[posicion_1][posicion_2] = 1
            self.red[posicion_2][posicion_1] = 0
            return True
        
        elif self.red[posicion_1][posicion_2] == 0 and self.red[posicion_2][posicion_1] == 0:
            return False

    def nivel_conexiones(self, inicio: str, destino: str) -> str:
        posicion_1 = self.estaciones.index(inicio)
        posicion_2 = self.estaciones.index(destino)
        condicion = dcciudad.alcanzable(self.red, posicion_1, posicion_2)
        red_elevada_2 = dcciudad.elevar_matriz(self.red, 2)
        if condicion == True:
            # Túnel directo
            if self.red[posicion_1][posicion_2] == 1:
                return "túnel directo"
            # Estación intermedia
            elif red_elevada_2[posicion_1][posicion_2] >= 1:
                return "estación intermedia"
            # Muy lejos
            else:
                return "muy lejos"
            
        else:
            return "no hay ruta"

    def rutas_posibles(self, inicio: str, destino: str, p_intermedias: int) -> int:
        posicion_1 = self.estaciones.index(inicio)
        posicion_2 = self.estaciones.index(destino)
        red_elevada_p_intermedias_mas_uno = dcciudad.elevar_matriz(self.red, p_intermedias + 1)
        rutas_intermedias = red_elevada_p_intermedias_mas_uno[posicion_1][posicion_2]

        return rutas_intermedias

    def ciclo_mas_corto(self, estacion: str) -> int:
        posicion_estacion = self.estaciones.index(estacion)
        tamaño_matriz = len(self.estaciones)
        contador = 0
        if self.red[posicion_estacion][posicion_estacion] >= 1:
            return 0
        
        for i in range(2, tamaño_matriz + 1):
            red_elevada_i = dcciudad.elevar_matriz(self.red, i)
            if red_elevada_i[posicion_estacion][posicion_estacion] >= 1:
                cantidad_estaciones_intermedias = i - 1
                contador += 1
                break
        
        if contador == 0:
            return -1
        else:
            return cantidad_estaciones_intermedias

    def estaciones_intermedias(self, inicio: str, destino: str) -> list:
        posicion_1 = self.estaciones.index(inicio)
        posicion_2 = self.estaciones.index(destino)
        red_elevada_2 = dcciudad.elevar_matriz(self.red, 2)
        # Si no hay rutas desde inicio hasta destino con una única estación intermedia
        if red_elevada_2[posicion_1][posicion_2] == 0:
            return []
        # Si si hay...
        else:
            estaciones_intermedias = []
            for i in range(0, len(self.estaciones)):
                if self.red[posicion_1][i] == 1:
                    if self.red[i][posicion_2] == 1:
                        estaciones_intermedias.append(self.estaciones[i])
            
            return estaciones_intermedias

    def estaciones_intermedias_avanzado(self, inicio: str, destino: str) -> list:
        posicion_1 = self.estaciones.index(inicio)
        posicion_2 = self.estaciones.index(destino)
        red_elevada_3 = dcciudad.elevar_matriz(self.red, 3)
        # Si no hay rutas desde inicio hasta destino con SOLO dos estaciones intermedias
        if red_elevada_3[posicion_1][posicion_2] == 0:
            return []
        # Si si hay...
        else:
            estaciones_int = []
            for i in range(0, len(self.estaciones)):
                if self.red[posicion_1][i] == 1:
                    for j in range(0, len(self.estaciones)):
                        if self.red[i][j] == 1:
                            if self.red[j][posicion_2] == 1:
                                estaciones_int.append([self.estaciones[i], self.estaciones[j]])
            
            return estaciones_int

    def cambiar_planos(self, nombre_archivo: str) -> bool:
        ruta_archivo = os.path.join("data", nombre_archivo)
        instancia_archivo = Path(ruta_archivo)

        if instancia_archivo.exists():
            with open(ruta_archivo, "r", encoding = "utf-8") as f:
                lista = f.readlines()
            for i in range(0, len(lista)):
                lista[i] = lista[i].strip("\n")

            tamaño_nueva_red = int(lista[0])
            self.estaciones = lista[1:tamaño_nueva_red + 1]
            red = lista[tamaño_nueva_red + 1]
            lista_de_red = red.split(",")

            for i in range(0, len(lista_de_red)):
                lista_de_red[i] = int(lista_de_red[i])
            
            lista_de_listas_de_red = []
            i = 0
            while i < len(lista_de_red):
                fila_actual = lista_de_red[i:i + tamaño_nueva_red]
                lista_de_listas_de_red.append(fila_actual)
                i += tamaño_nueva_red

            self.red = lista_de_listas_de_red

            return True

        else:
            return False

    def asegurar_ruta(self, inicio: str, destino: str, p_intermedias: int) -> list:
        # Encontrar posición de inicio y posición de destino
        posicion_1 = self.estaciones.index(inicio)
        posicion_2 = self.estaciones.index(destino)
        cantidad_estaciones = len(self.estaciones)
        existencia_de_ruta = self.rutas_posibles(inicio, destino, p_intermedias)
        # Se realiza una "copia profunda" de la matriz original (al ser lista de listas,
        # es necesario utilizar la función deepcopy() de la librería Copy).
        copia_red = copy.deepcopy(self.red)
        # Si no existe una solución con p_intermedias estaciones desde inicio hasta destino
        if existencia_de_ruta == 0:
            return []
        # Caso directo, es decir, un único túnel (A -> B).
        elif p_intermedias == 0 and existencia_de_ruta != 0:
            return copia_red
        else:
            # Matriz entregada ya es la solución: se verifica la NO existencia de rutas más cortas.
            contador = 0
            for i in range(0, p_intermedias):
                existencia_de_ruta = self.rutas_posibles(inicio, destino, i)
                if existencia_de_ruta != 0:
                    contador += 1
            # Si ruta más corta es la con p_intermedias 
            if contador == 0:
                return copia_red
            
            # Matriz entregada NO es la solución
            else:
                # Buscar los "1" en matriz
                for i in range(0, cantidad_estaciones):
                    for j in range(0, cantidad_estaciones):
                        if copia_red[i][j] == 1:
                            # Se convierte "1" encontrado en "0"
                            copia_red[i][j] = 0
                            # Revisar si ruta con p_intermedias sigue existiendo
                            matriz_elevada = dcciudad.elevar_matriz(copia_red, p_intermedias + 1)
                            # En caso de que no exista ruta (debido al cambio), se devuelve el "1"
                            if matriz_elevada[posicion_1][posicion_2] == 0:
                                copia_red[i][j] = 1
                
                # Verificación si matriz modificada tiene como ruta más corta la con p_intermedias
                contador2 = 0
                for i in range(1, p_intermedias + 1):
                    matriz_elevada = dcciudad.elevar_matriz(copia_red, i)
                    if matriz_elevada[posicion_1][posicion_2] != 0:
                        contador2 += 1

                # Si matriz modificada tiene como ruta más corta la con p_intermedias
                if contador2 == 0:
                    return copia_red

                # Si matriz modificada sigue teniendo alguna ruta más corta (con menos de 
                # p_intermedias estaciones) y es imposible eliminarla sin eliminar a su vez 
                # la ruta con p_intermedias (CASO NO SOLUCIÓN, SE ENTREGA LISTA VACÍA).
                else:
                    return []