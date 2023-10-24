import random

def is_cyclic_util(graph, node, visited, rec_stack):
    visited[node] = True
    rec_stack[node] = True

    for neighbor in graph[node]:
        if not visited[neighbor]:
            if is_cyclic_util(graph, neighbor, visited, rec_stack):
                return True
        elif rec_stack[neighbor]:
            return True

    rec_stack[node] = False
    return False

def is_cyclic(graph, N):
    visited = [False] * (N + 1)
    rec_stack = [False] * (N + 1)
    for node in range(1, N + 1):
        if not visited[node] and is_cyclic_util(graph, node, visited, rec_stack):
            return True
    return False

N = 400

# Losowe czasy trwania zadań
task_durations = [random.randint(1, 100) for _ in range(N)]

# Losowa liczba połączeń - przyjmujmy, że chcemy średnio około 2 połączenia na zadanie
M = 2 * N

# Losowe połączenia
dependencies = []
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    task_from = random.randint(1, N)
    task_to = random.randint(1, N)
    while task_from == task_to or (task_from, task_to) in dependencies:  # Upewnij się, że nie ma duplikatów
        task_from = random.randint(1, N)
        task_to = random.randint(1, N)
    
    # Dodaj połączenie i sprawdź czy tworzy cykl
    graph[task_from].append(task_to)
    if is_cyclic(graph, N):
        # Jeśli tworzy cykl, usuń połączenie
        graph[task_from].remove(task_to)
    else:
        # Jeśli nie tworzy cyklu, dodaj do listy zależności
        dependencies.append((task_from, task_to))

# Zapisz do pliku
with open("input.txt", "w") as f:
    f.write(f"{N} {len(dependencies)}\n")
    f.write(" ".join(str(t) for t in task_durations) + "\n")
    for dep in dependencies:
        f.write(f"{dep[0]} {dep[1]}  ")

print("File generated!")
