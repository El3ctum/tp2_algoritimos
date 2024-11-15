## Contando Livros com Números Ímpares ##

import time


def count_odd_books(aQueue: int) -> int:
    qtd_odd_books = 0

    for i in range(len(aQueue) - 1, -1, -1):
        if (aQueue[i] % 2) != 0:
            qtd_odd_books += 1

    return qtd_odd_books


if __name__ == "__main__":
    import random

    test_registers = [random.randint(0, 15) for _ in range(10)]
    start_time = time.time()
    qtd_odd_books = count_odd_books(test_registers)
    end_time = time.time()

    total_time = end_time - start_time
    print(total_time)
    print(test_registers)
    print(qtd_odd_books)
