

import random



cartas = [

    {"nome": "Lula", "ataque": 80, "defesa": 60, "velocidade": 90},

    {"nome": "Polvo", "ataque": 70, "defesa": 85, "velocidade": 75},

    {"nome": "Camarão", "ataque": 65, "defesa": 50, "velocidade": 95}

]



def escolher_carta():

    return random.choice(cartas)



def mostrar_carta(carta):

    print(f"\nCarta: {carta['nome']}")

    print(f"Ataque: {carta['ataque']}")

    print(f"Defesa: {carta['defesa']}")

    print(f"Velocidade: {carta['velocidade']}")



print("Bem-vindo ao Super Trunfo - Frutos do Mar!\n")



carta_jogador = escolher_carta()

carta_maquina = escolher_carta()



mostrar_carta(carta_jogador)



atributo = input("\nEscolha um atributo para competir (ataque, defesa ou velocidade): ").lower()



valor_jogador = carta_jogador[atributo]

valor_maquina = carta_maquina[atributo]



print("\nCarta da máquina:")

mostrar_carta(carta_maquina)



print(f"\nSeu valor: {valor_jogador} x Valor da máquina: {valor_maquina}")



if valor_jogador > valor_maquina:

    print("\nVocê venceu!")

elif valor_jogador < valor_maquina:

    print("\nVocê perdeu!")

else:

    print("\nEmpate!")
