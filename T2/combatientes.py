# Archivo donde se definen las clases de la entidad Combatiente

# IMPORTS
from abc import ABC, abstractmethod
from random import random
import parametros

# CÓDIGO

    ## 4.2 COMBATIENTES ##
class Combatiente(ABC):

    def __init__(self, nombre, vida_max, vida, poder, defensa, agilidad, 
                 resistencia, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nombre = nombre
        self.vida_max = vida_max
        self.__vida = vida
        self.__poder = poder
        self.__defensa = defensa
        self.__agilidad = agilidad
        self.__resistencia = resistencia
        self.ataque = round((self.__poder + self.__agilidad + self.__resistencia) * \
                            ((2 * self.__vida) / self.vida_max))

    # Se define la property para la vida del combatiente (getter y setter)
    @property
    def vida(self):
        return self.__vida
    
    @vida.setter
    def vida(self, valor):
        if valor < parametros.VIDA_MIN:
            self.__vida = parametros.VIDA_MIN
        elif valor > self.vida_max:
            self.__vida = self.vida_max
        else:
            self.__vida = round(valor)

    # Se define la property para el poder del combatiente (getter y setter)
    @property
    def poder(self):
        return self.__poder
    
    @poder.setter
    def poder(self, valor):
        if valor < parametros.PODER_MIN:
            self.__poder = parametros.PODER_MIN
        elif valor > parametros.PODER_MAX:
            self.__poder = parametros.PODER_MAX
        else:
            self.__poder = round(valor)

    # Se define la property para la defensa del combatiente (getter y setter)
    @property
    def defensa(self):
        return self.__defensa
    
    @defensa.setter
    def defensa(self, valor):
        if valor < parametros.DEFEN_MIN:
            self.__defensa = parametros.DEFEN_MIN
        elif valor > parametros.DEFEN_MAX:
            self.__defensa = parametros.DEFEN_MAX
        else:
            self.__defensa = round(valor)

    # Se define la property para la agilidad del combatiente (getter y setter)
    @property
    def agilidad(self):
        return self.__agilidad
    
    @agilidad.setter
    def agilidad(self, valor):
        if valor < parametros.AGIL_MIN:
            self.__agilidad = parametros.AGIL_MIN
        elif valor > parametros.AGIL_MAX:
            self.__agilidad = parametros.AGIL_MAX
        else:
            self.__agilidad = round(valor)

    # Se define la property para la resistencia del combatiente (getter y setter)
    @property
    def resistencia(self):
        return self.__resistencia
    
    @resistencia.setter
    def resistencia(self, valor):
        if valor < parametros.RESIS_MIN:
            self.__resistencia = parametros.RESIS_MIN
        elif valor > parametros.RESIS_MAX:
            self.__resistencia = parametros.RESIS_MAX
        else:
            self.__resistencia = round(valor)

    # Método abstracto atacar
    @abstractmethod
    def atacar(self, enemigo):
        pass

    # Método abstracto curarse
    @abstractmethod
    def curarse(self, valor):
        self.vida += valor

    # Método abstracto evolucionar
    @abstractmethod
    def evolucionar(self):
        pass

    # Método abstracto presentarse
    @abstractmethod
    def __str__(self):
        pass

    # Guerrero
class Guerrero(Combatiente):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.tipo = "Guerrero"

    def atacar(self, enemigo):
        dano = round(self.ataque - enemigo.defensa)
        self.agilidad = self.agilidad * (1 - parametros.CANSANCIO)
        
        if dano < parametros.DANO_MIN:
            return parametros.DANO_MIN
        else:
            return dano

    def curarse(self, valor):
        super().curarse(valor)

    def evolucionar(self, item, ejercito_jugador):
        nombre = self.nombre
        vida_max = self.vida_max
        vida = self.vida
        poder = self.poder
        defensa = self.defensa
        agil = self.agilidad
        resis = self.resistencia

        # Si el item es un pergamino, entonces evoluciona en un MagodeBatalla
        if item.nombre == "Pergamino":
            ejercito_jugador.combatientes.remove(self)
            combat_evolu = MagoDeBatalla(nombre, vida_max, vida, poder, defensa, agil, resis)
            ejercito_jugador.combatientes.append(combat_evolu)

        # Si el item es una aramadura, entonces evoluciona en un Paladín
        elif item.nombre == "Armadura":
            ejercito_jugador.combatientes.remove(self)
            combat_evolu = Paladin(nombre, vida_max, vida, poder, defensa, agil, resis)
            ejercito_jugador.combatientes.append(combat_evolu)

    def __str__(self):
        texto_1 = f"¡Hola! Soy {self.nombre}, un Gato {self.tipo} con {self.vida} / {self.vida_max}"
        texto_2 = f" de vida, {self.ataque} de ataque y {self.defensa} de defensa."
        return texto_1 + texto_2
    

    # Caballero
class Caballero(Combatiente):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.tipo = "Caballero"

    def atacar(self, enemigo):
        prob = random()
        # Si sorprende al rival
        if prob <= parametros.PROB_CAB:
            enemigo.poder = enemigo.poder * (1 - parametros.RED_CAB)
            dano = round((self.ataque * parametros.ATQ_CAB) - enemigo.defensa)
            self.resistencia = self.resistencia * (1 - parametros.CANSANCIO)
            if dano < parametros.DANO_MIN:
                return parametros.DANO_MIN
            else:
                return dano
        
        # Si no sorprende al rival
        else:
            dano = round(self.ataque - enemigo.defensa)
            self.resistencia = self.resistencia * (1 - parametros.CANSANCIO)
            if dano < parametros.DANO_MIN:
                return parametros.DANO_MIN
            else:
                return dano

    def curarse(self, valor):
        super().curarse(valor)

    def evolucionar(self, item, ejercito_jugador):
        nombre = self.nombre
        vida_max = self.vida_max
        vida = self.vida
        poder = self.poder
        defensa = self.defensa
        agil = self.agilidad
        resis = self.resistencia

        # Si el item es una pergamino, entonces evoluciona en un CaballeroArcano
        if item.nombre == "Pergamino":
            ejercito_jugador.combatientes.remove(self)
            combat_evolu = CaballeroArcano(nombre, vida_max, vida, poder, defensa, agil, resis)
            ejercito_jugador.combatientes.append(combat_evolu)

        # Si el item es una lanza, entonces evoluciona en un Paladín
        elif item.nombre == "Lanza":
            ejercito_jugador.combatientes.remove(self)
            combat_evolu = Paladin(nombre, vida_max, vida, poder, defensa, agil, resis)
            ejercito_jugador.combatientes.append(combat_evolu)

    def __str__(self):
        texto_1 = f"¡Hola! Soy {self.nombre}, un Gato {self.tipo} con {self.vida} / {self.vida_max}"
        texto_2 = f" de vida, {self.ataque} de ataque y {self.defensa} de defensa."
        return texto_1 + texto_2


    # Mago
class Mago(Combatiente):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.tipo = "Mago"

    def atacar(self, enemigo):
        prob = random()
        # Si activa su poder
        if prob <= parametros.PROB_MAG:
            defensa_reducida = enemigo.defensa * (1 - parametros.RED_MAG)
            dano = round((self.ataque * parametros.ATQ_MAG) - defensa_reducida)
            self.resistencia = self.resistencia * (1 - parametros.CANSANCIO)
            self.agilidad = self.agilidad * (1 - parametros.CANSANCIO)
            if dano < parametros.DANO_MIN:
                return parametros.DANO_MIN
            else:
                return dano

        # Si no activa su poder
        else:
            dano = round(self.ataque - enemigo.defensa)
            self.resistencia = self.resistencia * (1 - parametros.CANSANCIO)
            self.agilidad = self.agilidad * (1 - parametros.CANSANCIO)
            if dano < parametros.DANO_MIN:
                return parametros.DANO_MIN
            else:
                return dano

    def curarse(self, valor):
        super().curarse(valor)

    def evolucionar(self, item, ejercito_jugador):
        nombre = self.nombre
        vida_max = self.vida_max
        vida = self.vida
        poder = self.poder
        defensa = self.defensa
        agil = self.agilidad
        resis = self.resistencia

        # Si el item es una lanza, entonces evoluciona en un MagoDeBatalla
        if item.nombre == "Lanza":
            ejercito_jugador.combatientes.remove(self)
            combat_evolu = MagoDeBatalla(nombre, vida_max, vida, poder, defensa, agil, resis)
            ejercito_jugador.combatientes.append(combat_evolu)

        # Si el item es una armadura, entonces evoluciona en un CaballeroArcano
        elif item.nombre == "Armadura":
            ejercito_jugador.combatientes.remove(self)
            combat_evolu = CaballeroArcano(nombre, vida_max, vida, poder, defensa, agil, resis)
            ejercito_jugador.combatientes.append(combat_evolu)

    def __str__(self):
        texto_1 = f"¡Hola! Soy {self.nombre}, un Gato {self.tipo} con {self.vida} / {self.vida_max}"
        texto_2 = f" de vida, {self.ataque} de ataque y {self.defensa} de defensa."
        return texto_1 + texto_2
    

    # Paladín
class Paladin(Guerrero, Caballero):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.tipo = "Paladin"

    def atacar(self, enemigo):
        prob = random()
        # Si activa los poderes de Caballero (es decir, si actúa como un Caballero)
        if prob <= parametros.PROB_PAL:
            dano = Caballero.atacar(self, enemigo)
            self.resistencia = self.resistencia * (1 + parametros.AUM_PAL)
            return dano
        # Si actúa como Guerrero
        else:
            dano = Guerrero.atacar(self, enemigo)
            self.resistencia = self.resistencia * (1 + parametros.AUM_PAL)
            return dano

    def curarse(self, valor):
        super().curarse(valor)

    def __str__(self):
        texto_1 = f"¡Hola! Soy {self.nombre}, un Gato Paladín con {self.vida} / {self.vida_max}"
        texto_2 = f" de vida, {self.ataque} de ataque y {self.defensa} de defensa."
        return texto_1 + texto_2
    

    # Mago de Batalla
class MagoDeBatalla(Guerrero, Mago):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.tipo = "MagoDeBatalla"

    def atacar(self, enemigo):
        prob = random()
        # Si actúa como Mago
        if prob <= parametros.PROB_MDB:
            dano = Mago.atacar(self, enemigo)
            self.agilidad = self.agilidad * (1 - parametros.CANSANCIO)
            self.defensa = self.defensa * (1 + parametros.DEF_MDB)
            return dano
        # Si actúa como Guerrero
        else:
            dano = Guerrero.atacar(self, enemigo)
            self.agilidad = self.agilidad * (1 - parametros.CANSANCIO)
            self.defensa = self.defensa * (1 + parametros.DEF_MDB)
            return dano

    def curarse(self, valor):
        super().curarse(valor)

    def __str__(self):
        texto_1 = f"¡Hola! Soy {self.nombre}, un Gato Mago de Batalla con {self.vida} /"
        texto_2 = f" {self.vida_max} de vida, {self.ataque} de ataque y {self.defensa} de defensa."
        return texto_1 + texto_2
    

    # Caballero Arcano
class CaballeroArcano(Caballero, Mago):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.tipo = "CaballeroArcano"

    def atacar(self, enemigo):
        prob = random()
        # Si actúa como Caballero
        if prob <= parametros.PROB_CAR:
            dano = Caballero.atacar(self, enemigo)
            self.poder = self.poder * (1 + parametros.AUM_CAR)
            self.agilidad = self.agilidad * (1 + parametros.AUM_CAR)
            self.resistencia = self.resistencia * (1 - parametros.CANSANCIO)
            return dano
        # Si actúa como Mago
        else:
            dano = Mago.atacar(self, enemigo)
            self.poder = self.poder * (1 + parametros.AUM_CAR)
            self.agilidad = self.agilidad * (1 + parametros.AUM_CAR)
            self.resistencia = self.resistencia * (1 - parametros.CANSANCIO)
            return dano

    def curarse(self, valor):
        super().curarse(valor)

    def __str__(self):
        texto_1 = f"¡Hola! Soy {self.nombre}, un Gato Caballero Arcano con {self.vida} /"
        texto_2 = f" {self.vida_max} de vida, {self.ataque} de ataque y {self.defensa} de defensa."
        return texto_1 + texto_2