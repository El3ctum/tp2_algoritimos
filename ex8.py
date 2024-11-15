## Invertendo a Ordem de uma Fila ##

import time


def invert_queue(aQueue):
    """ A construção desse função se deu baseada na simples inversão das posições das fila,
    utilizei a variavel 'half_queue' para limitar até onde a inversão vai, pois não é
    possivel inverter a posição de alguém que está no meio da fila.
    """

    aQueue = aQueue.copy()

    half_queue = len(aQueue) // 2
    start = 0
    end = len(aQueue) - 1

    while start < half_queue:
        aQueue[start], aQueue[end] = aQueue[end], aQueue[start]

        start += 1
        end -= 1

    return aQueue


if __name__ == "__main__":
    import random

    test_registers = [random.randint(0, 10) for _ in range(4)]
    start_time = time.time()
    inverted_queue = invert_queue(test_registers)
    end_time = time.time()

    total_time = end_time - start_time
    print(total_time)
    print(test_registers)
    print(inverted_queue)
