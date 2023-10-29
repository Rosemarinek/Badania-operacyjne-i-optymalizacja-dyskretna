import random

# Tworzenie losowego grafu z 100 wierzchołkami
n = 900
max_weight = 10  # Maksymalna waga krawędzi
graph = [[0 if i == j else random.randint(1, max_weight) for j in range(n)] for i in range(n)]

# Zapisywanie grafu do pliku
with open("large_graph.txt", "w") as file:
    file.write(f"{n}\n")
    for row in graph:
        file.write(" ".join(map(str, row)) + "\n")
