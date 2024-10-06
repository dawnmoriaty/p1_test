from collections import defaultdict

def dfs(gr, node, parent, max_length, current_length):
    if current_length > max_length:
        return 0
    count = 1
    # i
    for neighbor, length in gr[node]:
        if neighbor != parent:
            count += dfs(gr, neighbor, node, max_length, current_length + length)
    return count
def count_cycles(graph, t):
    total_cycles = 0
    for node in graph:
        total_cycles += dfs(graph, node, -1, t, 0)
    return total_cycles

if __name__ == "__main__":
    graph = defaultdict(list)
    edges = [(1, 2, 3), (1, 3, 2), (2, 4, 1), (3, 5, 4)]
    for u, v, length in edges:
        graph[u].append((v, length))
        graph[v].append((u, length))
    t = 3 #wmax
    result = count_cycles(graph, t)

    print(f"{result}")
