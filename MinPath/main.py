import heapq
import time

def read_graph_from_file(filename):
    with open(filename, 'r') as file:
        n = int(file.readline())
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, file.readline().split())))
    return n, matrix


def dijkstra(n, matrix, start_vertex):
    distances = [float('infinity')] * n
    distances[start_vertex] = 0
    priority_queue = [(0, start_vertex)]
    predecessors = [-1] * n

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for i in range(n):
            if matrix[current_vertex][i] and current_distance + matrix[current_vertex][i] < distances[i]:
                distances[i] = current_distance + matrix[current_vertex][i]
                predecessors[i] = current_vertex
                heapq.heappush(priority_queue, (distances[i], i))

    paths = {}
    for i in range(n):
        if distances[i] != float('infinity'):
            path = []
            current = i
            while current != -1:
                path.append(current)
                current = predecessors[current]
            path.reverse()
            paths[i] = path
        else:
            paths[i] = []

    return distances, paths


def bellman_ford(n, matrix, start_vertex):
    distances = [float('infinity')] * n
    distances[start_vertex] = 0
    predecessors = [-1] * n
    edges = []

    for i in range(n):
        for j in range(n):
            if matrix[i][j]:
                edges.append((i, j, matrix[i][j]))

    for _ in range(n - 1):
        for edge in edges:
            u, v, w = edge
            if distances[u] != float('infinity') and distances[u] + w < distances[v]:
                distances[v] = distances[u] + w
                predecessors[v] = u

    for edge in edges:
        u, v, w = edge
        if distances[u] != float('infinity') and distances[u] + w < distances[v]:
            print("Graf zawiera cykl o ujemnej wadze")
            return None, None

    paths = {}
    for i in range(n):
        if distances[i] != float('infinity'):
            path = []
            current = i
            while current != -1:
                path.append(current)
                current = predecessors[current]
            path.reverse()
            paths[i] = path
        else:
            paths[i] = []

    return distances, paths


n, matrix = read_graph_from_file("large_graph.txt")
start_vertex = 0  # zakładając, że zaczynamy od wierzchołka 0 (czyli A)

t_s1 = time.perf_counter()
print("Dijkstra:", dijkstra(n, matrix, start_vertex))
t_e1= time.perf_counter()
time1 = t_e1 - t_s1
print(f'Czas obliczeń: {time1}')

t_s2 = time.perf_counter()
print("Bellman-Ford:", bellman_ford(n, matrix, start_vertex))
t_e2= time.perf_counter()
time2 = t_e2 - t_s2
print(f'Czas obliczeń: {time2}')