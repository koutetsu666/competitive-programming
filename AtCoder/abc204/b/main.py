n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    ans += max(0, a[i] - 10)
print(ans)
