##
import math
def solve(n, points):
    x1, y1 = points[0]
    ma = 0
    def dis(x1, y1, x2, y2):
        return math.sqrt((x1-x2)**2+(y1-y2)**2)
    endpoint = (-1, -1)
    for x, y in points:
        d = dis(x1, y1, x, y)
        if d > ma:
            ma = d
            endpoint = (x, y)
    xe, ye = endpoint
    points = sorted((dis(xe, ye, x, y), x, y) for x, y in points)
    return sum(dis(points[i-1][1], points[i-1][2], points[i][1], points[i][2]) for i in range(1, n))


n = int(input())
points = []
for i in range(n):
    x, y = map(int, input().split())
    points.append([x, y])
print(solve(n, points))