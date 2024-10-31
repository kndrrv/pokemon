#Kendra Gutiérrez, 2024

class Pokemon: # se crea la clase Pokemon

    def __init__(self, nombre, tipo, nivel, vida, ataque): # se crea el constructor y las variables, self, nombre, tipo, nive, vida y ataque
        self.__name = nombre # se agregan los atributos, utilizando self para poder acceder a ellos
        self.__type = tipo # y utilizando __ para volcer al atributo privado
        self.__level = nivel # así se evita que se pueda acceder o modificar directamente fuera de la clase
        self.__hp = vida
        self.__attack = ataque

    # getter y setter de name
    def get_name(self): # se utiliza el método getter para acceder al atributo privado __name
        return self.__name
    
    def set_name(self, new_name): # se utilizar el método setter para modificar el valor del atributo __name
        self.__name = new_name    
    
    # getter y setter de type
    def get_type(self): # se utiliza el método getter para acceder al atributo privado __type
        return self.__type
    
    def set_name(self, new_type):# se utilizar el método setter para modificar el valor del atributo __type
        self.__type = new_type  
    
    # getter y setter de level
    def get_name(self): # se utiliza el método getter para acceder al atributo privado __level
        return self.__level
    
    def set_name(self, new_level): # se utilizar el método setter para modificar el valor del atributo __level
        self.__level = new_level    

    # getter y setter de hp
    def get_name(self): # se utiliza el método getter para acceder al atributo privado __hp
        return self.__hp
    
    def set_name(self, new_hp): # se utilizar el método setter para modificar el valor del atributo __hp
        self.__hp = new_hp   

    # getter y setter de attack
    def get_name(self): # se utiliza el método getter para acceder al atributo privado __attack
        return self.__name
    
    def set_name(self, new_attack): # se utilizar el método setter para modificar el valor del atributo __attack
        self.__attack = new_attack

    # método para atacar
    def atacar(self, otro_pokemon): # se crea el método con los parámetros necesarios
        ataque = self.__attack
        vida_otro = otro_pokemon.get_hp()
    # verificación de los ataques y la vida del oponente
        if ataque < vida_otro / 2: # si el ataque es menor a la mitad de su vida
            otro_pokemon.set_hp(vida_otro - 1) # se rebaja 1 punto
        elif ataque >= vida_otro / 2 and ataque < vida_otro: # si el ataque es mayor o igual que la mitad de su vida
            otro_pokemon.set_hp(vida_otro - (vida_otro - ataque) / 2) # rebaja la mitad de la diferencia de vida
        elif ataque >= vida_otro: # si el ataque es mayor o igual al total de vida
            otro_pokemon.set_hp(int(vida_otro * 0.8)) # rebaja un 20% de la vida

    def __str__(self): # el método __str__ hace que devuelva una representación en forma de cadena cuando se imprima
        return f"Pókemon: {self.__name}, Tipo: {self.__type}, Nivel: {self.__level}, Vida: {self.__level}, Ataque: {self.__attack}"
    
    