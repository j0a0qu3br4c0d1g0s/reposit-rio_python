peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
imc = peso/(altura*altura)
if imc < 18.5:
    print("Muito magro(a)")
elif imc <= 24.9:
    print("É saudavel")
elif imc <= 29.9:
    print("Sobrepeso")
elif imc <= 34.9:
    print("Obesidade grau (pouco preocupante) 1")
elif imc <= 39.9:
    print("Obesidade grau 2 (vixi, esse ai tá gordo igual um peixe-boi, já pode internar)")
else:
    print("Obesidade grau 3 (Esse ai vai morrer com certeza kkkkk)")