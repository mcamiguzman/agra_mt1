dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def is_valid(x, y, W, H):
    return 0 <= x < W and 0 <= y < H

def build_graph(grid, W, H):
    graph={}
    for x in range(H):
        for y in range(W):
            # Ignorar paredes
            if grid[x][y] == '#':
                continue

            graph[(x, y)] = []

            # Generar conexiones 
            for i in range(4):
                new_x, new_y = x + dx[i], y + dy[i]
                if is_valid(new_x, new_y,W,H) and grid[new_x][new_y] != '#':
                    graph[(x, y)].append((new_x, new_y))
    return graph

def dfs(node, visited,grid,graph):
    x, y = node
    if visited[x][y] or grid[x][y] == 'T':
        return 0

    visited[x][y] = True
    gold_count = 0

    if grid[x][y] == 'G':
        gold_count += 1

    for neighbor in graph[node]:
        gold_count += dfs(neighbor, visited,grid,graph)

    return gold_count


def main():
    resultados = []
    while True:
        try:
            line = input()
            if not line:
                break
            
            W, H = map(int, line.split())
            grid = [input() for _ in range(H)]
            graph = build_graph(grid, W, H)

            start_x, start_y = -1, -1

            # Find the starting position of the player
            for x in range(H):
                for y in range(W):
                    if grid[x][y] == 'P':
                        start_x, start_y = x, y
                        break
                if start_x != -1:
                    break

            visited = [[False] * W for _ in range(H)]
            gold = dfs((start_x, start_y), visited,grid,graph)
            resultados.append(gold)
        except EOFError:
            break 
    for i in resultados:
            print(i)
main()