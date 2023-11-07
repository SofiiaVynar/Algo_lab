def numIslands(file_path):
    def reformat_graph(array):
        graph = {}
        for r in range(rows):
            for c in range(cols):
                if array[r][c] == '1':
                    possible = []
                    for nb_r in [-1, 0, 1]:
                        for nb_c in [-1, 0, 1]:
                            if nb_r == 0 and nb_c == 0:
                                continue
                            new_r, new_c = r + nb_r, c + nb_c
                            if 0 <= new_r < rows and 0 <= new_c < cols and array[new_r][new_c] == '1':
                                possible.append((new_r, new_c))
                    graph[(r, c)] = possible
        return graph

    def through_width(peak):
        queue = [peak]
        visited.add(peak)
        while queue:
            current_peak = queue.pop(0)
            for neighbor in graph[current_peak]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

    num_islands = 0
    with open(file_path, 'r') as file:
        rows, cols = 0, 0
        array = [line.strip().split() for line in file.readlines()]
        for row in array:
            rows += 1
            cols = 0
            for _ in row:
                cols += 1

    graph = reformat_graph(array)
    visited = set()
    for r in range(rows):
        for c in range(cols):
            if array[r][c] == '1' and (r, c) not in visited:
                through_width((r, c))
                num_islands += 1

    with open('output.txt', 'w') as output_file:
        output_file.write(f"{num_islands}")


file_path = 'lab_4.txt'

numIslands(file_path)

"""
grid = [
    ['1', '0', '1', '0', '0', '1', '0', '1', '0', '1'],
    ['0', '1', '0', '0', '1', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '1', '0', '0', '0', '0', '0', '0']
]
grid = [
    ['1', '0', '1', '0', '0', '0', '1', '1', '1', '1'],
    ['0', '0', '1', '0', '1', '0', '1', '0', '0', '0'],
    ['1', '1', '1', '1', '0', '0', '1', '0', '0', '0'],
    ['1', '0', '0', '1', '0', '1', '0', '0', '0', '0'],
    ['1', '1', '1', '1', '0', '0', '0', '1', '1', '1'],
    ['0', '1', '0', '1', '0', '0', '1', '1', '1', '1'],
    ['0', '0', '0', '0', '0', '1', '1', '1', '0', '0'],
    ['0', '0', '0', '1', '0', '0', '1', '1', '1', '0'],
    ['1', '0', '1', '0', '1', '0', '0', '1', '0', '0'],
    ['1', '1', '1', '1', '0', '0', '0', '1', '1', '1']
]
1 0 1 0 0 1 0 1 0 1
0 1 0 0 1 0 0 0 0 0
0 0 0 1 0 0 0 0 0 0
"""
