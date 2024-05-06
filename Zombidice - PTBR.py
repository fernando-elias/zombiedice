'''
Pontifícia Universidade Católica do Paraná
Curso: Análise e Desenvolvimento de Sistemas
Aluno: Fernando Doszanet Elias

Projeto Final

Projeto iniciado em: 04/03/2022
Última modificação em: 17/04/2022
'''

# Criação dos contadores de jogo e importação de bibliotecas
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


# Criação das funções utilizadas no jogo
def numero_de_jogadores():
    """
    Pede ao usuário o número de jogadores desta partida.

    :return: Número de jogadores
    """
    x = 0
    while x < 2:
        try:
            x = int(input("Informe o número de jogadores: "))
            if x < 2:
                print("Você precisa de pelo menos 2 jogadores!")
        except ValueError:
            print("Valor inválido")
    return x


def nome_jogadores(x: int):
    """
    Recebe o número de jogadores e pede o nome destes jogadores, retornando uma lista.

    :param x: Número de jogadores
    :return: Lista com o nome dos jogadores
    """
    listaX = []
    z = 0
    while z < x:
        y = input("Insira agora o nome do jogador " + str(z + 1) + ": ")
        listaX.append(y)
        z += 1
    return listaX


def pontuacao_inicial(x: int):
    """
    Cria uma lista com a pontuação inicial de cada jogador.

    :param x: Número de jogadores
    :return: lista com a pontuação inicial 0 para cada jogador
    """
    listaX = []
    for z in range(x):
        listaX.append(0)
    return listaX


def dados_disponiveis(x: list):
    """
    Calcula o número de dados disponivéis em cada jogada.

    :param x: Lista com os dados disponíveis
    :return: Retorna respectivamente o número de dados verdes, amarelos e vermelhos neste momento.
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
    Sorteia de forma aleatória 3 dados dentre os disponivéis no momento.
    Retorna uma lista com os dados selecionados.

    :param x: Lista com os dados disponíveis
    :return: Lista com os dados selecionados
    """
    y = []
    for z in range(3):
        numSorteado = random.randint(0, len(x)-1)
        dadoSelecionado = x[numSorteado]
        if dadoSelecionado == dadoVerde:
            corDado = 'Verde'
        elif dadoSelecionado == dadoAmarelo:
            corDado = 'Amarelo'
        else:
            corDado = 'Vermelho'
        print("Dado Sorteado " + str(z+1) + ": ", corDado)
        y.append(dadoSelecionado)
        x.remove(dadoSelecionado)
    return y


def sortear_face(x: list, c: int, p: int, t: int):
    """
    Sorteia de forma aleatória a face de cada um dos dados selecionados.

    :param x: Lista de dados selecionados
    :param c: Número atual de cérebros
    :param p: Número atual de passos
    :param t: Número atual de tiros
    :return: Retorna o número atualizado de cérebros, passos e tiros
    """
    for dadoSelecionado in x:
        numFace = random.randint(0, 5)
        if dadoSelecionado[numFace] == 'C':
            print("Você comeu um cérebro!!")
            c += 1
        elif dadoSelecionado[numFace] == 'P':
            print("A vítima escapou!!")
            p += 1
        else:
            print("Você tomou um tiro!!")
            t += 1
    return c, p, t


def placar(x: int, r: int, lj: list, lc: list):
    """
    Mostra o placar da rodada atual.

    :param x: Número de jogadores
    :param r: Contador de rodada, inicialmente 0
    :param lj: Lista de jogadores
    :param lc: Lista de cérebros/ pontuação de cada jogador no momento
    :return: Retorna e atualiza o valor da rodada atual
    """
    r += 1
    print("")
    print("Resultado da ", r, "Rodada!")
    print("")
    print(f'{"Jogador":^10}|{"Pontos":^10}')
    for z in range(x):
        print(f'{lj[z]:^10}|{lc[z]:^10}')
    return r


def zerar_marcadores(x: list, y: int, c: int, p: int, t: int):
    """
    Zera os contadores do programa e reinicia a lista de dados disponíveis.

    :param x: Lista de dados
    :param y: Jogador atual
    :param c: Contador de cérebros
    :param p: Contador de passos
    :param t: Contador de tiros
    :return: Retorna todos os contadores zerados e a lista para o padrão inicial, com todos os dados possíveis.
    """
    x = [*listaOficial]
    y += 1
    c = 0
    p = 0
    t = 0
    return x, y, c, p, t


def ganhador(x: list, lp: list):
    """
    Mostra o ganhador e a sua pontuação final.

    :param x: Lista de vencedores
    :param lp: Lista de pontuação dos vencedores
    """
    print("")
    print("TEMOS UM VENCEDOR!!!")
    print("")
    print(f'{"Jogador":^10}|{"Pontos":^10}')
    for z in range(len(x)):
        print(f'{x[z]:^10}|{lp[z]:^10}')
        print("")
        print("Parabéns ", x[z], " você venceu!!!")
    print("Obrigado por jogarem ZOMBIE DICE!!!!")
    print("ATÉ A PROXIMA!!!!")


def ganhadores(x: list, lp: list):
    """
    Mostra os ganhadores, em caso de término da rodada com mais de um jogador com mais de 13 pontos.

    :param x: Lista de vencedores
    :param lp: Lista de pontuação de vencedores
    """
    print("")
    print("TEMOS MAIS DE UM JOGADOR COM 13 PONTOS!!!")
    print("")
    print(f'{"Jogador":^10}|{"Pontos":^10}')
    for z in range(len(x)):
        print(f'{x[z]:^10}|{lp[z]:^10}')
    print("")
    for z in range(len(x)):
        print("Parabéns ", x[z], " pela grande partida!!!")
    print("")
    print("Para o resolver o desempate iniciem uma nova partida somente com os participantes com a mesma pontuação")
    print("Joguem apenas uma rodada e vejam quem obtem o maior número de pontos!!")
    print("Caso o empate persista iniciem uma nova partida e assim por diante até que o empate seja resolvido")
    print("Obrigado por jogarem ZOMBIE DICE!!!!")
    print("ATÉ A PROXIMA!!!!")


def eliminacao():
    """
    Retorna uma mensagem de eliminação
    """
    print("Você tomou muitos tiros e está gravemente ferido, portanto está ELIMINADO desta rodada!")


def condicao_de_vitoria(x: int, y: int):
    """
    Acrescenta o nome e a pontuação do jogador com 13 cérebros em listas distintas.

    :param x: Contador de vitória
    :param y: Contador da maior pontuação
    :return: Retorna o contador de vitória atualizado.
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
        print("Parabéns ", listaJogadores[jogadorAtual], "você conseguiu 13 cérebros!!!")
        return x, y
    elif listaCerebros[jogadorAtual] == y:
        x += 1
        p = listaCerebros[jogadorAtual]
        listaPontuacao.append(p)
        v = listaJogadores[jogadorAtual]
        vencedores.append(v)
        print("Parabéns ", listaJogadores[jogadorAtual], "você conseguiu 13 cérebros!!!")
        return x, y
    else:
        print("Parabéns ", listaJogadores[jogadorAtual], "você conseguiu 13 cérebros!!!")
        return x, y


def continuar():
    x = str(input("Deseja continuar jogando? (sim ou não): "))
    if x == 'não' or x == 'nao' or x == 'n':
        return x


# Boas-vindas aos jogadores
print("")
print("================ZOMBIE DICE================\n")
print("Seja muito bem-vindo ao jogo ZOMBIE DICE!!\n")

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
    print("Turno do Jogador: ", listaJogadores[jogadorAtual])
    print("")

    # Retornar os dados ao copo caso seja necessário
    if len(listaDados) < 3:
        listaDados = [*listaOficial]
        print("Parece que você está indo muito bem, continue assim!!")
        print("")

    # Mostrar os dados disponíveis no copo
    verdes, amarelos, vermelhos = dados_disponiveis(listaDados)
    print("Dados Disponíveis")
    print("")
    print(f'{"Verdes":<10} {" = "} {verdes:<10}')
    print(f'{"Amarelos":<10} {" = "} {amarelos:<10}')
    print(f'{"Vermelhos":<10} {" = "} {vermelhos:<10}')

    # Sortear 3 dados
    print("")
    input("Pressione ENTER para sortear 3 dados")
    print("")
    dadosSorteados = sortear_dados(listaDados).copy()

    # Sortear as faces dos 3 dados
    print("")
    input("Pressione ENTER para rolar os dados sorteados")
    print("")
    print("RESULTADOS")
    print("")
    cerebros, passos, tiros = sortear_face(dadosSorteados, cerebros, passos, tiros)

    # Resultado da rodada atual
    print("")
    print("SCORE DA RODADA ATUAL")
    print("CÉREBROS: ", cerebros)
    print("TIROS: ", tiros)
    print("")

    # Conferir se o jogador tomou 3 tiros e está eliminado desta rodada
    if tiros >= 3:
        eliminacao()
        listaDados, jogadorAtual, cerebros, passos, tiros = zerar_marcadores(listaDados, jogadorAtual, cerebros, passos, tiros)
        if jogadorAtual == numJogadores:
            rodada = placar(numJogadores, rodada, listaJogadores, listaCerebros)
            if vitoria == 1:
                ganhador(vencedores, listaPontuacao)
                input("Pressione ENTER para fechar o jogo")
                break
            elif vitoria > 1:
                ganhadores(vencedores, listaPontuacao)
                input("Pressione ENTER para fechar o jogo")
                break
            jogadorAtual = 0
            print("")
            input("Pressione ENTER para iniciar a próxima rodada")
            continue
        else:
            print("")
            print("PRÓXIMO JOGADOR(A)!")
            continue

    # Verificar a condição de vitória
    if listaCerebros[jogadorAtual] + cerebros >= 13:
        vitoria, maior = condicao_de_vitoria(vitoria, maior)
        if jogadorAtual != (numJogadores-1):
            print("Vamos terminar essa rodada e ver quem é o(a) vencedor(a).....")
        listaDados, jogadorAtual, cerebros, passos, tiros = zerar_marcadores(listaDados, jogadorAtual, cerebros, passos, tiros)
        if jogadorAtual == numJogadores:
            rodada = placar(numJogadores, rodada, listaJogadores, listaCerebros)
            if vitoria == 1:
                ganhador(vencedores, listaPontuacao)
                input("Pressione ENTER para fechar o jogo")
                break
            elif vitoria > 1:
                ganhadores(vencedores, listaPontuacao)
                input("Pressione ENTER para fechar o jogo")
                break
            jogadorAtual = 0
            print("")
            input("Pressione ENTER para iniciar a próxima rodada")
            continue
        print("")
        print("PRÓXIMO JOGADOR(A)!")
        continue

    # Verificar se o usuário deseja continuar jogando
    continua = continuar()
    if continua == 'não' or continua == 'nao' or continua == 'n':

        # Contabilizar os cérebros do jogador
        listaCerebros[jogadorAtual] += cerebros

        # Zerar os contadores do jogo e retornar todos os dados ao copo
        listaDados, jogadorAtual, cerebros, passos, tiros = zerar_marcadores(listaDados, jogadorAtual, cerebros, passos, tiros)

        # Iniciar a próxima rodada de jogo
        if jogadorAtual == numJogadores:
            rodada = placar(numJogadores, rodada, listaJogadores, listaCerebros)
            if vitoria == 1:
                ganhador(vencedores, listaPontuacao)
                input("Pressione ENTER para fechar o jogo")
                break
            elif vitoria > 1:
                ganhadores(vencedores, listaPontuacao)
                input("Pressione ENTER para fechar o jogo")
                break
            jogadorAtual = 0
            print("")
            input("Pressione ENTER para iniciar a próxima rodada")
            continue

        print("")
        print("PRÓXIMO JOGADOR(A)!")

    # Continuar a rodada do mesmo jogador
    else:
        print("")
        print("Iniciando mais uma rodada do(a) jogador(a) atual...")


