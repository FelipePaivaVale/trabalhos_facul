def mochila_gulosa(capacidade, pesos, valores):

    indice = [i for i in range(len(pesos))]
    
    # cria lista de tuplas (peso, valor e indice)
    caixas = [(p, v, i) for p, v, i in zip(pesos, valores, indice)]
    
    # ordena a lista em ordem decrescente pelo valor/peso
    caixas.sort(key=lambda x: x[1]/x[0], reverse=True)
    
    # inicializa a mochila e soma_pesos
    mochila = []
    soma_pesos = 0
    
    # loop sobre cada caixa
    for caixa in caixas:
        # verifica se adiciona a caixa na mochila
        if soma_pesos + caixa[0] <= capacidade:
            mochila.append(caixa)
            soma_pesos += caixa[0]
    
    # retorna as caixas escolhidas
    return mochila

pesos = [200, 250, 450, 100, 300, 200, 400, 100, 50, 350, 250, 450, 50, 400, 100, 350, 200, 300, 200, 150]
valores = [7, 9, 4, 12, 10, 2, 13, 1, 7, 8, 11, 13, 6, 4, 10, 1, 6, 2, 7, 8]
capacidade = int(input("Qual o tamanho da mochila?"))

mochila = mochila_gulosa(capacidade, pesos, valores)

print(mochila)