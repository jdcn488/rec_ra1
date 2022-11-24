
from datetime import datetime

nome = str(input("Em qual o seu nome? \n"))

nasc = int(input("Em qual ano você nasceu(em numero)? \n"))

mes = int(input("Em qual mes você nasceu? \n")

ano_atual = datetime.now().year

idade = (ano_atual - nasc)

if idade < 18 :

    print("Você não pode porque tem menos de {} anos em {} e não vai poder fazer as aulas praticas a {} anos, em {}.".format(
        idade, ano_atual, (18 - idade), (nasc + 18))

elif idade >= 18 and mes <= 5:

    print("Você tem {} anos e j.".format(idade))

    print(" {}, há {} anos atrás.".format(
        (nasc + 18), idade - 18))
else:
    print("Você tem {} anos. Está na hora de se alistar.".format(idade))