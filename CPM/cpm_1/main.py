import time


def cpm(input_file, output_file):
    with open(input_file, 'r') as file:
        N, M = map(int, file.readline().split()) # N liczba zadan i M liczba polaczen
        durations = list(map(int, file.readline().split())) # czas trwania kazdego zadania
        dependencies = [] # zaleznosci
        for line in file:
            split_line = list(map(int, line.split()))
            for i in range(0, len(split_line), 2):
                dependencies.append((split_line[i], split_line[i + 1])) #pary zaleznosci

    earlyStart = [0] * N
    earlyFinish = [0] * N
    lateStart = [float('inf')] * N
    lateFinish = [float('inf')] * N

    #  przetwarzanie w przód: obliczenie ES, EF
    for _ in range(N):
        for a, b in dependencies:
            a, b = a-1, b-1 # zmniejszamy o 1, aby dostosować się do indeksów od zera
            earlyStart[b] = max(earlyStart[b], earlyFinish[a])
        for i in range(N):
            earlyFinish[i] = earlyStart[i] + durations[i]

    projectTime = max(earlyFinish)

    # przetwarzanie wstecz: obliczenie LS i LF
    for i in range(N):
        lateFinish[i] = projectTime
    for _ in range(N):
        for a, b in dependencies:
            a, b = a-1, b-1
            lateFinish[a] = min(lateFinish[a], lateStart[b])
        for i in range(N):
            lateStart[i] = lateFinish[i] - durations[i]

    criticalPath = []
    for i in range(N):
        if earlyStart[i] == lateStart[i] and earlyFinish[i] == lateFinish[i]:
            criticalPath.append((i + 1, earlyStart[i], earlyFinish[i]))

    criticalPath.sort(key=lambda x: x[1])  # Sortuj ścieżkę krytyczną według czasu rozpoczęcia

    isCycleInGraph = False
    for i in range(N):
        if earlyStart[i] > lateStart[i] or earlyFinish[i] > lateFinish[i]:
            isCycleInGraph = True

    if(isCycleInGraph):
        with open(output_file, 'w') as file:
            file.write("There is cycle in the graph. This project doesn't end.\n")
    else:
        with open(output_file, 'w') as file:
            file.write(f"process time:\n{projectTime}\n")
            file.write("earlyStart earlyFinish lateStart lateFinish:\n")
            for i in range(N):
                file.write(f"{earlyStart[i]} {earlyFinish[i]} {lateStart[i]} {lateFinish[i]}\n")
            file.write("critical path:\n")
            for task, es, ef in criticalPath:
                file.write(f"{task} {es} {ef}\n")

#algorithm nr 1
if __name__ == "__main__":
    t_s = time.perf_counter()
    cpm('input.txt', 'output.txt')
    t_e= time.perf_counter()

    time=t_e-t_s
    print(f'Time operation: {time}')
