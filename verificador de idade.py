idade = float(input("Digite a sua idade: "))
if idade <0:
    print("Essa idade não pode ser usada")
elif idade <13:
    print("Essa idade é de uma criança")
elif idade <17:
    print("Essa idade é de um adolescente")
elif idade <60:
    print("Essa idade é de um adulto")
else:
    print("Essa idade é de um idoso")