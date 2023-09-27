import random

def generate_maximal_planar_graph(n):
    if n < 3:
        return None
    
    vertices = list(range(n))
    edges = []
    
    # Choose 3 vertices to form a triangle
    v1, v2, v3 = random.sample(vertices, 3)
    edges.append((v1, v2))
    edges.append((v2, v3))
    edges.append((v3, v1))
    
    # For each remaining vertex, add edges to 2 vertices that are already connected by an edge
    for i in range(3, n):
        connected_vertices = random.sample(vertices[:i], 2)
        for j in range(2):
            u = connected_vertices[j]
            if (u, i) not in edges and (i, u) not in edges:
                edges.append((u, i))
    
    # Randomly reorder the edges
    random.shuffle(edges)
    
    return vertices, edges

vertices, edges = generate_maximal_planar_graph(10)
print(vertices)
print(edges)
print(len(edges) == 3 * len(vertices) - 6)






def is_maximal_planar(vertices, edges):
    n = len(vertices)
    if n < 3:
        return False
    
    if len(edges) != 3 * n - 6:
        return False
    
    # Create a dictionary to store the neighbors of each vertex
    neighbors = {v: set() for v in vertices}
    for u, v in edges:
        neighbors[u].add(v)
        neighbors[v].add(u)
    
    # Create the dual graph
    dual_vertices = edges
    dual_edges = []
    for u, v in edges:
        for w in neighbors[u]:
            if w != v and (w, v) not in edges and (v, w) not in edges:
                dual_edges.append(((u, v), (v, w)))
    
    # Check if the dual graph is a tree
    visited = set()
    queue = [dual_vertices[0]]
    while queue:
        u = queue.pop(0)
        if u in visited:
            return False
        visited.add(u)
        for v in dual_vertices:
            if (u, v) in dual_edges:
                queue.append(v)
    
    return len(visited) == len(dual_vertices)

vertices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
edges = [(1, 8)]
print(is_maximal_planar(vertices, edges))



vertices, edges = generate_maximal_planar_graph(10)
while not is_maximal_planar(vertices, edges):
    vertices, edges = generate_maximal_planar_graph(10)
print(vertices)
print(edges)
    
