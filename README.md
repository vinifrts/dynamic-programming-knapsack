## Problema: A Mochila do Explorador

Implementação do problema da mochila utilizando três abordagens diferentes:

- recursão ingênua
- top-down com memoização
- bottom-up com tabulação

---

# Parte 1 - Análise do Problema

O problema da mochila pode ser resolvido com programação dinâmica porque ele possui duas características principais:

- subproblemas sobrepostos
- estrutura ótima

## subproblemas sobrepostos

Durante a resolução do problema, vários cálculos iguais acabam sendo repetidos.

Por exemplo, ao decidir se um item será colocado ou não na mochila, o algoritmo precisa resolver novamente versões menores do mesmo problema, como:

- qual o melhor valor possível usando os primeiros 3 itens com capacidade 5
- qual o melhor valor possível usando os primeiros 2 itens com capacidade 4

Esses mesmos cálculos aparecem várias vezes na árvore de recursão.

A programação dinâmica evita repetições armazenando os resultados já calculados.

## estrutura ótima

A solução ótima do problema depende das melhores soluções de subproblemas menores.

Se um item for escolhido, então o restante da solução precisa ser a melhor solução possível para a capacidade restante da mochila.

Por exemplo:

- se um item pesa 4 e a mochila suporta 10
- sobra capacidade 6
- então o problema vira encontrar a melhor combinação possível para capacidade 6

Isso mostra que a solução do problema pode ser construída a partir de soluções ótimas menores.

## conclusão

A programação dinâmica é adequada porque reduz drasticamente a quantidade de cálculos repetidos e consegue encontrar a solução ótima de forma eficiente, principalmente para capacidades maiores da mochila.

---

# Parte 2 - Implementação

O projeto possui três versões do algoritmo:

## versão a - recursão ingênua

Implementação recursiva simples sem otimizações.

## versão b - top-down com memoização

Implementação recursiva com armazenamento de resultados já calculados para evitar repetições.

## versão c - bottom-up com tabulação

Implementação iterativa utilizando tabela para construção da solução ótima.

---

# Conjunto de itens utilizado

| item      | peso | valor |
|-----------|------|--------|
| lanterna  | 2    | 6      |
| barraca   | 4    | 10     |
| faca      | 1    | 3      |
| cobertor  | 3    | 7      |
| cantil    | 2    | 5      |
| mapa      | 1    | 4      |
| corda     | 5    | 9      |

Capacidades testadas:

- W = 6
- W = 10
- W = 15

---

# Como executar

Clone o repositório:

```bash
git clone https://github.com/vinifrts/dynamic-programming-knapsack.git
```

Entre na pasta:

```bash
cd dynamic-programming-knapsack
```

Execute o arquivo:

```bash
python knapsack.py
```

---

# Saída esperada

O programa imprime:

- valor máximo obtido
- itens escolhidos
- peso total ocupado

para as três abordagens implementadas.

---

# Tecnologias utilizadas

- Python 3

---

# Autor

Desenvolvido por Vinicius Freitas.
