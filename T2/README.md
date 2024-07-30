# Tarea 2: DCCombatientes 🐈⚔️

El código es capaz de simular la experiencia de juego tal como se especifica en el enunciado y es a prueba de todo tipo de errores (ya sea en consola o de los archivos necesarios para ejecutar el programa).

### Cosas implementadas y no implementadas :white_check_mark: :x:

#### Programación Orientada a Objetos: 12 pts (10%)
##### ✅ Definición de clases, herencia y *properties*

Para el desarrollo de la tarea se utilizaron los contenidos vistos en clases tales como Herencia, Multiherencia, Clases abstractas y Properties.

#### Preparación del programa: 10 pts (8%)
##### ✅ Inicio de la partida

Al iniciarse el juego el jugador comienza con un ejército vacío de combatientes y con el dinero correspondiente al parámetro ```ORO_INICIAL``` especificado en el archivo ```parametros.py```. Además, el programa es a prueba de errores tanto en el input entregado en consola como en los archivos entregados para su funcionamiento.

#### Entidades: 56 pts (47%)
##### ✅ Ejército
Se cumple con todo lo especificado en la pauta.

##### ✅ Combatientes
Se cumple con todo lo especificado en la pauta.

##### ✅ Ítems
Se cumple con todo lo especificado en la pauta.

#### Flujo del programa: 30 pts (25%)
##### ✅ Menú de Inicio
Se cumple con todo lo especificado en la pauta.

##### ✅ Menú Tienda
Se cumple con todo lo especificado en la pauta.
##### ✅ Selección de gato
Se cumple con todo lo especificado en la pauta.
##### ✅ Fin del Juego
Se cumple con todo lo especificado en la pauta.
##### ✅ Robustez
Todos los menús implementados son a prueba de cualquier tipo de input proveniente de consola por parte del jugador.

#### Archivos: 12 pts (10%)
##### ✅ Archivos .txt
Se cumple con todo lo especificado en la pauta.
##### ✅ parametros.py
Se cumple con todo lo especificado en la pauta.


## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además, para un correcto funcionamiento del código se debe descargar ```combatientes.py```, ```ejercito.py```, ```items.py```, ```parametros.py```, ```funciones_extras.py``` y ```funciones_extras_2.py``` (todos en la carpeta Tareas/T2/).

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```os```: ```path.join()```.
2. ```pathlib```: ```Path()```.
3. ```copy```: ```deepcopy()```.
4. ```sys```: ```argv```.
5. ```random```: ```choice()```.
6. ```abc```: ```ABC```, ```abstractmethod```.

### Librerías propias
Por otro lado, creé los siguientes módulos:

1. ```funciones_extras```: este módulo contiene funciones que considere oportunas para el desarrollo del archivo ```main.py```. Contiene a: ```menu_inicio(oro, ronda)``` (imprime el menú de inicio. Recibe dos parámetros), ```menu_tienda(oro)``` (imprime el menú de la tienda. Recibe un parámetro), ```revisar_exist_tipo_combatiente(ejercito_jugador, tipo)``` (verifica si en el ejercito del jugador hay algún combatiente de cierto tipo. Recibe dos parámetros), ```combatiente_cierto_tipo(ejercito_jugador, tipo)``` (crea sublistas de los combatientes del ejército del jugador según el tipo de combatiente. Recibe dos parámetros), ```menu_gatos_disponibles(lista_1, lista_2)``` (imprime el menú de gatos disponibles para cierto ítem. Recibe dos parámetros) y ```vida_actual_combatientes(ejercito_jugador)``` (revisa la vida de los combatientes. Recibe un parámetro).

2. ```funciones_extras_2```: este módulo contiene más funciones que considere oportunas para el desarrollo del archivo ```main.py```. Contiene a: ```abrir_archivo_dificultad(ruta_archivo, nombre_archivo)``` (abre el archivo de dificultad y retorna tres listas donde cada una corresponde al ejército enemigo de la primera, segunda y tercera ronda. Además, revisa todos los posibles errores que pueden existir en dicho archivo. Recibe dos parámetros) y ```abrir_archivo_entidades(ruta_archivo_2)``` (abre el archivo de entidades y retorna una lista con los combatientes disponibles para comprar en tienda. Además, revisa todos los posibles errores que pueden existir en dicho archivo. Recibe un parámetro).

3. ```combatientes.py```: en este módulo definí las clases relacionadas con los gatos combatientes.
4. ```items.py```: en este módulo definí la clase ```Item```.
5. ```ejercito.py```: en este módulo definí la clase ```Ejercito```.
6. ```parametros.py```: en este módulo definí parámetros constantes necesarios para un correcto funcionamiendo de ```main.py```.

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Se asume que si el valor entregado por los archivos para los atributos numéricos de los combatientes son tipo ```float```, luego son inválidos. Esto fue especificado en una issue.
2. Se asume que cuando se compra un combatiente de la tienda este ya no puede volver a comprarse a lo largo del juego. El qué hacer en torno a esto quedó a libre elección del estudiante, pero creo que se acerca más a la realidad la forma en la que lo hice.
3. Se asume que el combatiente del jugador que está experimentando el juego será el que ataca primero. Si bien la disminución de la vida de los combatientes se hizo "al mismo tiempo" en el método ```combatir()``` de la clase ```Ejercito```, hay ciertos métodos ```atacar()``` que disminuyen atributos del enemigo que luego son utilizados para calcular el daño que se hará al contrincante. Luego, se asume como válido que para cierto tipo de combatientes el jugador tendrá una leve ventaja por sobre "la consola".
4. Se asume que los gatos que comienzan peleando (y los que pelearán una vez muere el combatiente de su equipo) serán los ubicados en la posición "0" de la lista que representa al ejército.
5. Se asume que el valor de los parámetros que hacen referencia a porcentajes se puede dejar en decimal (con los cambios respectivos en las fórmulas del enunciado).
6. Se asume que los gatos combatientes disponibles en tienda siempre serán extraídos del archivo con nombre ```unidades.txt```.
7. Se asume que el formato de entrega de los archivos es siempre el mismo en el de dificultad y en el de unidades (uso de ";" y ",").
8. Se asume que al ganar (ser vencedor en las tres rondas) se debe cerrar el programa notificando al jugador que ganó.