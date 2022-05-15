from random import randint
from time import sleep

print("BEM VINDO AO JOGO JO-KEN-PÔ")
nome = input(str("Qual seu nome? "))
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
itens = ('PEDRA', 'PAPEL', 'TESOURA')
jogador = int(input("Qual a sua jogada? "))

pc = randint(0,2)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ")
sleep(1)
print('=~='*8)
print("O você jogou {}".format(itens[jogador]))
print("O Computador jogou {}".format(itens[pc]))
print('=~='*8)


if jogador == 0 and pc == 2  or jogador == 1 and pc == 0 or jogador == 2 and pc == 1:
    print("{} venceu!".format(nome))
elif jogador == 0 and pc == 0 or jogador == 1 and pc == 1 or jogador == 2 and pc == 2:
    print("Empate! tente novamente!")
elif jogador == 0 and pc == 1 or jogador == 1 and pc == 2 or jogador == 2 and pc == 0:
    print("{} perdeu!".format(nome))
else:
    print("JOGADA INVALIDA")
