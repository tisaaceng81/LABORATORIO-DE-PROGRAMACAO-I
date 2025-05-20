import random
from collections import defaultdict

def similar_pair(n, k, arestas): 
    arvore = {}
    for a, b in arestas:
        if a not in arvore:
            arvore[a] = []
        arvore[a].append(b)

    contador = 0
    caminho = []

    def dfs(no):
        nonlocal contador
        for ancestral in caminho:
            if abs(ancestral - no) <= k:
                contador += 1
        caminho.append(no)
        for filho in arvore.get(no, []):
            dfs(filho)
        caminho.pop()

    filhos = set(b for a, b in arestas)
    todos = set(a for a, b in arestas) | filhos
    raiz = list(todos - filhos)[0]
    dfs(raiz)
    return contador

def gerarTesteAleatorioComParametros(n, k):
    nos = list(range(2, n + 1))
    random.shuffle(nos)
    arestas = []
    for i in range(n - 1):
        a = random.randint(1, i + 1)
        b = nos[i]
        arestas.append((a, b))
    return (n, k, arestas)

def exibir_arvore_formatada(arestas):
    filhos = defaultdict(list)
    todos_nos = set()
    tem_pai = set()

    for a, b in arestas:
        filhos[a].append(b)
        todos_nos.update([a, b])
        tem_pai.add(b)

    raiz = list(todos_nos - tem_pai)
    if not raiz:
        print("Não foi possível determinar a raiz.")
        return
    raiz = raiz[0]

    for no in filhos:
        filhos[no].sort()

    def desenhar(no, prefixo="", eh_ultimo=True):
        conector = "└── " if eh_ultimo else "├── "
        print(prefixo + conector + str(no))
        novo_prefixo = prefixo + ("    " if eh_ultimo else "│   ")
        filhos_no = filhos.get(no, [])
        for i, filho in enumerate(filhos_no):
            desenhar(filho, novo_prefixo, i == len(filhos_no) - 1)

    print()
    desenhar(raiz)

def generateTestCases():
    print("Digite n e k separados por espaço:")
    n, k = map(int, input().split())

    if n < 1:
        print("n deve ser pelo menos 1")
        return []

    print("Deseja gerar as arestas aleatoriamente? (s/n):")
    escolha = input().strip().lower()

    if escolha == 's':
        return [gerarTesteAleatorioComParametros(n, k)]
    else:
        print(f"Digite {n - 1} arestas no formato 'a b':")
        arestas = []
        for _ in range(n - 1):
            a, b = map(int, input().split())
            arestas.append((a, b))
        return [(n, k, arestas)]

def main():
    testCases = generateTestCases()
    if not testCases:
        return

    for idx, (n, k, arestas) in enumerate(testCases, 1):
        print(f"\n Teste {idx}")
        print(f"n = {n}, k = {k}")
        print("Arestas:", arestas)

        print("\n Estrutura da Árvore:")
        exibir_arvore_formatada(arestas)

        resultado = similar_pair(n, k, arestas)
        print(f"\n➡ Resultado: {resultado}")

if __name__ == "__main__":
    main()




