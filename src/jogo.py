import random

numero_aleatorio = random.randint(1, 10)
papite = int(input("de um papite do numero alatório: "))

while papite != numero_aleatorio:
    if papite == numero_aleatorio:
        print("voce acertou o numero escolhido pelo computador")
    elif papite > numero_aleatorio:
        print("o numero do papite é menor que o numero escolhido pelo computador")
        papite = int(input("de um papite do numero alatório: "))#outro papite
    elif papite < numero_aleatorio:
        print("o numero do papite é maior que o numero escolhido pelo computador")
        papite = int(input("de um papite do numero alatório: "))#outro papiteas