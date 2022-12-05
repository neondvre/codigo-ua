from personaje import Personaje

class Elfo(Personaje):
    def __init__(self, nombre="", raza="", arma="", vida="", daño="", bonificación=0, reino = ""):
        super().__init__(nombre, raza, arma, vida, daño, bonificación)

        self.__reino = reino

    def get_reino(self):
        return self.__reino

    def set_reino(self,reino):
        self.__reino = reino 

    
    def __str__(self):
        return "nombre {} - raza {} - arma {} - vida {} - daño {} - bonificacion {} - reino {}".format(self.__nombre, self.__raza, self.__arma,\
             self.__vida, self.__daño, self.__bonificación,self.__reino)



    def historia_elfo(self):
        print("Los elfos provienen del reino Miau, el cuál contiene la mayor cantidad de habitantes. Son conocidos por su gran inteligencia\n"
        "y destreza. ")



    def quita_vida(self):
        print("usted ha seleccionado la clase elfo")
        quita_vida= 0.9 * super().get_vida()
        super().set_vida(quita_vida)
        print("la vida final de su personaje es de" , int(super().get_vida()))
    
    def victoria_elfo(self):
        print("Los elfos ganan!")
        print(str(super().get_nombre))
        print(str(super().get_raza))
        print(str(super().get_arma))
        print(str(super().get_vida))
        print(str(super().get_daño))
        print(str(super().get_arma))
        print(str(super().get_bonificacion))
        print(str(self.get_reino))



    


    




