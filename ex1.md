# Introdução à Notação Big O #

## Função 1 ##

- A primeira função tem complexidade linear, pois possui apenas um loop que é diretamente ligado a quantidade itens a ser iterado:
- Notação Big O -> O(n)

## Função 2 ##

- A segunda função tem complexidade quadrática, pois possui dois loops lineares aninhados, então para cada valor de n é feita uma execução linear (n * n):
- Notação Big O -> O(n^2)

## Função 3 ##

- A terceira função tem complexidade exponencial, por se tratar de uma função recursiva que a cada chamada executa a mesma função mais duas vezes,
então o crescimento é duplicado a cada chamada até que o valor final seja encontrado:
- Notação Big O -> O(2^n)
