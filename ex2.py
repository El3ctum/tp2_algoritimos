## Comparação entre Complexidade de Tempo e Espaço ##

"""
Mestre, caso não seja pedir muito, gostaria de saber qual das duas implementaçẽos faz mais sentido!

Se tem alguma mudança na performance ou qualidade de leitura de código.
"""

import time


class OrderList:
    def __init__(self, aList: list):
        self.unordered_list = aList

    def merge_sort(self):
        if len(self.unordered_list) <= 1:
            return self.unordered_list

        # Halving the list
        mid = len(self.unordered_list) // 2
        left_side = OrderList(self.unordered_list[:mid]).merge_sort()
        right_side = OrderList(self.unordered_list[mid:]).merge_sort()

        # Grouping the sides again
        return self.__merge(left_side, right_side)

    def __merge(self, left_side, right_side):
        sorted_list = []
        i, j = 0, 0

        # Grouping the ordered lists
        while i < len(left_side) and j < len(right_side):
            if left_side[i] < right_side[j]:
                sorted_list.append(left_side[i])
                i += 1
            else:
                sorted_list.append(right_side[j])
                j += 1

        # Appending the final elements

        sorted_list.extend(left_side[i:])
        sorted_list.extend(right_side[j:])

        return sorted_list

# Using functions


def merge_sort(aList):
    if len(aList) <= 1:
        return aList

    # Halving the list
    mid = len(aList) // 2
    left_side = merge_sort(aList[:mid])
    right_side = merge_sort(aList[mid:])

    # Merging the sorted halves
    return merge(left_side, right_side)


def merge(left_side, right_side):
    sorted_list = []
    i, j = 0, 0

    # Merging the ordered lists
    while i < len(left_side) and j < len(right_side):
        if left_side[i] < right_side[j]:
            sorted_list.append(left_side[i])
            i += 1
        else:
            sorted_list.append(right_side[j])
            j += 1

    # Appending any remaining elements
    sorted_list.extend(left_side[i:])
    sorted_list.extend(right_side[j:])

    return sorted_list


if __name__ == "__main__":
    import random

    test_registers = [random.randint(0, 10000000) for _ in range(5000000)]
    # start_time = time.time()
    # ordered_list = merge_sort(test_registers)
    # end_time = time.time()

    start_time = time.time()
    ordered_list = OrderList(test_registers).merge_sort()
    end_time = time.time()
    
    total_time = end_time - start_time    
    print(total_time)
