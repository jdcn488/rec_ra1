peso = float(input("Digite seu peso (em kg): \n"))

altura = float(input("Digite sua altura (em m): \n"))


imc = (peso / (altura**2))

if imc < 16:

    print("Seu IMC é de: {:.1f}. magreza grave.".format(imc))

elif imc >= 16 and imc < 17:
    print("Seu IMC é de: {:.1f}. magreza moderada.".format(imc))

elif imc >= 17 and imc < 18.5:
    print("Seu IMC é de: {:.1f}. magreza leve.".format(imc))

elif imc >= 18.5 and imc < 25:
    print("Seu IMC é de: {:.1f}. saldavel.".format(imc))

elif imc >= 25 and imc < 30:
    print("Seu IMC é de: {:.1f}. sobrepeso.".format(imc))

elif imc >= 30 and imc < 35:
    print("Seu IMC é de: {:.1f}. obesidada grau 1.".format(imc))

elif imc >= 35 and imc < 40:
    print("Seu IMC é de: {:.1f}. obesidada grau 2.".format(imc))

else:
    print("Seu IMC é de: {:.1f}. obesidade grau 3.".format(imc))


