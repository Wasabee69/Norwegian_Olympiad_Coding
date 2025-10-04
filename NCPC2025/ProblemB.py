###
from functools import cache


def solve(n, H, W, books):
    books = sorted([(h, w, i) for i, (h, w) in enumerate(books)],key=lambda x: x[0], reverse=True)
    @cache
    def rec(tot_width, height_laying, i, layed, upright):
        if tot_width > W: return None
        if i == n:
            if tot_width <= W and layed and upright:
                return ["!"]
            return None
        h, w, idx = books[i]
        if h <= H:
            if rec(tot_width+w, height_laying, i+1, layed, 1) is not None:
                return rec(tot_width+w, height_laying, i+1, layed, 1) + [(0, idx)]

        if height_laying and height_laying+w <= H:
            if rec(tot_width, height_laying+w, i+1, 1, upright) is not None:
                return rec(tot_width, height_laying+w, i+1, 1, upright) + [(1, idx)]
        elif w <= H:
            if rec(tot_width+h, w, i+1, 1, upright) is not None:
                return rec(tot_width+h, w, i+1, 1, upright) + [(1, idx)]

    if rec(0, 0, 0, 0, 0):
        res = {0:[], 1:[]}
        for i in range(n, 0, -1):
            status, idx = rec(0, 0, 0, 0, 0)[i]
            res[status].append(idx+1)
        return f"upright {' '.join(map(str, res[0]))}\nstacked {' '.join(map(str, res[1]))}"
    return "impossible"



    

        

N, H, W = map(int, input().split())
books = []
for i in range(N):
    h, w = map(int, input().split())
    books.append((h, w))
print(solve(N, H, W, books))


