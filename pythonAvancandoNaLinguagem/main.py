from adivinhar import jogarAdivinhar
from forca import jogarForca

repetir = True
while(repetir):
    jogo = input("Escolha um jogo\n \
        0 para jogar adivinhar\n \
        1 para jogar forca\n")
    try:
        jogo = int(jogo)
        repetir = True if jogo < 0 or jogo > 1 else False
    except:
        repetir = True
    if (repetir):
        print("Valor digitado não corresponde a um numero no intervalo\n")

    if jogo == 0:
        jogarAdivinhar()
    else: 
        jogarForca()