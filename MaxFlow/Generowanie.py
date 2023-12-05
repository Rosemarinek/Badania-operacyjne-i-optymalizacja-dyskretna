import random

def generate_graph(n, max_weight=10, probability=0.5):
    """
    Generuje losowy graf o n wierzchołkach.

    :param n: Liczba wierzchołków
    :param max_weight: Maksymalna waga krawędzi
    :param probability: Prawdopodobieństwo istnienia krawędzi między dwoma wierzchołkami
    :return: Macierz sąsiedztwa
    """
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(i+1, n):
            if random.random() < probability:
                weight = random.randint(1, max_weight)
                matrix[i][j] = weight
                matrix[j][i] = weight
                
    return matrix

def save_graph_to_file(filename, matrix):
    with open(filename, 'w') as file:
        file.write(str(len(matrix)) + '\n')
        for row in matrix:
            file.write('  '.join(map(str, row)) + '\n')

# Przykład użycia:
n = 100  # dla 10 wierzchołków
matrix = generate_graph(n)
save_graph_to_file("input.txt", matrix)
