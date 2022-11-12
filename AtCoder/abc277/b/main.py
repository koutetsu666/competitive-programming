n = int(input())

st = set()
for i in range(n):
    s = input()
    if s[0] not in ('H', 'D', 'C', 'S'):
        print("No")
        exit()
    if s[1] not in ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K'):
        print("No")
        exit()
    st.add(s)

if len(st) != n:
    print("No")
    exit()
print("Yes")

