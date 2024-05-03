LadoA = float(input("Digite o comprimento do Lado A: "))
LadoB = float(input("Digite o comprimento do Lado B: "))
LadoC = float(input("Digite o comprimento do Lado C: "))

tipo = (LadoA, LadoB, LadoC)
print("Tipo de triângulo:", tipo)

if (LadoA + LadoB < LadoC) or (LadoB + LadoC < LadoA) or (LadoC + LadoA < LadoB):
    print("Não pode ser um triângulo")
elif (LadoA == LadoB) and (LadoA == LadoC) and (LadoB == LadoC):
    print("Esse triângulo é Equilátero, todos os lados são iguais.")
elif (LadoA == LadoB and LadoC < LadoA) or (LadoB == LadoC and LadoA < LadoB) or (LadoC == LadoA and LadoB < LadoC):
    print("O triângulo é Isósceles, dois lados são iguais.")
elif (LadoA + LadoB > LadoC) and (LadoA + LadoC > LadoB) and (LadoB + LadoC > LadoA):
    print("Esse triângulo é Escaleno, os três lados são diferentes.")