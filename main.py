from elfo import Elfo 
from enano import Enano
from humano import Humano
import random

b = 0
persrandom = []

obj1 = Elfo("elfo", "aaa",  "espada", 500, 60, 20, "miau")
obj2 = Humano("aaa", "hombre", "espada", 600 , 60, 10, "triton")
obj3 = Enano("jiji", "enano", "espada", 500, 70 , 20, "oreo")
persrandom.append(obj1)
persrandom.append(obj2)
persrandom.append(obj3)
def selectRandom(persrandom):
    a = random.choice(persrandom)
    return a

def menu():
    print("bienvenido a 'las desaventuras de miau\n"
        "porfavor selecione una opción\n"
        "1.- Leer historia\n"
        "2.- Jugar\n"
        "3.- Salir")
    
def manual():       
    p1 =int(input("seleccione la raza del personaje 1:\n"
            "1.- Elfo\n"
            "2.- Enano\n"
            "3.- Hombre"))
    if p1 == 1:
                raza = "elfo"
                nombre = input("introduzca el nombre de su personaje")
                arma = input("¿Qué arma desea ultilizar?")
                vida = 500
                daño = 60
                bonificacion = 20
                reino = input("a que reino pertenece?")
                obj_elfo = Elfo(nombre, raza, arma, vida, daño, bonificacion, reino)
                obj_elfo.quita_vida()
                return obj_elfo
            
    elif p1 == 2:
                raza = "enano"
                nombre = input("introduzca el nombre de su personaje")
                arma = input("¿Qué arma desea ultilizar?")
                vida = 500
                daño = 70
                bonificacion = 0
                clan = input("introduzca clan")
                obj_enano = Enano(nombre, raza, arma, vida, daño, bonificacion, clan)
                obj_enano.aumenta_vida()
                return obj_enano
            
    elif p1 == 3:
                raza = "hombre"
                nombre = input("introduzca el nombre de su personaje")
                arma = input("¿Qué arma desea ultilizar?")
                vida = 600
                daño = 60
                bonificacion = 0
                familia = input("introduzca familia")
                obj_hombre = Humano(nombre, raza, arma, vida, daño, bonificacion, familia)
                obj_hombre.super_bono()
                return obj_hombre

def combate():
    p2 = int(input("el combate está por comenzar\n"
       "escoge a tu oponente: \n"
       "1.- Manual \n"
       "2.- Aleatorio "))
    if p2 == 1:
        jugador2 = manual()
        for i in range(10):
            i = i + 1
            jugador.set_vida(jugador.get_vida() - jugador2.get_daño())
            if jugador2.get_vida() <= 0:
                print("el jugador 2 a perdido!! ")
                print(str(jugador.victoria()))
                break
            elif jugador.get_vida() <= 0:
                print("el jugador 1 a perdido ")
                print(str(jugador2.victoria()))
                break
            Humano.restar_bono(Humano)
        if jugador.get_vida() > jugador2.get_vida():
            print("el ganador es el jugador 1 ")
        elif jugador2.get_vida() > jugador.get_vida():
            print("el ganador es el jugador 2 ")
 
    if p2 == 2:
        jugador2 = selectRandom(persrandom)
        print("tu oponente será ", jugador2.get_raza())
        for i in range(10):
            i = i + 1
            jugador.set_vida(jugador.get_vida() - jugador2.get_daño())
            if jugador2.get_vida() <= 0:
                print("el jugador 2 a perdido!! ")
                print(str(jugador.victoria()))
                break
            elif jugador.get_vida() <= 0:
                print("el jugador 1 a perdido ")
                print(str(jugador2.victoria()))
                break
            if i == range(1,9):
                a = jugador2.get_bonificacion() -1
                jugador2.set_bonificacion(a)
        if jugador.get_vida() > jugador2.get_vida():
            print("el ganador es el jugador 1 ")
        elif jugador2.get_vida() > jugador.get_vida():
            print("el ganador es el jugador 2 ")
 

a = 0
while a != 3:
    menu()
    opcion = int(input())
    if opcion == 1:
        historia = int(input("¿De cuál raza desea leer su historia?\n"
        "1.- Elfos\n"
        "2.- Enanos\n"
        "3.- Humanos"))

        if historia == 1:
            print(str(Elfo.historia_elfo(Elfo)))
        elif historia ==2:
            print(str(Enano.historia_enano(Elfo)))
        elif historia == 3:
            print(str(Humano.historia_humano(Humano)))


    if opcion == 2:
        print("debes crear tu personaje primero")
        jugador = manual()
        print("tu personaje es:")
        
        combate()
    if opcion == 3:
        exit()

        