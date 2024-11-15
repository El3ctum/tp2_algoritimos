## Implementando uma Tabela Hash Simples ##

## Referencias ##
"""Para esse exercicio eu tive algumas dificuldades para montar sozinho, então busque na internet por referencias, 
abaixo estão os links para os artigos que usei como referencia.

https: // www.geeksforgeeks.org/implementation-of-hash-table-in -python-using-separate-chaining/
https://python.plainenglish.io/implementing-a-hash-table-in-python-step-by-step-716f61323a4d
https://realpython.com/python-hash-table/
https://stackabuse.com/hash-tables-in-python/
"""



class SimpleHashtable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_func(self, key):
        print(hash(key))
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_func(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def search(self, key):
        index = self._hash_func(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def remove(self, key):
        index = self._hash_func(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return


if __name__ == "__main__":
    table = SimpleHashtable(10)

    table.inserir("Davi", 26)
    table.inserir("Gabriela", 25)
    table.inserir("Daniel", 30)
    table.inserir("Fernando", 35)
    table.inserir("Renata", 40)

    table.buscar("Davi")
    table.buscar("Fernando")
    table.buscar("Gabriela")

    table.remover("Daniel")
    table.remover("Luísa")
