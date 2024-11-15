## Exibindo a Próxima Tarefa na Pilha ##

def task_on_top(tasks_queue):
    return tasks_queue[-1]


if __name__ == "__main__":
    tasks_queue = ["Task 1: Entrar portal infnet",
                   "Task 2: Ler as atividades", "Task 3: Fazer as atividades"]

    top_task = task_on_top(tasks_queue)
    print("Next task:", top_task)
