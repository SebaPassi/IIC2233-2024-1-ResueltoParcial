import red

conexiones = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]
estaciones = ["A", "B", "C"]

red = red.RedMetro(conexiones, estaciones)
resultado_estudiante = red.asegurar_ruta("A", "C", 1)
print(resultado_estudiante)