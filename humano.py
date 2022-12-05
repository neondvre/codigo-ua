from personaje import Personaje

class Humano(Personaje):
    def __init__(self, nombre="", raza="", arma="", vida="", daño="", bonificación=0, familia = ""):
        super().__init__(nombre, raza, arma, vida, daño, bonificación)

        self.__familia = familia

    def get_familia(self):
        return self.__familia
    def set_familia(self, familia):
        self.__familia = familia

    def __str__(self):
        return "nombre {} - raza {} - arma {} - vida {} - daño {} - bonificacion {} - Familia {}".format(self.__nombre, self.__raza, self.__arma,\
             self.__vida, self.__daño, self.__bonificación, self.__familia)


    def super_bono(self):
        a = 1
        while a != 2:
            print("usted ha seleccionado la raza hombre")
            super_bono = int(input("¿Cuánto daño desea agregar?"))
            if super_bono < 5 or super_bono >15:
                print("seleccione un numero del 5 al 15")
            
            
            elif super_bono >= 5 or super_bono <= 15:
                super().set_bonificacion(super_bono)
                vf = super().get_daño() + super().get_bonificacion()
                super().set_bonificacion(vf)
                print(str(super().get_bonificacion()))
                break

    def restar_bono(self):
        i = 1
        if i == range(1,9):
                a = Humano.get_bonificacion() -1
                Humano.set_bonificacion(a)


    def historia_humano(self):
        print("Los hombres son los más débiles, estos no poseen poderes ni características especiales, aún así el Dios Miau les dió una cualidad muy especial...\n"
        "Ninguna")


    def victoria(self):
        print("Los hombres ganan!")
        print(str(super().get_nombre))
        print(str(super().get_raza))
        print(str(super().get_arma))
        print(str(super().get_vida))
        print(str(super().get_daño))
        print(str(super().get_arma))
        print(str(super().get_bonificacion))
        print(str(self.get_familia))

    def derrota(self):
        print("has perdido, quizás el Dios Miau tenga un poco de piedad más adelante ")
        arma = input("Porfavor actualiza tu arma ")
        super().set_arma(arma)
        print("usted escogio", str(super().get_arma))