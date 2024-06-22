from Clases import clases

class Guerrero(clases.Persona):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, arma):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.__arma = arma  # Atributo privado

    def get_arma(self):
        return self.__arma

    def set_arma(self, arma):
        self.__arma = arma

    def __daño(self, enemigo):
        # Los guerreros infligen más daño basado en la fuerza
        return (self.fuerza * 2) - enemigo.defensa

    def atacar(self, enemigo):
        daño = self.__daño(enemigo)
        enemigo.vida -= daño
        print(self.nombre, "ha atacado con su", self.__arma, "e infligido", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()

class Mago(clases.Persona):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, arma):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.__arma = arma  # Atributo privado

    def get_arma(self):
        return self.__arma

    def set_arma(self, arma):
        self.__arma = arma

    def __daño(self, enemigo):
        # Los magos infligen daño basado en la inteligencia
        return (self.inteligencia * 2) - enemigo.defensa

    def atacar(self, enemigo):
        # Los magos pueden lanzar hechizos
        daño = self.__daño(enemigo)
        enemigo.vida -= daño
        print(self.nombre, "ha lanzado un hechizo con su", self.__arma, "e infligido", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()