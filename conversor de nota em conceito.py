nota = float(input("Digite a nota do aluno: "))

conceito = (nota)
print("O conceito correspondente à nota", nota, "é:", conceito)

if nota >= 9:
    print("A")
elif nota >= 7.5:
    print("B")
elif nota >= 6:
    print("C")
elif nota >= 5:
    print("D")
else: 
    print("F")