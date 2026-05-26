# lista de itens
itens = [
    ("lanterna", 2, 6),
    ("barraca", 4, 10),
    ("faca", 1, 3),
    ("cobertor", 3, 7),
    ("cantil", 2, 5),
    ("mapa", 1, 4),
    ("corda", 5, 9)
]



# versao a - recursao ingenua


def mochila_recursiva(indice, capacidade):
    # caso base
    if indice == 0 or capacidade == 0:
        return 0

    nome, peso, valor = itens[indice - 1]

    # se o item nao cabe na mochila
    if peso > capacidade:
        return mochila_recursiva(indice - 1, capacidade)

    # escolhe o melhor entre pegar ou nao pegar o item
    sem_item = mochila_recursiva(indice - 1, capacidade)

    com_item = valor + mochila_recursiva(
        indice - 1,
        capacidade - peso
    )

    return max(sem_item, com_item)


def reconstruir_recursiva(capacidade):
    itens_escolhidos = []
    peso_total = 0

    i = len(itens)
    w = capacidade

    while i > 0 and w > 0:
        atual = mochila_recursiva(i, w)
        anterior = mochila_recursiva(i - 1, w)

        # verifica se o item foi escolhido
        if atual != anterior:
            nome, peso, valor = itens[i - 1]
            itens_escolhidos.append(nome)
            peso_total += peso
            w -= peso

        i -= 1

    return itens_escolhidos[::-1], peso_total



# versao b - top-down com memoizacao


memo = {}


def mochila_memo(indice, capacidade):
    # verifica se ja foi calculado
    if (indice, capacidade) in memo:
        return memo[(indice, capacidade)]

    # caso base
    if indice == 0 or capacidade == 0:
        return 0

    nome, peso, valor = itens[indice - 1]

    # se o item nao cabe
    if peso > capacidade:
        resultado = mochila_memo(indice - 1, capacidade)

    else:
        sem_item = mochila_memo(indice - 1, capacidade)

        com_item = valor + mochila_memo(
            indice - 1,
            capacidade - peso
        )

        resultado = max(sem_item, com_item)

    # salva no memo
    memo[(indice, capacidade)] = resultado

    return resultado


def reconstruir_memo(capacidade):
    itens_escolhidos = []
    peso_total = 0

    i = len(itens)
    w = capacidade

    while i > 0 and w > 0:
        atual = mochila_memo(i, w)
        anterior = mochila_memo(i - 1, w)

        # verifica se o item foi usado
        if atual != anterior:
            nome, peso, valor = itens[i - 1]
            itens_escolhidos.append(nome)
            peso_total += peso
            w -= peso

        i -= 1

    return itens_escolhidos[::-1], peso_total



# versao c - bottom-up com tabulacao


def mochila_bottom_up(capacidade):
    n = len(itens)

    # cria tabela
    tabela = [[0 for _ in range(capacidade + 1)]
              for _ in range(n + 1)]

    # preenche a tabela
    for i in range(1, n + 1):
        nome, peso, valor = itens[i - 1]

        for w in range(capacidade + 1):

            # se o item nao cabe
            if peso > w:
                tabela[i][w] = tabela[i - 1][w]

            else:
                sem_item = tabela[i - 1][w]

                com_item = valor + tabela[i - 1][w - peso]

                tabela[i][w] = max(sem_item, com_item)

    # reconstrucao dos itens escolhidos
    itens_escolhidos = []
    peso_total = 0

    w = capacidade

    for i in range(n, 0, -1):
        if tabela[i][w] != tabela[i - 1][w]:
            nome, peso, valor = itens[i - 1]

            itens_escolhidos.append(nome)
            peso_total += peso
            w -= peso

    itens_escolhidos.reverse()

    return tabela[n][capacidade], itens_escolhidos, peso_total



# funcao de testes


def executar_testes(capacidade):
    print(f"capacidade da mochila: {capacidade}")
   

    # versao recursiva
    valor_a = mochila_recursiva(len(itens), capacidade)
    escolhidos_a, peso_a = reconstruir_recursiva(capacidade)

    print("\nversao a - recursao ingenua")
    print("valor maximo:", valor_a)
    print("itens escolhidos:", escolhidos_a)
    print("peso total:", peso_a)

    # limpa memo antes do teste
    global memo
    memo = {}

    # versao memoizacao
    valor_b = mochila_memo(len(itens), capacidade)
    escolhidos_b, peso_b = reconstruir_memo(capacidade)

    print("\nversao b - top-down com memoizacao")
    print("valor maximo:", valor_b)
    print("itens escolhidos:", escolhidos_b)
    print("peso total:", peso_b)

    # versao bottom-up
    valor_c, escolhidos_c, peso_c = mochila_bottom_up(capacidade)

    print("\nversao c - bottom-up com tabulacao")
    print("valor maximo:", valor_c)
    print("itens escolhidos:", escolhidos_c)
    print("peso total:", peso_c)


# testes
executar_testes(6)
executar_testes(10)
executar_testes(15)
