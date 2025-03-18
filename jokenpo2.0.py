# Jokenpô
#Pedra, papel e tesoura

escolha_jogador = int(input("Escolha [1] pedra, [2] papel ou [3] tesoura: "))

import random
escolha_computador = random.randint(1,3)

print("Escolha do jogador:",escolha_jogador)
print("Escolha do computador:",escolha_computador)
if(escolha_jogador == 1 and escolha_computador == 2):
  print("Jogador perdeu")
elif(escolha_jogador == 1 and escolha_computador == 3):
  print("Jogador venceu")
elif(escolha_jogador == 2 and escolha_computador == 1):
  print("Jogador venceu")
elif(escolha_jogador == 2 and escolha_computador == 3):
  print("Jogador perdeu")
elif(escolha_jogador == 3 and escolha_computador == 1):
  print("Jogador perdeu")
elif(escolha_jogador == 3 and escolha_computador == 2):
  print("Jogador venceu")
else:
    print("Empate")