import random as rd


def adivinar():
    a = rd.randint(1, 101)
    b = rd.randint(1, 101)
    suma = a + b

    while True:
        user = int(input("Ingrese la suma de los números aleatorios entre 0 y 200:"))
        if user == suma:
            print("Felicidades, has adivinado")
            break
        else:
            print("Su respuesta no es correcta")

adivinar()