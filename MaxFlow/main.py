def ford_fulkerson(graph, source, sink):
    n = len(graph)
    parents = [-1] * n
    max_flow = 0
    flow_paths = []  # Do przechowywania ścieżek przepływu
    original_graph = [row[:] for row in graph]  # Kopia oryginalnego grafu

    def bfs():
        visited = [False] * n
        queue = [source]
        visited[source] = True

        while queue:
            u = queue.pop(0)
            for v in range(n):
                if not visited[v] and graph[u][v] > 0:
                    queue.append(v)
                    visited[v] = True
                    parents[v] = u
        return visited[sink]

    while bfs():
        path_flow = float('inf')
        s = sink
        path = []

        while s != source:
            path_flow = min(path_flow, graph[parents[s]][s])
            path.insert(0, s)
            s = parents[s]
        path.insert(0, source)
        flow_paths.append((path_flow, path))

        max_flow += path_flow
        v = sink
        while v != source:
            u = parents[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parents[v]

    flow_graph = [[0 for _ in range(n)] for _ in range(n)]
    for u in range(n):
        for v in range(n):
            if original_graph[u][v] > 0:
                flow_graph[u][v] = original_graph[u][v] - graph[u][v]
                if flow_graph[u][v] < 0: flow_graph[u][v] = 0

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
    filename = 'MaxFlows_test8.txt'
    graph, n = read_graph_from_file(filename)
    max_flow, flow_graph, flow_paths = ford_fulkerson(graph, 0, n - 1)

    print("Maksymalny przepływ:", max_flow)
    print_flow_graph(flow_graph)
    print_flow_paths(flow_paths)