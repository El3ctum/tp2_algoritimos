## Priorizar Tempo ou Espaço? ##


import time


def brute_force(aList: list):
    duplicated_numbers = set()

    for i in range(len(aList)):
        for j in range(i + 1, len(aList)):
            if aList[i] == aList[j]:
                duplicated_numbers.add(aList[i])

    return duplicated_numbers


def best_option(aList: list):
    """
        A escolha do seguinte algoritmo foi feita baseada no meu conhecimento de python, talvez sendo implementada diferente
        se for escolhida uma outra linguagem.

        A escolha da utilização de "set()" na construção da função se deve pelo fato de a propria estrutura oferecer a filtragem
        de dados duplicados de forma eficiente, o que faz com que eu possa implementar uma solução O(n) para um problema que em
        teoria precisaria de algo como O(n^2) com foi implementado na brute_force. Tudo porque ao passar por cada número da lista
        eu já faço a comparação nos sets, quem tem acesso O(1), não atrapalhando assim a execução do loop.
    """
    first_values = set()
    duplicated_numbers = set()

    for data in aList:
        if data in first_values:
            duplicated_numbers.add(data)
        else:
            first_values.add(data)

    return duplicated_numbers


if __name__ == "__main__":
    import random

    test_registers = [random.randint(0, 10000000) for _ in range(5000000)]
    start_time = time.time()
    brute_force = brute_force(test_registers)
    end_time = time.time()

    # start_time = time.time()
    # best_option = best_option(test_registers)
    # end_time = time.time()

    total_time = end_time - start_time
    print(total_time)
