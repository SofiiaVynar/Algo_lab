from queue import Queue


def add_ribs(graph, start, end):
    if start not in graph:
        graph[start] = []
    if end not in graph:
        graph[end] = []
    graph[end].append(start)


def bfs(graph, start, target):
    visited = set()
    queue = Queue()
    queue.put(start)
    visited.add(start)

    while not queue.empty():
        current = queue.get()
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.put(neighbor)
                if neighbor == target:
                    return True
    return False


def isAble(pipelines, cities, storages):
    graph = {}
    result = {}

    for start, end in pipelines:
        add_ribs(graph, start, end)

    for storage in storages:
        unable_cities = [city for city in cities if not bfs(graph, city, storage)]
        result[storage] = unable_cities

    all_able = all(not cities for cities in result.values())
    if all_able:
        return {}

    return result


input_file = 'inputs.txt'
output_file = 'outputs.txt'

with open(input_file, 'r') as f:
    lines = f.readlines()

    pipelines = [line.strip().split() for line in lines[0:7]]
    cities = lines[8].strip().split()
    storages = lines[10].strip().split()

    unable = isAble(pipelines, cities, storages)

with open(output_file, 'w') as f:
    f.write(str(unable))