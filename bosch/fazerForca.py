import random


def definirPalavra():
    tamLista = 0
    indexTemas = []
    indexPalavras = []
    indexPalaTema = []
    palavraDoTema = []
    lista = []
    arq = open("./bosch/Palavras.txt", "r", encoding="utf-8")
    txtArq = arq.read()
    palavra = ""
    for ponteiro in txtArq:
        if ponteiro == "\n":
            continue
        if ponteiro == "|":
            continue
        if ponteiro != ",":
            palavra += ponteiro
        else:
            lista.append(palavra)
            palavra = ""
    arq.close()
    for i in lista:
        if i == i.upper():
            # print(i)
            indexTemas.append(tamLista)
        else:
            indexPalavras.append(tamLista)

        tamLista += 1

    aleaT = random.choice(indexTemas)
    # print("------------------")
    for i in range(aleaT+1, (len(lista)-1)):
        if indexPalavras.__contains__(i):
            indexPalaTema.append(i)
            palavraDoTema.append(lista[i])
        else:
            break
    aleaP = random.choice(indexPalaTema)
    tema = lista[aleaT]
    palavra = lista[aleaP]
    # print("\n\nFIM DE 'definirPalavra\n\n")
    return tema, palavra


def desenho(i):
    if i == 6:
        print("_______\n"
              "|    |         \n"
              "|\n"
              "|\n"
              "|   |‾‾|‾| \n"
              "|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    if i == 5:
        print("_______\n"
              "|    |O\n"
              "|\n"
              "|\n"
              "|   |‾‾|‾| \n"
              "|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    if i == 4:
        print("_______\n"
              "|    |O       \n"
              "|     T       \n"
              "|\n"
              "|   |‾‾|‾| \n"
              "|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    if i == 3:
        print("_______\n"
              "|    |O       \n"
              "|    /T\      \n"
              "|\n"
              "|   |‾‾|‾| \n"
              "|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    if i == 2:
        print("_______\n"
              "|    |O       \n"
              "|    /T\      \n"
              "|     ‾      \n"
              "|   |‾‾|‾| \n"
              "|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    if i == 1:
        print("_______\n"
              "|    |O       \n"
              "|    /T\      \n"
              "|    /‾\      \n"
              "|   |‾‾|‾| \n"
              "|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    if i == 0:
        print("_______\n"
              "|     |"
              "|     O       \n"
              "|    /T\      \n"
              "|    |‾|      \n"
              "|‾‾‾\   /‾‾‾‾‾‾‾‾‾‾‾‾")


def jogo(tema, palavra, dica):

    letras = []
    palavraOcul = "_ " * len(palavra)
    print(palavraOcul)

    while chances > 0:
        # print("\n\nESCREVA UMA LETRA, PODE ESCREVER EU NAO MORDO\n")
        while True:
            print("LETRAS DIGITADAS: ", letras)
            digitado = input("letra: ").upper()
            if len(digitado.strip()) > 1:
                if digitado.strip().lower() == "sim" and not dica:
                    print("DICA ATIVA")
                    dica = True
                    print("TEMA: ", tema)
                    desenho(chances)
                    print("PALAVRA: ", palavraOcul)
                else:
                    print("VOCE DIGITOU MAIS DE UMA LETRA")
                continue
            if digitado not in letras:
                letras.append(digitado)
                break
            else:
                print("ESSA LETRA JA FOI DIGITADA")
                continue

        if palavra.upper().__contains__(digitado):
            print("\nACERTOU U-U\n")
        else:
            chances = chances - 1
            print("\nOOOHH VOCE ERROU\n")
        print("TEMA: ", tema)
        desenho(chances)
        print("SUAS VIDAS: ", chances)
        checar = 0
        print("PALAVRA: ", end="")
        palavraOcul = ""
        for i in palavra:
            hide = True
            for j in letras:
                if i.upper() == j.upper():
                    print(i, end=" ")
                    checar += 1
                    hide = False
                    palavraOcul += j+" "
            if hide:
                print("_ ", end="")
                palavraOcul += "_ "
        print("\n", checar, "/", len(palavra))
        if checar == len(palavra):
            print("GANHOU")
            break
    if chances <= 0:
        print("VOCÊ PERDEU")

def jogar():
    dica = False
    topico, termo = definirPalavra()
    jogo(topico, termo, dica)
