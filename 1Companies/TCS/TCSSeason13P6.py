import sys
from itertools import combinations
from collections import Counter

def polygon_area(points):
    area = 0.0
    n = len(points)
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i+1)%n]
        area += (x1*y2 - x2*y1)
    return abs(area)/2.0

def forms_closed_polygon(sticks):
    points = []
    point_counts = Counter()
    for x1, y1, x2, y2 in sticks:
        points += [(x1, y1), (x2, y2)]
        point_counts[(x1, y1)] += 1
        point_counts[(x2, y2)] += 1
    # Each unique point used exactly twice
    unique_points = list(set(points))
    for pt in unique_points:
        if point_counts[pt] != 2:
            return False, []
    # Try to order vertices in sequence
    used = set()
    seq = [unique_points[0]]
    curr = seq[0]
    used.add(curr)
    while len(seq) < len(unique_points):
        found = False
        for x1, y1, x2, y2 in sticks:
            if (x1, y1) == curr and (x2, y2) not in used:
                seq.append((x2, y2))
                curr = (x2, y2)
                used.add(curr)
                found = True
                break
            elif (x2, y2) == curr and (x1, y1) not in used:
                seq.append((x1, y1))
                curr = (x1, y1)
                used.add(curr)
                found = True
                break
        if not found:
            return False, []
    return True, seq

def solve_game(sticks):
    N = len(sticks)
    max_kalyan_area = -1
    kalyan_indices = []
    for k in range(N, 2, -1):
        for comb in combinations(range(N), k):
            comb_sticks = [sticks[i] for i in comb]
            ok, poly = forms_closed_polygon(comb_sticks)
            if ok:
                area = polygon_area(poly)
                if area > max_kalyan_area:
                    max_kalyan_area = area
                    kalyan_indices = list(comb)
        if max_kalyan_area > -1:
            break
    if max_kalyan_area == -1:
        print("Abandoned")
        return
    leftover = [sticks[i] for i in range(N) if i not in kalyan_indices]
    max_computer_area = -1
    for k in range(len(leftover), 2, -1):
        for comb in combinations(range(len(leftover)), k):
            comb_sticks = [leftover[i] for i in comb]
            ok, poly = forms_closed_polygon(comb_sticks)
            if ok:
                area = polygon_area(poly)
                if area > max_computer_area:
                    max_computer_area = area
    if max_computer_area > max_kalyan_area:
        print("Computer")
    else:
        print("Kalyan")

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    sticks = []
    for _ in range(N):
        sticks.append(tuple(map(int, sys.stdin.readline().split())))
    solve_game(sticks)

