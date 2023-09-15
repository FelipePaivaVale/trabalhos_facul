from collections import deque

def busca_peso(grafo, inicio, fim):
    visitados = set()
    fila = deque([(inicio, [inicio], 0)])

    while fila:
        atual, caminho, peso_total = fila.popleft()
        visitados.add(atual)

        if atual == fim:
            return caminho, peso_total

        for ver, peso in grafo.get(atual, {}).items():
            if ver not in visitados:
                fila.append((ver, caminho + [ver], peso_total + peso))

    return None, None

def busca(proximo, v):
    if proximo[v] != v:
        proximo[v] = busca(proximo, proximo[v])
    return proximo[v]

def juntar(proximo, alt, v1, v2):
    r1 = busca(proximo, v1)
    r2 = busca(proximo, v2)

    if alt[r1] > alt[r2]:
        proximo[r2] = r1
    elif alt[r1] < alt[r2]:
        proximo[r1] = r2
    else:
        proximo[r2] = r1
        alt[r1] += 1

def kruskal(grafo):
    arestas = []
    for v in grafo:
        for ver, peso in grafo[v].items():
            arestas.append((peso, v, ver))
    arestas.sort()
    agn = {}
    proximo = {v: v for v in grafo}
    alt = {v: 0 for v in grafo}

    def busca(v):
        if proximo[v] != v:
            proximo[v] = busca(proximo[v])
        return proximo[v]

    def juntar(v1, v2):
        r1 = busca(v1)
        r2 = busca(v2)

        if alt[r1] > alt[r2]:
            proximo[r2] = r1
        elif alt[r1] < alt[r2]:
            proximo[r1] = r2
        else:
            proximo[r2] = r1
            alt[r1] += 1

    for peso, v1, v2 in arestas:
        if busca(v1) != busca(v2):
            juntar(v1, v2)
            agn.setdefault(v1, {})[v2] = peso
            agn.setdefault(v2, {})[v1] = peso
    return agn

if __name__ == "__main__":
    grafo_com_dados = {
        1: {2: 220, 3: 255, 10: 460},
        2: {1: 220, 3: 105, 6: 240, 10: 360, 16: 510},
        3: {1: 255, 2: 105, 4: 130, 6: 165},
        4: {3: 130, 5: 240, 6: 180, 7: 195, 9: 315, 12: 340},
        5: {4: 240, 8: 300, 9: 310},
        6: {2: 240, 3: 165, 4: 180, 7: 165, 10: 360, 12: 285, 14: 285},
        7: {4: 195, 6: 165, 9: 225, 13: 255},
        8: {5: 300, 9: 330, 11: 225},
        9: {4: 315, 5: 310, 7: 225, 8: 330, 10: 505, 12: 255, 15: 220, 18: 360},
        10: {1: 460, 2: 360, 6: 360, 9: 505, 12: 280, 16: 200},
        11: {8: 225, 13: 330, 15: 210, 19: 270},
        12: {4: 340, 6: 285, 9: 255, 10: 280, 13: 150, 14: 70, 18: 200, 20: 270, 27: 585},
        13: {7: 255, 11: 330, 12: 150, 15: 195, 18: 210},
        14: {6: 285, 12: 70, 16: 255, 17: 195, 21: 300},
        15: {9: 220, 11: 210, 13: 195, 16: 590, 18: 230, 19: 105},
        16: {16: 510, 10: 200, 14: 255, 15: 590, 17: 110, 22: 190},
        17: {14: 195, 16: 110, 18: 275, 22: 170},
        18: {9: 360, 12: 200, 13: 230, 15: 230, 17: 275, 19: 195, 20: 170, 23: 210, 24: 345},
        19: {11: 270, 15: 105, 18: 195, 23: 360, 26: 345},
        20: {12: 270, 18: 170, 21: 165, 23: 120, 30: 465},
        21: {14: 300, 20: 165, 22: 160, 31: 390},
        22: {16: 190, 17: 170, 21: 160, 23: 375, 25: 190},
        23: {19: 360, 20: 120, 22: 375, 24: 150, 25: 340, 30: 360},
        24: {18: 345, 23: 150, 26: 150, 28: 260, 29: 255},
        25: {22: 190, 23: 340, 31: 360},
        26: {19: 345, 24: 150, 27: 360, 28: 175, 29: 285},
        27: {12: 585, 26: 360, 31: 210},
        28: {24: 260, 26: 175, 32: 260, 33: 230},
        29: {24: 255, 26: 285, 30: 150, 32: 255, 34: 435},
        30: {20: 465, 23: 360, 29: 150, 31: 180, 34: 435, 35: 480},
        31: {21: 390, 25: 360, 27: 210, 30: 180, 34: 580, 35: 420},
        32: {28: 260, 29: 255, 33: 75, 34: 330},
        33: {28: 230, 32: 75, 34: 300, 36: 185},
        34: {29: 435, 30: 435, 31: 580, 32: 330, 33: 300, 35: 300, 36: 260, 37: 320},
        35: {30: 480, 31: 420, 34: 300, 37: 180},
        36: {33: 185, 34: 260,37: 450, 38: 260},
        37: {34: 320, 35: 180, 36: 450, 39: 480},
        38: {36: 260, 39: 330, 40: 110},
        39: {37: 480, 38: 330, 40: 150},
        40: {39: 150, 38: 110}
    }
    primeiro = 1
    ultimo = 40

    caminho, peso_total = busca_peso(grafo_com_dados, primeiro, ultimo)
    if caminho:
        print(f"Caminho do vértice {primeiro} ao vértice {ultimo}:")
        print(" -> ".join(map(str, caminho)))
        print(f"Peso total da rota: {peso_total}")
    else:
        print(f"Não foi possível encontrar um caminho do vértice {primeiro} ao vértice {ultimo}.")

    agn = kruskal(grafo_com_dados)
    print("\nÁrvore Geradora Mínima - Kruskal:")
    for v in agn:
        for ver, peso in agn[v].items():
            print(f"{v} -- {ver} : {peso}")