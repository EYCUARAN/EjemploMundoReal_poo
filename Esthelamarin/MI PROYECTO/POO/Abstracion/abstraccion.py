from abc import ABC, abstractmethod


class Personaje(ABC):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, arma):
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self.__vida = vida
        self.__arma = arma

    @property
    def nombre(self):
        return self.__nombre

    @property
    def fuerza(self):
        return self.__fuerza

    @property
    def inteligencia(self):
        return self.__inteligencia

    @property
    def defensa(self):
        return self.__defensa

    @property
    def vida(self):
        return self.__vida

    @vida.setter
    def vida(self, valor):
        self.__vida = valor

    @property
    def arma(self):
        return self.__arma

    def atributos(self):
        print(self.nombre, ":", sep="")
        print("·Fuerza:", self.fuerza)
        print("·Inteligencia:", self.inteligencia)
        print("·Defensa:", self.defensa)
        print("·Vida:", self.vida)
        print("·Arma:", self.__arma)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.__fuerza += fuerza
        self.__inteligencia += inteligencia
        self.__defensa += defensa

    def esta_vivo(self):
        return self.__vida > 0

    def morir(self):
        self.__vida = 0
        print(self.nombre, "ha muerto")

    @abstractmethod
    def __daño(self, enemigo):
        pass

    @abstractmethod
    def atacar(self, enemigo):
        pass


class Guerrero(Personaje):
    def __daño(self, enemigo):
        return (self.fuerza * 2) - enemigo.defensa

    def atacar(self, enemigo):
        daño = self.__daño(enemigo)
        enemigo.vida -= daño
        print(self.nombre, "ha atacado con su", self.__arma, "e infligido", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", enemigo.vida)

        else:
            enemigo.morir()


class Mago(Personaje):
    def __daño(self, enemigo):
        return (self.inteligencia * 2) - enemigo.defensa

    def atacar(self, enemigo):
        daño = self.__daño(enemigo)
        enemigo.vida -= daño
        print(self.nombre, "ha lanzado un hechizo con su", self.__arma, "e infligido", daño, "puntos de daño a",
              enemigo.nombre)

        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()
