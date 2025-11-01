def normalize_edge(edge):
    return tuple(sorted(edge))

def find_cycles_in_permutation(perm):
    visited = set()
    cycles = 0
    for i in range(len(perm)):
        if i not in visited:
            cycles += 1
            current = i
            while current not in visited:
                visited.add(current)
                current = perm[current]
    return cycles

def zoobin_min_rotations(E, current_edges, expected_edges):
    # Normalize edges to treat undirected edges consistently
    current_normalized = [normalize_edge(e) for e in current_edges]
    expected_normalized = [normalize_edge(e) for e in expected_edges]

    # Map each normalized current edge to its index for permutation creation
    edge_to_index = {edge: idx for idx, edge in enumerate(current_normalized)}

    # Create permutation mapping from expected edges to current edges by indices
    perm = [edge_to_index[edge] for edge in expected_normalized]

    # Number of cycles in this permutation is the minimum number of rotations required
    return find_cycles_in_permutation(perm)

if __name__ == "__main__":
    E = int(input())
    current_edges = [tuple(map(int, input().split())) for _ in range(E)]
    expected_edges = [tuple(map(int, input().split())) for _ in range(E)]

    print(zoobin_min_rotations(E, current_edges, expected_edges))
