n = int(input())
p = list(map(int, input().split()))

ans = 0
for i in range(1, n-1):
    if (p[i] - p[i - 1]) * (p[i] - p[i + 1]) < 0:
        ans += 1

print(ans)
