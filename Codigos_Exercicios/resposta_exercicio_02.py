import random

def insertionSort(arr):
    deslocamentos = 0
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > chave:
            arr[j + 1] = arr[j]
            j -= 1
            deslocamentos += 1
        arr[j + 1] = chave
    return deslocamentos

def insertionSortDetalhado(L):
    deslocamentos = 0
    for i in range(1, len(L)):
        k = i
        while k > 0 and L[k] < L[k-1]:
            print(f"Comparando {L[k]} e {L[k-1]} -> trocando")
            L[k], L[k-1] = L[k-1], L[k]
            print(f"Vetor atual: {L}")
            print("-" * 50)
            k -= 1
            deslocamentos += 1
            print(f"Deslocamento {deslocamentos}: {L}")
        if k > 0:
            print(f"Comparando {L[k]} e {L[k-1]} -> não troca")
            print("-" * 50)
    return deslocamentos

def generate_random_array(size, min_val=1, max_val=100):
    return [random.randint(min_val, max_val) for _ in range(size)]

def main():
    modo = input("Escolha o modo:\n1 - Simples\n2 - Detalhado\nDigite 1 ou 2: ")
    if modo == "1":
        arr = generate_random_array(10)
        print("Array de entrada:", arr)
        deslocamentos = insertionSort(arr)
        print("Array ordenado:", arr)
        print("Deslocamentos realizados:", deslocamentos)
    elif modo == "2":
        a = int(input("Digite o valor mínimo do intervalo: "))
        b = int(input("Digite o valor máximo do intervalo: "))
        n = int(input("Digite o número de elementos do vetor: "))
        # Gera vetor aleatório sem repetição entre a e b
        X = random.sample(range(a, b), n)
        print('Vetor não ordenado:')
        print(X)
        print()
        deslocamentos = insertionSortDetalhado(X)
        print('Vetor ordenado:')
        print(X)
        print()
        print(f'Número total de deslocamentos: {deslocamentos}')
    else:
        print("Modo inválido. Execute o programa novamente e escolha 1 ou 2.")

if __name__ == "__main__":
    main()
