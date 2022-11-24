from random import randint


contador = 0


while (True):

    jogador1 = 200

    jogador2 = 200


    print('1. atacar')

    print('2. curar')

    print('3. fim')


    entrada = int(input("Digite uma opção: "))

    if entrada == 1 and jogador1 > 0 and jogador2 > 0:

        dano = randint(50,100)
        dano2 = randint(50,100)

        if contador % 2 == 0:

            print(f'Player 1 tirou {dano}')

            jogador2 = jogador2 - dano

            print('1. atacar')

            print('2. curar')

            print('3. fim')

            entrada = int(input("Digite uma opção: "))

            print(f'vida do Player 1: {jogador1}')

            print(f'vida do Player 2: {jogador2}')

            contador = contador + 1

        else:
            print(f'Player 2 tirou {dano2}')

            jogador1 = jogador1 - dano2

            print('1. atacar')

            print('2. curar')

            print('3. fim')

            entrada = int(input("Digite uma opção: "))

            print(f'vida do Player 1: {jogador1}')

            print(f'vida do Player 2: {jogador2}')

            concontador = contador + 1


    if entrada == 2 and jogador1 > 0 and jogador2 > 0:

        cura = randint(30,50)

        if contador % 2 == 0:

            print(f'Player 1 tirou {cura}')

            jogador1 = jogador1 + cura

            concontador = contador + 1

        else:
            print(f'Player 2 tirou {cura}')

            jogador2 = jogador2 + cura

            concontador = contador + 1

    if entrada == 3:

        if (jogador1) > (jogador2):

            print('Player 1 é o vencedor')

            print('Obrigada por jogar!')

        elif (jogador1) < (jogador2):

            print('Player 2 é o vencedor')

            print('Obrigada por jogar!')

        else:
            print('Empate')

            print('Obrigada por jogar!')

            break

    contador += 1