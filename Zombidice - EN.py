'''
Pontifícia Universidade Católica do Paraná
Course: Systems Analysis and Development
Discipline: Computational Logic
Student: Fernando Doszanet Elias

Final Project

Project started on: 04/03/2022
Last modified on: 17/04/2022
'''

# Creation of game counters and libraries import
import random
jogadorAtual = 0
cerebros = 0
passos = 0
tiros = 0
rodada = 0
vitoria = 0
maior = 0
vencedores = []
listaPontuacao = []


# Creation of functions used in the game
def numero_de_jogadores():
    """
    Ask the user for the number of players in this match.

    :return: Number of players
    """
    x = 0
    while x < 2:
        try:
            x = int(input("Please provide the number of players: "))
            if x < 2:
                print("You need at least 2 players!")
        except ValueError:
            print("Invalid value")
    return x


def nome_jogadores(x: int):
    """
    Receives the number of players and asks for the names of these players, returning a list.

    :param x: Number of players
    :return: List with the names of the players
    """
    listaX = []
    z = 0
    while z < x:
        y = input("Now, please enter player " + str(z + 1) + " name: ")
        listaX.append(y)
        z += 1
    return listaX


def pontuacao_inicial(x: int):
    """
    Create a list with the initial score of each player.

    :param x: Number of players
    :return: List with the initial score set to 0 for each player
    """
    listaX = []
    for z in range(x):
        listaX.append(0)
    return listaX


def dados_disponiveis(x: list):
    """
    Calculate the number of dice available for each roll.

    :param x: List with the available dice
    :return: Returns, respectively, the number of green, yellow, and red dice at this moment.
    """
    vd = 0
    a = 0
    ve = 0
    for z in range(len(x)):
        if x[z] == dadoVerde:
            vd += 1
        elif x[z] == dadoAmarelo:
            a += 1
        else:
            ve += 1
    return vd, a, ve


def sortear_dados(x: list):
    """
    Randomly select 3 dice from those currently available..
    Returns a list with the selected dice.

    :param x: List with the available dice
    :return: List with the selected dice
    """
    y = []
    for z in range(3):
        numSorteado = random.randint(0, len(x)-1)
        dadoSelecionado = x[numSorteado]
        if dadoSelecionado == dadoVerde:
            corDado = 'Green'
        elif dadoSelecionado == dadoAmarelo:
            corDado = 'Yellow'
        else:
            corDado = 'Red'
        print("Selected Die " + str(z+1) + ": ", corDado)
        y.append(dadoSelecionado)
        x.remove(dadoSelecionado)
    return y


def sortear_face(x: list, c: int, p: int, t: int):
    """
    Randomly selects the face of each of the selected dice.

    :param x: List of selected dice
    :param c: Current number of brains
    :param p: Current number of footprints
    :param t: Current number of shotguns
    :return: Returns the updated number of brains, footprints, and shotguns
    """
    for dadoSelecionado in x:
        numFace = random.randint(0, 5)
        if dadoSelecionado[numFace] == 'C':
            print("You ate your victim's brain!!")
            c += 1
        elif dadoSelecionado[numFace] == 'P':
            print("Your victim escaped")
            p += 1
        else:
            print("Your victim fought back and you were SHOT!")
            t += 1
    return c, p, t


def placar(x: int, r: int, lj: list, lc: list):
    """
    Displays the scoreboard for the current round.

    :param x: Number of players
    :param r: Round counter, initially set to 0
    :param lj: List of players
    :param lc: List of brains/score of each player at the moment
    :return: Returns and updates the value of the current round
    """
    r += 1
    print("")
    print("Round ", r, " Result!")
    print("")
    print(f'{"Player":^10}|{"Score":^10}')
    for z in range(x):
        print(f'{lj[z]:^10}|{lc[z]:^10}')
    return r


def zerar_marcadores(x: list, y: int, c: int, p: int, t: int):
    """
    Reset the program counters and restart the list of available dice.

    :param x: List of dice
    :param y: Current player
    :param c: Brain counter
    :param p: Footprints counter
    :param t: Shotgun counter
    :return: Reset all counters to zero and reset the list to the initial state, with all possible dice.
    """
    x = [*listaOficial]
    y += 1
    c = 0
    p = 0
    t = 0
    return x, y, c, p, t


def ganhador(x: list, lp: list):
    """
    Show the winners and their final scores.

    :param x: List of winners
    :param lp: List of winners' scores
    """
    print("")
    print("WE HAVE A WINNER!!!!")
    print("")
    print(f'{"Player":^10}|{"Score":^10}')
    for z in range(len(x)):
        print(f'{x[z]:^10}|{lp[z]:^10}')
        print("")
        print("Congratulations ", x[z], " you won!!!")
    print("Thank you for playing ZOMBIE DICE!!!!")
    print("UNTIL NEXT TIME!!!!")


def ganhadores(x: list, lp: list):
    """
    Show the winners if the round ends with more than one player having more than 13 points.

    :param x: List of winners
    :param lp: List of winners' scores
    """
    print("")
    print("WE HAVE MORE THAN ONE PLAYER WITH 13 POINTS!!!")
    print("")
    print(f'{"Player":^10}|{"Score":^10}')
    for z in range(len(x)):
        print(f'{x[z]:^10}|{lp[z]:^10}')
    print("")
    for z in range(len(x)):
        print("Congratulations ", x[z], " on the great game!!!")
    print("")
    print("To handle the tie, start a new game only with the participants with the same score")
    print("Play only one round and see who gets the highest number of points!!")
    print("If the tie persists, start a new game and so on until the tie is solved")
    print("Thank you for playing ZOMBIE DICE!!!!")
    print("UNTIL NEXT TIME!!!!")


def eliminacao():
    """
    Returns an elimination message
    """
    print("You have taken too many shots and are severely injured, so you were ELIMINATED from this round!")


def condicao_de_vitoria(x: int, y: int):
    """
    Adds the name and score of the player with 13 brains to different lists.

    :param x: Victory counter
    :param y: Highest score counter
    :return: Returns the updated victory counter
    """
    listaCerebros[jogadorAtual] += cerebros
    if listaCerebros[jogadorAtual] > y:
        x = 0
        x += 1
        y = listaCerebros[jogadorAtual]
        p = listaCerebros[jogadorAtual]
        listaPontuacao.clear()
        listaPontuacao.append(p)
        v = listaJogadores[jogadorAtual]
        vencedores.clear()
        vencedores.append(v)
        print("Congratulations ", listaJogadores[jogadorAtual], "you have got 13 brains!!!")
        return x, y
    elif listaCerebros[jogadorAtual] == y:
        x += 1
        p = listaCerebros[jogadorAtual]
        listaPontuacao.append(p)
        v = listaJogadores[jogadorAtual]
        vencedores.append(v)
        print("Congratulations ", listaJogadores[jogadorAtual], "you have got 13 brains!!!")
        return x, y
    else:
        print("Congratulations ", listaJogadores[jogadorAtual], "you have got 13 brains!!!")
        return x, y


def continuar():
    x = str(input("Do you wish to continue playing? (yes or no): "))
    if x == 'no' or x == 'No' or x == 'n' or x == 'nO' or x == 'NO':
        return x


# Boas-vindas aos jogadores
print("")
print("================ZOMBIE DICE================\n")
print("Welcome to the ZOMBIE DICE game!!\n")

# Entrada de número de jogadores
numJogadores = numero_de_jogadores()
print("")

# Entrada do nome dos jogadores
listaJogadores = nome_jogadores(numJogadores).copy()

# Criaçao da lista de pontuação
listaCerebros = pontuacao_inicial(numJogadores).copy()

# Criação dos dados
dadoVerde = 'CPCTPC'
dadoAmarelo = 'TPCTPC'
dadoVermelho = 'TPTCPT'
listaOficial = (dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoAmarelo, dadoAmarelo, dadoAmarelo, dadoAmarelo, dadoVermelho, dadoVermelho, dadoVermelho)
listaDados = [*listaOficial]

# Rodada de jogo
while True:
    print("")
    print("Player: ", listaJogadores[jogadorAtual])
    print("")

    # Retornar os dados ao copo caso seja necessário
    if len(listaDados) < 3:
        listaDados = [*listaOficial]
        print("It seems like you're doing great, keep it up!!")
        print("")

    # Mostrar os dados disponíveis no copo
    verdes, amarelos, vermelhos = dados_disponiveis(listaDados)
    print("Available Dice")
    print("")
    print(f'{"Green":<10} {" = "} {verdes:<10}')
    print(f'{"Yellow":<10} {" = "} {amarelos:<10}')
    print(f'{"Red":<10} {" = "} {vermelhos:<10}')

    # Sortear 3 dados
    print("")
    input("Press ENTER to select 3 dice")
    print("")
    dadosSorteados = sortear_dados(listaDados).copy()

    # Sortear as faces dos 3 dados
    print("")
    input("Press ENTER to roll the selected dice")
    print("")
    print("RESULTS")
    print("")
    cerebros, passos, tiros = sortear_face(dadosSorteados, cerebros, passos, tiros)

    # Resultado da rodada atual
    print("")
    print("CURRENT ROUND SCORE")
    print("BRAINS: ", cerebros)
    print("SHOTGUNS: ", tiros)
    print("")

    # Conferir se o jogador tomou 3 tiros e está eliminado desta rodada
    if tiros >= 3:
        eliminacao()
        listaDados, jogadorAtual, cerebros, passos, tiros = zerar_marcadores(listaDados, jogadorAtual, cerebros, passos, tiros)
        if jogadorAtual == numJogadores:
            rodada = placar(numJogadores, rodada, listaJogadores, listaCerebros)
            if vitoria == 1:
                ganhador(vencedores, listaPontuacao)
                input("Press ENTER to close the game")
                break
            elif vitoria > 1:
                ganhadores(vencedores, listaPontuacao)
                input("Press ENTER to close the game")
                break
            jogadorAtual = 0
            print("")
            input("Press ENTER to start next round")
            continue
        else:
            print("")
            print("NEXT PLAYER!")
            continue

    # Verificar a condição de vitória
    if listaCerebros[jogadorAtual] + cerebros >= 13:
        vitoria, maior = condicao_de_vitoria(vitoria, maior)
        if jogadorAtual != (numJogadores-1):
            print("Let's finish this round and see who the winner is....")
        listaDados, jogadorAtual, cerebros, passos, tiros = zerar_marcadores(listaDados, jogadorAtual, cerebros, passos, tiros)
        if jogadorAtual == numJogadores:
            rodada = placar(numJogadores, rodada, listaJogadores, listaCerebros)
            if vitoria == 1:
                ganhador(vencedores, listaPontuacao)
                input("Press ENTER to close the game")
                break
            elif vitoria > 1:
                ganhadores(vencedores, listaPontuacao)
                input("Press ENTER to close the game")
                break
            jogadorAtual = 0
            print("")
            input("Press ENTER to start next round")
            continue
        print("")
        print("NEXT PLAYER!")
        continue

    # Verificar se o usuário deseja continuar jogando
    continua = continuar()
    if continua == 'no' or continua == 'NO' or continua == 'n' or continua == 'nO' or continua == 'No':

        # Contabilizar os cérebros do jogador
        listaCerebros[jogadorAtual] += cerebros

        # Zerar os contadores do jogo e retornar todos os dados ao copo
        listaDados, jogadorAtual, cerebros, passos, tiros = zerar_marcadores(listaDados, jogadorAtual, cerebros, passos, tiros)

        # Iniciar a próxima rodada de jogo
        if jogadorAtual == numJogadores:
            rodada = placar(numJogadores, rodada, listaJogadores, listaCerebros)
            if vitoria == 1:
                ganhador(vencedores, listaPontuacao)
                input("Press ENTER to close the game")
                break
            elif vitoria > 1:
                ganhadores(vencedores, listaPontuacao)
                input("Press ENTER to close the game")
                break
            jogadorAtual = 0
            print("")
            input("Press ENTER to start next round")
            continue

        print("")
        print("NEXT PLAYER!")

    # Continuar a rodada do mesmo jogador
    else:
        print("")
        print("Starting another round for the current player...")


