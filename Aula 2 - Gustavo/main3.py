numero = int(input("Digite um numero:"))
if numero >= 1 and numero <= 10:
    print("Número válido")
else:
        print("Número inválido")

alternativa = str(input("Digite S/N se você deseja sair: ")).lower()
if alternativa == "s" or alternativa == "n":
    print("Operação inválida")
    if alternativa == "s":
     print("adeus")
    else:
     print("continue")

else:
    print("Operação inválida")