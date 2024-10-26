a= 10 # branco -> VARIÁVEL ; azul -> NÚMERO
b= 5

print(a) #uma PRINT é a comunicação que o código dará na consola, ou seja, smepre que quisermos que algo apareça
         #na consola

print(a+b

#quando nós defenimos algum tipo de variável (texto que aparece em branco) temos a defenir
#no caso de a e b (as variáveis anteriormente defenidas) , efetuamos esse processo com a sua IDENTIFICAÇÃO
#  O NOME DA VARIÁVEL chama-se IDENTIFICADOR DA VARIÁVEL, ou seja, no caso de "a" e "b", os seus nomes
#são os seus identificadores

#SEMPRE QUE MENCIONAMOS o nome da variável no código, significa que nos estamos a referir ao VALOR QUE ELA ARMAZENA
#PARA DEFINIR UMA VARIÁVEL começamos por lhe dar um nome e depois adicionamos um "=" (neste caso, o = significa
#                                                                                                            DEFINIR)

#----------------------------------INPUTS e PRINTS

#como vimos no exemplo anterior, a função print() retorna um resultado no ecrã
#já que as variáveis são objetos que amrzenam e guardam valores, podemos reter um valor espicificado pelo utilizador

#neste caso, utilizamos uma nova função:     input()

#a função input() aguarda uma ENTRADA DE INFORMAÇÃO DO UTILIZADOR ATRAVÉS DO TERMINAL (Phyton console ou consola)

#podemos fazer um input() de palavras (dados de texto) -> STRINGS

#ou podemos fazer um input de valores numéricos (números) -> INT (inteiros) FLOAT (decimais)
#                                                             ^               ^
#                                                             |               |
#                                  designação de números INTEIROS em python   |
#                                                                    designação de números DECIMAIS em python

#AUTOMATICAMENTE, ao escrevermos a função input(), ela vai interpretar os dados como STRINGS
#vamos ver a diferença entre uma STRING e um NÚMERO:

c="5"
d="6" #uma STRING é sempre introduzida com ASPAS "" e o texto aparece a VERDE

print(c+d) #se eu SOMAR estas duas VARIÁVEIS que, por sua vez, armazenam STRINGS, o código apenas vai juntar
#                 os dois algarismos, porque não podemos somar dados de texto

#se eu quiser fazer um input() NUMÉRICO, devo especificar ANTES DA FUNÇÃO:

# int(input()) - ISTO OBRIGA A FUNÇÃO INPUT() A APENAS ACEITAR NÚMEROS INTEIROS

nome=input() #para podermos usar aquilo que escrevemos nos inputs temos de os armazenar em variáveis

print(nome) #assim, o valor da variável nome passa a ser aquilo que foi escrito no input