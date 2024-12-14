velocidade=int(input("A que velocidade passaste no radar?: "))

limite=80

passagemlimite=0

multa=0

if velocidade>limite:
    passagemlimite=velocidade-limite
    multa=pasagem*2

    print(f"Estás a ir muito depressa! Passaste")