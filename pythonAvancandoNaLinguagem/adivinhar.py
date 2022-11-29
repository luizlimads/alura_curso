from random import randint

secreto = randint(0,100)

def jogarAdivinhar():
    repetir=True
    while(repetir):
        dificuldade = input("Escolha o nuvel de dificuldade\n \
        0 para ter 7 tentativas\n \
        1 para ter 5 tentativas\n \
        2 para ter 3 tentativas\n")
        try:
            dificuldade = int(dificuldade)
            repetir = True if dificuldade < 0 or dificuldade > 2 else False
        except:
            repetir = True
        if (repetir):
            print("Valor digitado não corresponde a um numero no intervalo\n")

    if (dificuldade == 0):
        numeroTentativas = 7
    elif (dificuldade == 1):
        numeroTentativas = 5
    else:
        numeroTentativas = 3

    repetir=True
    while(repetir):
        tentativa = input("digite um valor inteiro entre 0 e 100: ")
        try:
            tentativa = int(tentativa)
            erroDigitar = True if tentativa < 0 or tentativa > 100 else False
        except:
            erroDigitar = True
        
        if (erroDigitar):
            print("Valor digitado não corresponde a um numero no intervalo\n")
        else:
            numeroTentativas -= 1
            print(numeroTentativas)
        
        if (tentativa != secreto and numeroTentativas == 0):
            print("Fim do jogo voce perdeu")
            repetir = False
        elif (tentativa != secreto and numeroTentativas > 0):
            print("Nao acertou")
        else:
            print("Fim do jogo voce ganhou")
            repetir = False

if(__name__ == "__main__"):
    jogarAdivinhar()

