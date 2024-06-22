from Clases import clases


class Guerrero(clases.Persona):
    def daño(self, enemigo):
        # Los guerreros infligen más daño basado en la fuerza
        return (self.fuerza * 2) - enemigo.defensa


class Mago(clases.Persona):
    def daño(self, enemigo):
        # Los magos infligen daño basado en la inteligencia
        return (self.inteligencia * 2) - enemigo.defensa

    def atacar(self, enemigo):
        # Los magos pueden lanzar hechizos
        daño = self.daño(enemigo)
        enemigo.vida -= daño
        print(self.nombre, "ha lanzado un hechizo e infligido", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()