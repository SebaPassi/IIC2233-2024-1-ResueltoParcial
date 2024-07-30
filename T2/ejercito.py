# Archivo donde se definen las clases de la entidad Ejército

# IMPORTS
import parametros

# CÓDIGO

    ## 4.1 EJÉRCITO ##
class Ejercito:

    def __init__(self):
        self.combatientes = []
        self.oro_disponible = parametros.ORO_INICIAL

    # Una ejecución de este método simula el combate de una única ronda (de tres posibles)
    def combatir(self, ejercito_enemigo):
        gano_jugador = False

        # Comienza ronda
        while (len(self.combatientes) != 0) and (len(ejercito_enemigo) != 0):

            combatiente_jugador = self.combatientes[0]
            combatiente_enemigo = ejercito_enemigo[0]

            # Ataque entre combatiente_jugador y combatiente_enemigo
            while (combatiente_jugador.vida != 0) and (combatiente_enemigo.vida != 0):
                dano_1 = combatiente_jugador.atacar(combatiente_enemigo)
                dano_2 = combatiente_enemigo.atacar(combatiente_jugador)

                combatiente_enemigo.vida -= dano_1
                combatiente_jugador.vida -= dano_2

            # Después de atacar, se "popea" aquel combatiente muerto
            if combatiente_jugador.vida == 0:
                self.combatientes.pop(0)
            if combatiente_enemigo.vida == 0:
                ejercito_enemigo.pop(0)

        # Si ganó ejército del jugador se "avisa" que fue victorioso 
        # (aplica para victoria y para empate).
        if len(ejercito_enemigo) == 0:
            gano_jugador = True
            return gano_jugador
        
        # Si jugador perdió, se "avisa" que fue derrotado.
        elif (len(ejercito_enemigo) != 0) and (len(self.combatientes) == 0):
            return gano_jugador

    # Método para añadir combatientes al ejército
    def anadir_combatiente(self, combatiente) -> None:
        self.combatientes.append(combatiente)

    # Método presentarse
    def __str__(self):
        texto_1 = "*** Este es tu Ejército Actual ***\n"
        texto_2 = "\n"
        texto_3 = ""
        for combatiente in self.combatientes:
            texto_3 = texto_3 + str(combatiente) + "\n"
        texto_4 = "\n"
        texto_5 = f"Te quedan {len(self.combatientes)} combatientes. ¡Éxito, Guerrero!"
        return texto_1 + texto_2 + texto_3 + texto_4 + texto_5