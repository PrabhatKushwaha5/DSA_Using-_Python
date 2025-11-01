def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def min_cars(races):
    N = len(races)
    adj = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j:
                if races[j][2] > races[i][2]:
                    # Check if can move from race i to race j based on Manhattan distance and time
                    if races[j][2] - races[i][2] >= manhattan(races[j], races[i]):
                        adj[i].append(j)

    match_to = [-1] * N

    def bpm(u, visited):
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                if match_to[v] == -1 or bpm(match_to[v], visited):
                    match_to[v] = u
                    return True
        return False

    max_matching = 0
    for u in range(N):
        visited = [False] * N
        if bpm(u, visited):
            max_matching += 1

    # Minimum number of cars needed is total races - max matching (minimum path cover in DAG)
    return N - max_matching

if __name__ == "__main__":
    N = int(input())
    races = [tuple(map(int, input().split())) for _ in range(N)]
    print(min_cars(races))
