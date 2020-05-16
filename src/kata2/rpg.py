#!/usr/bin/python

import random
import string
from random import randint


def RandomPasswordGenerator(passLen=10):

    letras = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    letrasMinus = letras.lower()
    numeros = "1234567890"
    caracteresEspeciale = "|@#~€¬!·$%/&%(/)/¿?^*"

    opciones = [letras, letrasMinus, numeros, caracteresEspeciale]
    contraseña = ''
    for i in range(passLen):
        opcion = opciones[randint(0, len(opciones)-1)]
        contraseña += opcion[randint(0, len(opcion)-1)]
    return contraseña


print(RandomPasswordGenerator(15))
