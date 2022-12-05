from personaje import Personaje

class Enano(Personaje):
    def __init__(self, nombre="", raza="", arma="", vida=0, daño=0, bonificación=0, clan = ""):
        super().__init__(nombre, raza, arma, vida, daño, bonificación)
    

        self.__clan = clan

    def get_clan(self):
        return self.__clan
    def set_clan(self, clan):
        self.__clan = clan

    def __str__(self):
        return "nombre {} - raza {} - arma {} - vida {} - daño {} - bonificacion {} - clan {}".format(self.__nombre, self.__raza, self.__arma,\
             self.__vida, self.__daño, self.__bonificación, self.__clan)

    def aumenta_vida(self):
        a= 3
        while a !=2:
            print("usted ha seleccionado la clase enano")
            aumenta_vida= int(input("¿cuánta vida desea agregar?"))
            if aumenta_vida <50 or aumenta_vida >100:
                print("seleccione un número entre el 50 y 100")
            elif aumenta_vida >=50 or aumenta_vida <=100:
                super().set_bonificacion(aumenta_vida)
                vf = super().get_vida() + super().get_bonificacion()
                super().set_vida(vf)
                print("la vida final es de: ", str(super().get_vida()))
                break

    def historia_enano(self):
        print("Los enanos vienen del clan Tritón, suelen ser juguetones y traviesos. Además, tal como Tritón, comen mucho y siempre están sucios.\n"
        "")

    def derrota(self):
        print("Los enanos han perdido, quizás en un futuro el dios Miau tenga más piedad contigo waja :P")

    def victoria(self):
        print("Los enanos ganan!")
        print(str(super().get_nombre))
        print(str(super().get_raza))
        print(str(super().get_arma))
        print(str(super().get_vida))
        print(str(super().get_daño))
        print(str(super().get_arma))
        print(str(super().get_bonificacion))
        print(str(self.get_clan))

