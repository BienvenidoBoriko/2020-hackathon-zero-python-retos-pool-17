from random import randint

options = ["Piedra", "Papel", "Tijeras"]


def quienGana(player, ai):

    player = player.lower()

    ai = ai.lower()

    if (player == 'piedra' and ai == 'papel'):
        return 'Perdiste!'
    elif(player == 'piedra' and ai == 'piedra'):
        return 'Empate!'
    elif(player == 'papel' and ai == 'papel'):
        return 'Empate!'
    elif(player == 'tijeras' and ai == 'tijeras'):
        return 'Empate!'
    elif(player == 'piedra' and ai == 'papel'):
        return 'Perdiste!'
    elif(player == 'papel' and ai == 'tijeras'):
        return 'Perdiste!'
    elif(player == 'tijeras' and ai == 'piedra'):
        return 'Perdiste!'
    elif(player == 'piedra' and ai == 'tijeras'):
        return 'Ganaste!'
    elif(player == 'papel' and ai == 'piedra'):
        return 'Ganaste!'
    elif(player == 'tijeras' and ai == 'papel'):
        return 'Ganaste!'
    else:
        return 'obcion invalida'


def Game():
    global options

    optionIa = options[randint(0, len(options) - 1)]

    opcionUser = input("elige una opcion [Piedra - Papel - Tijera]: ")

    winner = quienGana(opcionUser, optionIa)

    print(winner)


Game()
