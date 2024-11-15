##  Ordenando uma Pilha em Ordem Crescente ##


import time

"""separei a atividade em duas partes, pois na minha concepção fica mais organizado e mais performatico. Pois a primeira vez
    a necessidade de ordenação é maior e mais complexa, sendo assim um algoritmo que tenha apenas esse foco é mais util, já
    nas proximas vezes, não será necessário ordenar tudo e sim inserir na ordem correta, então fica melhor um algoritmo com esse
    foco.
    """


def first_sort(aList: list):
    grades = aList.copy()
    for i in range(len(grades)):
        for j in range(len(grades)-1-i):
            if grades[j] > grades[j+1]:
                grades[j], grades[j+1] = grades[j+1], grades[j]
    return grades


def insert_new_grade(aList: list, new_grade: int):
    grades = aList.copy()
    grades.append(new_grade)
    for i in range(len(grades) - 1, 0, -1):
        if grades[i] < grades[i - 1]:
            grades[i], grades[i - 1] = grades[i - 1], grades[i]
        else:
            break
    return grades


if __name__ == "__main__":
    import random

    test_registers = [random.randint(0, 10) for _ in range(10)]
    start_time = time.time()
    only_sort = first_sort(test_registers)
    end_time = time.time()

    start_time = time.time()
    insert_grade = insert_new_grade(only_sort, 3.5)
    end_time = time.time()

    total_time = end_time - start_time
    print(total_time)
    print(only_sort)
    print(insert_grade)
