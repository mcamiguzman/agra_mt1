def generate_graph(grid):
    graph = {}

    # Crear verices 
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            nodo = grid[row][col]
            if nodo not in graph:
                graph[nodo] = []

            # conexiones 
            if row > 0:
                graph[nodo].append(grid[row - 1][col])
            if row < len(grid) - 1:
                graph[nodo].append(grid[row + 1][col])
            if col > 0:
                graph[nodo].append(grid[row][col - 1])
            if col < len(grid[row]) - 1:
                graph[nodo].append(grid[row][col + 1])
    return graph

def calculate_gols_total(grafo):
    num_nodos = len(grafo)
    total_gold = 0

    for nodo in grafo:
        if nodo == "G":
            total_gold += 1
    return total_gold

def calculate1(graph):
    num_v = len(graph)
    invalid_gold = 0

    for v in range(num_v):
        if graph[v] == "G":
            invalid = False
            for neighbor in graph[v]:
                if neighbor == "#":
                    invalid = True
                elif neighbor == "T":
                    invalid = True
                    for other_neighbor in graph[v]:
                        if other_neighbor == "#":
                            invalid = False
                        if other_neighbor == "G":
                            invalid_gold += 1
                            break
                    break
            if invalid:
                invalid_gold += 1
    return invalid_gold

def calculate2(graph):
    num_v = len(graph)
    invalid_gold = 0

    for v in range(num_v):
        if "T" in graph[v] and "P" not in graph[v]:
            for neighbor in graph[v]:
                if neighbor == "G":
                    invalid_gold += 1
                    break
    return invalid_gold              

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
            graph = generate_graph(grid)
            answer = calculate_gols_total(graph)-(calculate1(graph)+calculate2(graph))
            total_answers.append(answer)
        except EOFError:
            break 
    for i in total_answers:
            print(i)
main()