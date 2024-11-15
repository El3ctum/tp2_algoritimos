## Contando Pedidos Ímpares na Pilha ##

import time


def count_odd(aQueue: int) -> int:
    qtd_odd = 0

    for i in range(len(aQueue) - 1, -1, -1):
        if (aQueue[i] % 2) != 0:
            qtd_odd += 1

    return qtd_odd


if __name__ == "__main__":
    import random

    test_registers = [random.randint(0, 10) for _ in range(50)]
    start_time = time.time()
    qtd_odds = count_odd(test_registers)
    end_time = time.time()

    total_time = end_time - start_time
    print(total_time)
    print(test_registers)
    print(qtd_odds)
