def is_valid_move(row, col, rows, cols, matrix):
    return 0 <= row < rows and 0 <= col < cols and matrix[row][col] != '#'

def generate_adjacency_list(grid):
    rows = len(grid)
    cols = len(grid[0])
    graph = []

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] != '#':
                neighbors = []
                if is_valid_move(row - 1, col, rows, cols, grid):
                    neighbors.append(grid[row - 1][col])
                if is_valid_move(row + 1, col, rows, cols, grid):
                    neighbors.append(grid[row + 1][col])
                if is_valid_move(row, col - 1, rows, cols, grid):
                    neighbors.append(grid[row][col - 1])
                if is_valid_move(row, col + 1, rows, cols, grid):
                    neighbors.append(grid[row][col + 1])

                graph.append(neighbors)
                
    return graph

def count_golds(graph):
    num_v = len(graph)
    Gs = []
    Ts = []
    position_player = None

    for v in range(num_v):
        for connection in graph[v]:
            if connection == "P":
                position_player = v
            elif connection == "G":
                Gs.append(v)
            elif connection == "T":
                Ts.append(v)

    def bfs(pos):
        visited = [False] * num_v
        visited[pos[0]] = True
        cola = [pos]
        golds = 0

        while cola:
            node = cola.pop(0)
            if node in Gs:
                Gs.remove(node)
                golds += 1

            for neighbor in graph[node]:
                if not visited[neighbor] and (neighbor not in Ts):
                    visited[neighbor] = True
                    cola.append(neighbor)
        return golds
    total_golds = 0
    if position_player is not None:
        total_golds += bfs(position_player)
    return total_golds

def main():
    total_answers = []
    while True:
        try:
            line_m= input()
            if not line_m:
                break
            
            W, H = map(int, line_m.split())
            lines =[]
            for _ in range(H):
                line = input()
                lines.append(line)
                
            grid = [list(map(str,line.split())) for line in lines]
            graph = matrix_graph(grid)
            answer = count_golds(graph)
            total_answers.append(answer)
        except EOFError:
            break 
    for i in total_answers:
            print(i)
main()