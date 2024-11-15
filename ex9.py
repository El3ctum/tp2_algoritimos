##  Ordenando uma Lista sem Funções Prontas ##

import time


def first_sort(aList: list):
    numbers = aList.copy()
    for i in range(len(numbers)):
        for j in range(len(numbers)-1-i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers


if __name__ == "__main__":
    import random

    test_registers = [random.randint(0, 10) for _ in range(10)]
    start_time = time.time()
    sorted_numbers = first_sort(test_registers)
    end_time = time.time()

    total_time = end_time - start_time
    print(total_time)
    print(test_registers)
    print(sorted_numbers)
