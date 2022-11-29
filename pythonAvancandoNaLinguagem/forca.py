from random import randint
def jogarForca():
    ref_arquivo = open("palavras.txt","r")
    for _ in range(randint(1,9)):
        linha = ref_arquivo.readline()
        valores = linha.split()
    ref_arquivo.close()


    continuaJogo = True
    palavraSecreta = valores[0]

    continuaJogo = True
    letrasAcertadas = [None]*len(palavraSecreta)
    erros = 0   

    while continuaJogo:
        chute = input("digite uma letra: ").strip()
        chute = chute.upper()

        if palavraSecreta.find(chute) == -1:
            erros += 1
            if erros == 6:
                print('voce perdeu')
                continuaJogo = False
                continue
        else:
            posicao = 0
            for letra in palavraSecreta:
                if chute == letra.upper():
                    letrasAcertadas[posicao] = letra
                posicao += 1
            print(letrasAcertadas)
        
        if len(list(filter(None,letrasAcertadas))) == len(palavraSecreta):
            print('voce ganhou')
            continuaJogo = False

if(__name__ == "__main__"):
    jogarForca()