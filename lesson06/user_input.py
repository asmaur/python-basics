"""Nesta aula vamos criar o jogo de Pedra, Papel e Tesoura em python.
Vamos aprender condicionais e entrada de dados pelo usuário!.

Por mais informações e documentação sempre consultar a site
oficial do Python em https://pyhon.org/docs

"""

import random
import sys
from enum import Enum

class Jogo(Enum):
    PEDRA = 1
    PAPEL = 2
    TESOURA = 3


print("")
numero = input("Entre um numero... \n1 para Pedra, \n2 para Papel, \n3 para Tesoura: \n\n")

jogador = int(numero)

if jogador < 1 or jogador > 3:
    sys.exit("Escolha um numero: 1, 2 ou 3 \n")

computador = int(random.choice("123"))

print("")
# print("Você escolheu: " + str(jogador))
# print("O computador escolheu: " + str(computador))
print("Você escolheu: " + str(Jogo(jogador)).replace("Jogo.", ""))
print("O computador escolheu: " + str(Jogo(computador)).replace("Jogo.", ""))

if jogador == 1 and computador == 3:
    print("🎉 Você ganhou!")
elif jogador == 2 and computador == 1:
    print("🎉 Você ganhou!")
elif jogador == 3 and computador == 2:
    print("🎉 Você ganhou!")
elif jogador == computador:
    print("😒 Empate!")
else:
    print("🐍 O computador ganhou!")


