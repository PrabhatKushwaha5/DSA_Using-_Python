from itertools import combinations, chain

def get_folds(start, end, rects, index):
    valid = []
    for c in range(start + 1, end):
        ok = True
        for r in rects:
            if r[index] < c < r[index+2]:
                ok = False
                break
        if ok:
            valid.append(c)
    return valid

def powerset(iterable):
    # powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def solve():
    N = int(input())
    rects = [tuple(map(int, input().split())) for _ in range(N)]
    x1, y1, x2, y2 = map(int, input().split())

    folds_x = get_folds(x1, x2, rects, 0)
    folds_y = get_folds(y1, y2, rects, 1)

    min_area = float('inf')

    for sel_x in powerset(folds_x):
        Xs = sorted([x1, x2] + list(sel_x))
        for sel_y in powerset(folds_y):
            Ys = sorted([y1, y2] + list(sel_y))
            for i in range(len(Xs)-1):
                for j in range(len(Ys)-1):
                    area = (Xs[i+1] - Xs[i]) * (Ys[j+1] - Ys[j])
                    if area < min_area:
                        min_area = area
    print(min_area)

if __name__ == "__main__":
    solve()
