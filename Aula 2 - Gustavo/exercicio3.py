alternativa = str(input("Digite seu sexo:"))
if alternativa in "fF" or alternativa == "Femenino":
    print("F - Feminino")
elif alternativa in "mM" or alternativa == "Masculino":
    print("M - Masculino")
elif alternativa == "Nao opinar".lower():
    print("Personalizado")
else:
    print ("Sexo não indentificado")