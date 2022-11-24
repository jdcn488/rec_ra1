n = 0
cont = 0
cont2 = 0

for i in range(0,10):

    numeros = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    n = int(input("Digite um numero: \n"))

    if cont % 2 == 0:

        mumeros.append(n)

        cont = cont + 1

    else:
        print("O número {} é ímpar.".format(n))

        mumeros.append(n)

        cont2 = cont2 + 1



        menor = n
        for menor in range(numeros):
            if menor % 2 == 0:
                cont = cont + 1
                menor = n
            else:
                cont2 = cont2 + 1
                menor = n

        maior = n
        for maior in range(numeros):
            if maior % 2 == 0:
                cont = cont + 1
                maior = n
            else:
                cont2 = cont2 + 1
                maior = n

        print("O maior resultado foi: {}.".format(maior))
        print("O menor resultado foi: {}.".format(menor))