alternativa = str(input("Digite uma vogal ou consoante: "))
if alternativa in "aeiou":
    print("Vogal")
elif alternativa in "bcdfghjklmnpqrstvwxyz":
    print("Consoante")
else:
    print("não é uma letra")