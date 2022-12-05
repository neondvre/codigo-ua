class Personaje:
    def __init__(self, nombre = "", raza = "", arma = "", vida = "", daño = "", bonificación = 0.0):
        self.__nombre = nombre
        self.__raza = raza
        self.__arma = arma
        self.__vida = vida
        self.__daño = daño
        self.__bonificación = bonificación


    
        
    def get_nombre(self):
        return self.__nombre
    def get_raza(self):
        return self.__raza
    def get_arma(self):
        return self.__arma
    def get_vida(self):
        return self.__vida
    def get_daño(self):
        return self.__daño
    def get_bonificacion(self):
        return self.__bonificación

    def set_nombre(self, nombre):
        self.__nombre = nombre
    def set_raza(self, raza):
        self.__raza = raza
    def set_arma(self, arma):
        self.__arma = arma 
    def set_vida(self,vida):
        self.__vida = vida
    def set_daño(self, daño):
        self.__daño = daño
    def set_bonificacion(self,bonificacion):
        self.__bonificación = bonificacion

    def __str__(self):
        return "nombre {} - raza {} - arma {} - vida {} - daño {} - bonificacion {}".format(self.__nombre, self.__raza, self.__arma, self.__vida, self.__daño, self.__bonificación)

    
    
        
    