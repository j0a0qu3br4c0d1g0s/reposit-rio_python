numero = float(input("Digite um número: "))
if numero > 0 and numero % 2 == 0 :
    print("Número é Positivo e Par")
elif numero > 0 and numero % 2 != 0:
    print("Número é Impar  e negativo")
elif numero == 0:
    print("Número é Zero")
else:
    print("Este número não corresponde a nenhum outro número anterior")