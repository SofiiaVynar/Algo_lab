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


pipelines = [['Львів', 'Київ'], ['Київ', 'Запоріжжя'], ['Черкаси', 'Вінниця'], ['Вінниця', 'Запоріжжя'],
             ['Сховище_1', 'Львів'], ['Сховище_2', 'Вінниця'],['Сховище_3', 'Черкаси']]
cities = ['Львів', 'Київ', 'Запоріжжя', 'Черкаси', 'Вінниця']
storages = ['Сховище_1', 'Сховище_2', 'Сховище_3']

unable = isAble(pipelines, cities, storages)
print(unable)