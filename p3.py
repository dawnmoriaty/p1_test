from collections import defaultdict

def dfsCountE(graph, node, parent, t, current_length):
    if current_length > t:
        return 0
    count = 0
    for neighbor, length in graph[node]:
        if neighbor != parent:
            count += 1  # Đếm cạnh giữa node và neighbor
            count += dfsCountE(graph, neighbor, node, t, current_length + length)
    return count

def countCycle(graph, t):
    total_cycles = 0
    visited = set()
    for node in graph:
        if node not in visited:
            total_cycles += dfsCountE(graph, node, -1, t, 0)
            visited.add(node)
    return total_cycles


if __name__ == "__main__":
    graph = defaultdict(list)
    edges = [(1, 2, 3), (1, 3, 2), (2, 4, 1), (3, 5, 4)]
    for u, v, length in edges:
        graph[u].append((v, length))
        graph[v].append((u, length))

    t = 3
    result = countCycle(graph, t)

    print(f"Tổng số các cạnh thuộc vòng chạy có độ dài tối đa {t}: {result}")
