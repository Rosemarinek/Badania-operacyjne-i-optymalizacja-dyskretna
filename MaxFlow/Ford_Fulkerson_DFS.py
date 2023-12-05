import time


def fulkerson_dfs(graph, source, sink):
    n = len(graph)
    parents = [-1] * n  
    max_flow = 0
    flow_paths = []  
    original_graph = [row[:] for row in graph]  

    def dfs(u, flow):
        if u == sink:
            return flow
        for v in range(n):
            if parents[v] == -1 and graph[u][v] > 0:
                parents[v] = u
                next_flow = min(flow, graph[u][v])
                result = dfs(v, next_flow)
                if result > 0:
                    return result
        return 0

    while True:
        parents = [-1] * n
        path_flow = dfs(source, float('inf'))

        if path_flow == 0:
            break

        max_flow += path_flow
        v = sink
        path = []
        while v != source:
            u = parents[v]
            path.insert(0, v)
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = u
        path.insert(0, source)
        flow_paths.append((path_flow, path))

    flow_graph = [[0 for _ in range(n)] for _ in range(n)]
    for u in range(n):
        for v in range(n):
            if original_graph[u][v] > 0:
                flow_graph[u][v] = original_graph[u][v] - graph[u][v]
                if flow_graph[u][v] < 0: 
                    flow_graph[u][v] = 0

    return max_flow, flow_graph, flow_paths

def print_flow_graph(flow_graph):
    print("Graf przepływów:")
    for row in flow_graph:
        x = sum(row)
        print(x, row)

def print_flow_paths(flow_paths):
    print("Ścieżki przepływów:")
    for flow, path in flow_paths:
        print(f"Przepływ: {flow}, Ścieżka: {path}")

# Wczytywanie danych z pliku
def read_graph_from_file(filename):
    with open(filename, 'r') as file:
        n = int(file.readline().strip())
        graph = [list(map(int, line.split())) for line in file]
    return graph, n

if __name__ == "__main__":
    filename = 'data/MaxFlows_500.txt'
    t_s = time.perf_counter()
    graph, n = read_graph_from_file(filename)
    max_flow, flow_graph, flow_paths = fulkerson_dfs(graph, 0, n - 1)
    t_e = time.perf_counter()
    time = t_e - t_s

    print("Maksymalny przepływ:", max_flow)
    print_flow_graph(flow_graph)
    print_flow_paths(flow_paths)
    print(f'Czas obliczeń: {time}')
