# Labirinto com Busca em Largura e Profundidade

Este projeto é uma visualização interativa da resolução de labirintos usando dois algoritmos clássicos de busca: **Busca em Profundidade (DFS)** e **Busca em Largura (BFS)**. A aplicação foi desenvolvida em Python utilizando a biblioteca **Pygame** para representar o labirinto e a execução dos algoritmos de forma animada.

##### Autores: Gustavo Moro e Lucas Gabriel Bernardino
---

## Algoritmos Implementados

### Busca em Profundidade (Depth-First Search - DFS)
A DFS explora o mais fundo possível em cada caminho antes de retroceder. É simples de implementar, porém **não garante o caminho mais curto** e pode ser ineficiente em certos casos.

### Busca em Largura (Breadth-First Search - BFS)
A BFS explora todos os vizinhos de um nó antes de passar para os próximos níveis. Garante encontrar o **caminho mais curto** (em termos de número de passos) se o custo de todos os caminhos for o mesmo.

---

## Estrutura dos Arquivos

```
labirinto/
├── main.py         # Interface gráfica principal com Pygame
├── depth.py        # Implementação da busca em profundidade (DFS)
├── breadth.py      # Implementação da busca em largura (BFS)
├── utils.py        # Funções utilitárias como geração e desenho do labirinto
```
---

## Como Executar

1. Instale as dependências
```
pip install pygame
```

2. Execute no modo visualização
```
python main.py
```
---