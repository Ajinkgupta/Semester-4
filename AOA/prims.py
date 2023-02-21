from queue import PriorityQueue

def prim(graph, start):
    visited = set()
    min_cost = 0
    pq = PriorityQueue()
    pq.put((0, start))

    while not pq.empty():
        cost, node = pq.get()
        if node in visited:
            continue
        visited.add(node)
        min_cost += cost

        for neighbor, cost in graph[node].items():
            if neighbor not in visited:
                pq.put((cost, neighbor))

    return min_cost
 
graph = {
    'A': {'B': 2, 'D': 3},
    'B': {'A': 2, 'C': 4, 'D': 2},
    'C': {'B': 4, 'D': 1},
    'D': {'A': 3, 'B': 2, 'C': 1},
}

start_node = 'A'
min_cost = prim(graph, start_node)
print(f"Minimum cost of spanning tree starting from node {start_node}: {min_cost}")
