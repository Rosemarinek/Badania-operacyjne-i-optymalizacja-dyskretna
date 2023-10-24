import time

def dfs_early(node, graph, durations, earlyStart, earlyFinish):
    for dependent in graph[node]:
        dfs_early(dependent, graph, durations, earlyStart, earlyFinish)
        earlyStart[node] = max(earlyStart[node], earlyFinish[dependent])
    earlyFinish[node] = earlyStart[node] + durations[node-1]

def dfs_late(node, graph, durations, lateStart, lateFinish):
    for dependent in [i for i, x in enumerate(graph) if node in x]:
        dfs_late(dependent, graph, durations, lateStart, lateFinish)
        lateFinish[node] = min(lateFinish[node], lateStart[dependent])
    lateStart[node] = lateFinish[node] - durations[node-1]

def is_cyclic(graph, node, visited, rec_stack):
    visited[node] = True
    rec_stack[node] = True

    for neighbor in graph[node]:
        if not visited[neighbor]:
            if is_cyclic(graph, neighbor, visited, rec_stack):
                return True
        elif rec_stack[neighbor]:
            return True

    rec_stack[node] = False
    return False

def is_acyclic(graph, N):
    visited = [False] * (N + 1)
    rec_stack = [False] * (N + 1)

    for node in range(1, N + 1):
        if not visited[node]:
            if is_cyclic(graph, node, visited, rec_stack):
                return False

    return True

if __name__ == "__main__":
    t_s = time.perf_counter()
    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()

    N, M = map(int, lines[0].split())
    task_durations = list(map(int, lines[1].split()))
    dependencies = list(map(int, lines[2].split()))

    # Build the graph from the dependency information
    graph = [[] for _ in range(N + 1)]
    for i in range(0, 2 * M, 2):
        graph[dependencies[i + 1]].append(dependencies[i])

    is_acyclic_graph = is_acyclic(graph, N)

    with open("output.txt", "w") as output_file:
        if is_acyclic_graph:
            output_file.write("The graph is acyclic.")
        else:
            output_file.write("The graph has cycles.")

# Step 1: Calculate earlyStart and earlyFinish for each task
earlyStart = [0] * (N + 1)
earlyFinish = [0] * (N + 1)
lateStart = [float('inf')] * (N + 1)
lateFinish = [float('inf')] * (N + 1)

for node in range(1, N + 1):
    if not any(node in sublist for sublist in graph):
        dfs_early(node, graph, task_durations, earlyStart, earlyFinish)

projectTime = max(earlyFinish)

# Step 2: Calculate lateStart and lateFinish for each task
lateFinish = [projectTime for _ in range(N + 1)]
lateStart = [projectTime] * (N + 1)

# Start dfs_late od zadań końcowych
for node in range(1, N + 1):
    if not graph[node]:  # Zadania końcowe nie mają zależności wychodzących
        dfs_late(node, graph, task_durations, lateStart, lateFinish)

criticalPath = []
for i in range(1, N + 1):
    if earlyStart[i] == lateStart[i] and earlyFinish[i] == lateFinish[i]:
        criticalPath.append((i, earlyStart[i], earlyFinish[i]))

criticalPath.sort(key=lambda x: x[1])  # Sortuj ścieżkę krytyczną według czasu rozpoczęcia

# Step 3: Write results to the output file
with open("output.txt", "w") as file:
    if is_acyclic_graph:
        file.write(f"process time:\n{projectTime}\n")
        file.write("earlyStart earlyFinish lateStart lateFinish:\n")
        for i in range(1, N + 1):
            file.write(f"{earlyStart[i]} {earlyFinish[i]} {lateStart[i]} {lateFinish[i]}\n")
        file.write("critical path:\n")
        for task, es, ef in criticalPath:
            file.write(f"{task} {es} {ef}\n")
    else:
        file.write("The graph has cycles.")

t_e= time.perf_counter()

time=t_e-t_s
print(f'Time operation: {time}s')