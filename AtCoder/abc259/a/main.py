n, m, x, t, d = map(int, input().split())
if x <= m <= n:
    print(t)
else:
    print(t + (m - x) * d)
