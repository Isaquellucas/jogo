import random
numero_aleatorio = random.randint(1, 20)
papite = int(input("de um papite sobre o numero escolhido: "))
vidas = 3

while papite != numero_aleatorio:
    if vidas == 0:
        print("\033[1;35m" + "Você perdeu")
        break
    elif papite < numero_aleatorio:
        print("o numero escolhido é "  + "\033[0;36m" +  "maior")
        vidas = vidas - 1 #perde uma vida caso erre
        print('\033[1;31m' + 'Você perdeu uma vida' + '\033[0m')#muda a cor pra vermelho
        papite = int(input("de um papite sobre o numero escolhido: "))
    elif papite > numero_aleatorio:
        print("o numero escolhido é " + "\033[0;36m" + "menor")
        vidas = vidas - 1 #perde uma vida caso erre
        print('\033[1;31m' + 'Você perdeu uma vida' + '\033[0m')#muda a cor pra vermelho
        papite = int(input("de um papite sobre o numero escolhido: "))
if papite == numero_aleatorio:
    print ('\033[1;32m' + 'Você ganhou' + '\033[0m')#muda a cor pra verde