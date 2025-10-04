##


def solve(n, m, k, edges):


    roots = list(range(n+1))
    def root(node):
        if roots[node] != node:
            roots[node] = root(roots[node])
        return roots[node]

    for u, v, in edges:
        ru, rv = root(u), root(v)
        if ru != rv:
            roots[rv] = ru
        

    components = {}
    for i in range(1, n+1):
        ru = root(i)
        if ru not in components:
            components[ru] = []
        components[ru].append(i)

    res = [-1] * (n+1)
    idx = {ru:0 for ru in components}
    for i in range(1, n+1):
        ru = root(i)
        res[i] = (idx[ru] % k) + 1
        idx[ru] += 1
    if any(idx[ru] < k for ru in components):
        return "impossible"

    return " ".join(map(str, res[1:]))




n, m , k = map(int, input().split())
edges = []
for i in range(m):
    a, b = map(int, input().split())
    edges.append([a, b])
print(solve(n, m, k, edges))