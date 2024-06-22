

def batalla(persona1, persona2, metodo):
    if metodo == "herencia":
        print("++++++Batalla por herencia+++++")
        persona1.atacar(persona2)
        if persona2.esta_vivo():
            persona2.atacar(persona1)
    elif metodo == "encapsulacion":
        print("++++++Batalla por encapsulación+++++++")
        persona1.atacar(persona2)
        if persona2.esta_vivo():
            persona2.atacar(persona1)
    else:
        print("Método no válido")