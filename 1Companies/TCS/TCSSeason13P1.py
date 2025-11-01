def can_form_by_one_cut_insert(shuffled, original):
    N = len(shuffled)
    if shuffled == original:
        return True
    for l in range(N):
        for r in range(l, N):
            segment = shuffled[l:r+1]
            remaining = shuffled[:l] + shuffled[r+1:]
            for i in range(len(remaining)+1):
                candidate = remaining[:i] + segment + remaining[i:]
                if candidate == original:
                    return True
    return False

def min_cut_insert(shuffled, original):
    if shuffled == original:
        return 0
    if can_form_by_one_cut_insert(shuffled, original):
        return 1

    N = len(shuffled)
    # Try all one cut-insert operations and check if from the resulting list,
    # original can be formed by one more cut-insert.
    for l1 in range(N):
        for r1 in range(l1, N):
            segment1 = shuffled[l1:r1+1]
            remaining1 = shuffled[:l1] + shuffled[r1+1:]
            for i1 in range(len(remaining1)+1):
                after_one = remaining1[:i1] + segment1 + remaining1[i1:]
                # Now check if from after_one we can get original by one cut-insert
                if can_form_by_one_cut_insert(after_one, original):
                    return 2
    return 2  # If not possible with 0 or 1, then must be 2

if __name__ == "__main__":
    N = int(input())
    input()  # 'shuffled'
    shuffled = [input().strip() for _ in range(N)]
    input()  # 'original'
    original = [input().strip() for _ in range(N)]
    print(min_cut_insert(shuffled, original))
