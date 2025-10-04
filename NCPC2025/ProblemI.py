###

def solve(n, m, edges):
    graph_out = [set() for _ in range(n)]
    graph_in = [set() for _ in range(n)]
    for u, v in edges:
        graph_out[u].add(v)
        graph_in[v].add(u)
    ccv = 0
    v = n+1
    for i in range(n):
        cur_ccv = sum(x not in graph_out[i] for x in graph_in[i])
        if cur_ccv >= ccv:
            if cur_ccv == ccv:
                v = min(v, i+1)
            else:
                v = i+1
            ccv = max(ccv, cur_ccv)
    return f"{v} {ccv}"






n, m = map(int, input().split())
edges = []
for i in range(m):
    u, v = map(int, input().split())
    edges.append([u-1, v-1])

print(solve(n, m, edges))