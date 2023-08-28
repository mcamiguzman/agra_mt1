def grid_graph(grid):
    rows = len(grid)
    columns = len(grid[0])
    graph = {}

    for row in range(rows):
        for col in range(columns):
            contenido = grid[row][col]
            v = [contenido, []]

            if (row, col) not in graph:
                graph[(row, col)] = v

            neighbor = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
            for neighbor in neighbor:
                neighbor_row, neighbor_col = neighbor
                if 0 <= neighbor_row < rows and 0 <= neighbor_col < columns:
                    graph[(row, col)][1].append((neighbor_row, neighbor_col))
    return graph

def dfs(node, graph, visited):
    visited[node] = True
    count = graph[node][0]  
    
    for neighbor in graph[node][1]:
        if not visited[neighbor] and graph[neighbor][0] == 1:
            count += dfs(neighbor, graph, visited)
    return count

def count_groups(graph):
    visited = {node: False for node in graph}
    groups = []
    
    for node in graph:
        if graph[node][0] == 1 and not visited[node]:
            group_size = dfs(node, graph, visited)
            groups.append(group_size)
    
    mayor = max(groups)
    return mayor

def read_grid():
    grid = []
    while True:
        try:
            line = input().strip()
            if not line:
                break
            grid.append(list(line))
        except EOFError:
            break
    return grid

def main():
    results = []
    while True:
        try:
            n = int(input())
            input()

            for _ in range(n):
                grid = read_grid()
                graph = grid_graph(grid)
                result = count_groups(graph)
                results.append(result)

                if _ < n -1:
                    input()
        except EOFError:
            break

