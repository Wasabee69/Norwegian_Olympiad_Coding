###


def solve(n, limits):
    limits = [int(l) if l != "/" else 0 for l in limits]
    ma = 0
    res = []
    for i in range(n):
        ma = max(ma, limits[i])
        if limits[i]:
            res.append(limits[i])
        else:
            res.append(((ma + 10)  // 10) * 10 )
    return "\n".join(str(x) for x in res)


n = int(input())
linjer = []
for i in range(n):
    linjer.append(input())
print(solve(n, linjer))

"""
"""
