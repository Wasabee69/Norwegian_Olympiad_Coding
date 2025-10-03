###
from sortedcontainers import SortedList
from bisect import bisect_left as bisect_left
import heapq
def Q1(n, klosser):
    res = 0
    unq = {}
    for h, b in klosser:
        if b not in unq:
            unq[b] = h
            res += unq[b]
        else:
            res -= unq[b]
            unq[b] = max(unq[b], h)
            res += unq[b]
    return res

N = 5
klosser = [(1, 2), (4, 5), (2, 1), (9, 5), (5, 5)]
print(Q1(N, klosser))

def Q2(n, ledere, edges):

    votes = [(1 if v == "S" else 0, p) for v, p in edges]
    graph = [[] for _ in range(n)]

    for i in range(1, n):
        v, p = votes[i]
        graph[ledere[i]].append((i, v, p))

    def rec(node):
        tot_votes = 1 + len(graph[node])
        good_votes = sum(v for _, v, p in graph[node]) + votes[node][0]

        this_price = 0 if votes[node][0] else votes[node][1]
        if not graph[node]:
            return this_price

        picks = sorted([rec(emp) for emp, v, p in graph[node]])
        picks_this = sorted(picks + [this_price])

        if tot_votes%2 == 0:
            if votes[node][0]:
                return sum(picks[:(tot_votes // 2) - 1])
            return min(this_price + sum(picks[:(tot_votes // 2) - 1]), sum(picks_this[:(tot_votes // 2) + 1]))
        return sum(picks_this[:(tot_votes // 2) + 1])

    return rec(0)



N = 6
ledere = [0,2,0,2,2,0]
edges = [("G", 10), ("G", 6), ("S", 2), ("G", 4), ("G", 9), ("G", 8)]
print(Q2(N, ledere, edges))

N = 5
ledere = [0, 3, 0, 2, 0]
edges = [("G", 8), ("s", 6), ("G", 4), ("S", 2), ("G", 2)]
print(Q2(N, ledere, edges))

def Q3(n, k, heights):
    def target(so):
        length = len(so)
        if length % 2 == 0:
            return (so[length // 2] + so[(length - 1) // 2]) // 2
        return so[length // 2]

    stack = SortedList([heights[0]])
    left = res = diff = 0
    def add_(x):
        res = 0
        length = len(stack)
        prev_mid = target(stack)
        stack.add(x)
        new_mid = target(stack)
        if prev_mid < new_mid:
            res += ((length+1) // 2) * (new_mid - prev_mid) - (length // 2) * (new_mid - prev_mid)
        elif prev_mid > new_mid:
            res += ((length+1) // 2) * (prev_mid - new_mid) - (length // 2) * (prev_mid - new_mid)
        return res + abs(new_mid - x)

    def remove_(x):
        length = len(stack)
        prev_mid = target(stack)
        res = -abs(prev_mid - x)
        stack.remove(x)
        new_mid = target(stack)
        if prev_mid < new_mid:
            res += (((length + 1) // 2 - 1)) * (new_mid - prev_mid) - (length // 2) * (new_mid - prev_mid)
        elif prev_mid > new_mid:
            res += (((length + 1) // 2 - 1)) * (prev_mid - new_mid) - (length // 2) * (prev_mid - new_mid)
        return res

    for i in range(1, n):
        diff += add_(heights[i])
        while diff > k:
            diff += remove_(heights[left])
            left += 1
        res = max(res, i - left + 1)
    return res

N = 5
K = 3
heights = [4, 4, 4, 4, 4]
print(Q3(N, K, heights), "expected =", 5)

N = 6
K = 5
heights = [1, 2, 3, 3, 2, 1]
print(Q3(N, K, heights), "expected =", 6)




def Q4(n, m, q, drown, edges, queries):
    maximum = [-1] * n
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    def expand(node):
        maximum[node] = drown[node]
        heap = [(-maximum[node], node)]
        while heap:
            year, node = heapq.heappop(heap)
            for nei in graph[node]:
                new_year = min(drown[nei], -year)
                if new_year > maximum[nei]:
                    maximum[nei] = new_year
                    heapq.heappush(heap, (-new_year, nei))


    ans = []
    for instruction, node in queries:
        if instruction == "!":
            expand(node)
        else:
            ans.append(maximum[node])
    return ans



N = 4
M = 3
Q = 5
drown = [20, 10, 30, 40]
edges = [[0, 1], [1, 2], [2, 3]]
queries = [["!", 2], ["?", 0], ["?", 1], ["?", 2], ["?", 3]]
print(Q4(N, M, Q, drown, edges, queries))

N = 7
M = 7
Q = 7
drown = [101, 105, 106, 103, 108, 107, 110]
edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0), (0, 3)]
queries = [("?", 4), ("!", 0), ("?", 4), ("?", 1), ("!", 2), ("?", 4), ("?", 1), ("!", 5), ("?", 4), ("?", 1), ("?", 6)]
print(Q4(N, M, Q, drown, edges, queries))



def Q5(n, q, s, queries):

    a = [0]
    b = [0]
    for i in range(n): a.append(a[-1]+(s[i] == "A"))
    for i in range(n): b.append(b[-1]+(s[i] == "B"))
    round_at_points_of_a = {}
    round_at_points_of_b = {}
    for i in range(1, n+1):
        x = a[i]
        if x not in round_at_points_of_a:
            round_at_points_of_a[x] = i

    for i in range(1, n+1):
        x = b[i]
        if x not in round_at_points_of_b:
            round_at_points_of_b[x] = i

    differences = {}
    difference_at = [0] * (n+1)
    for i in range(1, n+1):
        differences.setdefault(a[i] - b[i], []).append(i)
        difference_at[i] = a[i] - b[i]
    for d in differences:
        differences[d].append(n+1)

    points_set = set([k for k, m in queries])
    results = {}
    for k in sorted(list(points_set)):
        won_a = won_b = 0
        left = 0
        while left <= n:
            next_k_a = round_at_points_of_a.get(a[left] + k, n+1)
            next_k_b = round_at_points_of_b.get(b[left] + k, n+1)

            if next_k_a < n+1 and difference_at[next_k_a] - difference_at[left] < 2:
                diff_atleast_2 = difference_at[left] + 2
                if diff_atleast_2 in differences:
                    next_k_a = differences[diff_atleast_2][bisect_left(differences[diff_atleast_2], next_k_a)]
                else:
                    next_k_a = n+1

            if next_k_b < n+1 and difference_at[next_k_b] - difference_at[left] > -2:
                diff_atleast_2 = difference_at[left] - 2
                if diff_atleast_2 in differences:
                    next_k_b = differences[diff_atleast_2][bisect_left(differences[diff_atleast_2], next_k_b)]
                else:
                    next_k_b = n+1

            if next_k_a < next_k_b:
                won_a += 1
            if next_k_a > next_k_b:
                won_b += 1
            left = min(next_k_a, next_k_b)
            
            if won_a > won_b and (k, won_a) not in results:
                results[(k, won_a)] = ("A", left)
            if won_a < won_b and (k, won_b) not in results:
                results[(k, won_b)] = ("B", left)


    return [results.get((k, m), "X") for k, m in queries]



N = 19
Q = 5
S = "BBABAAAABBAABBABBBB"
queries = [(1, 2), (1, 4), (3, 2), (4, 2), (5, 2)]
print(Q5(N, Q, S, queries))

