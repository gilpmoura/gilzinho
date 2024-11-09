altura=int(input("Quanto mede a altura da tua parede?: "))
comprimento=int(input("Quanto mede o comprimento da tua parede?: "))

calculo=altura*comprimento #nesta variável, fazemos o cálculo da área da nossa parede
# se 1 litro de tinta preenche 2 metros quadrados da nossa parede,
#só precisamos da quantidade área/2 de tinta para pintá-la toda

tinta=calculo/2

print("Para pintar a parede toda, precisamos de ", tinta,"litros.")

