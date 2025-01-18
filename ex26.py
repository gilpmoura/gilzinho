numero_inicial= int(input("Diz um número inicial: "))

numero_final= int(input("Diz um número final: "))

for x in 25range(numero_inicial, numero_final+1):
    if x%2==0:
        print(x, end=" ")