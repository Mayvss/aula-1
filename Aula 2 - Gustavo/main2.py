cor = str(input("Digite [vermelho amarelo ou verde] :")).lower().strip()

match cor: 
    case "vermelho":
        print("Pare")
    case "amarelo":
        print("atenção")
    case "verde":
        print("Adiante")
    case _:
        print("Cor não correspondente")
