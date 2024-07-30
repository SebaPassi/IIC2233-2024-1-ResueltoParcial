# Tarea 1: DCCiudad 🚈🐈

## Consideraciones generales :octocat:

1. Todas las funciones de ```red.py``` funcionan correctamente (pasaron todos los test cases públicos).

### Cosas implementadas y no implementadas :white_check_mark: :x:

#### Menú: 13 pts (21,7%)
##### ✅ Consola
La interacción entre usuario - consola funciona correctamente y es a prueba de errores.
##### ✅ Menú de Acciones
Mi tarea cumple con todo lo solicitado para el menú de acciones.
##### ✅ Modularización
Ningún archivo .py presente en mi tarea excede las 400 líneas de código. Además, creé ```funciones_extras.py``` para modularizar mi trabajo.
##### ✅ PEP8
Mi tarea cumple con las reglas de ```PEP8```.


## Ejecución :computer:
Los módulos principales de la tarea a ejecutar son "red.py" y "main.py". Además, para un correcto funcionamiento del código se debe descargar ```funciones_extras.py```. Todos estos archivos se encuentran en la carpeta T1 de mi respositorio personal.


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```dcciudad```: ```imprimir_red(red, estaciones)```, ```elevar_matriz(red, exponente)```, ```alcanzable(red, inicio, destino)```.
2. ```os```: ```path.join()```.
3. ```pathlib```: ```Path()```, ```exists()```, ```is_file()``` (dos últimos son métodos de una instancia de la clase Path()).
4. ```sys```: ```argv```.
5. ```red```: todas las funciones contenidas en "red.py" (importé este módulo para la elabotación de "main.py").
6. ```copy```: ```deepcopy()```.
### Librerías propias
Por otro lado, creé el siguiente módulo:

1. ```funciones_extras```: este módulo contiene funciones que considere oportunas para el desarrollo del archivo "main.py". Contiene a: ```imprimir_menu_acciones_completo(nombre_archivo_texto, estacion)``` (imprime el menú de acciones completo. Recibe dos parámetros) y a ```imprimir_menu_acciones()``` (imprime el menú de acciones sin primeras dos líneas. No recibe parámetros).

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Asumí que para la entrega del texto a la hora de ejecutar ```main.py```, el nombre del archivo irá sin el ".txt" final. Es decir, que el formato será SIEMPRE ```python3.11 main.py plano_1 cobreloa``` (o similares) y no ```python3.11 main.py plano_1.txt cobreloa``` (o similares).
2. Asumí que luego de que el usuario elija una opción en el menú (a excepción de la opción 4), se debía imprimir el menú nuevamente (pero SIN las primeras dos líneas en donde se menciona la red cargada y la estación elegida).

-------

## Referencias de código externo :books:

Para entender cómo se utilizaba ```sys.argv``` vi el siguiente video publicado en YouTube:
1. \<https://www.youtube.com/watch?v=ZQ9JO0e9468>: utilicé la información de este video para la elaboración de "main.py" (línea 12).