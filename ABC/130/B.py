N, X = map(int, input().split())
positions = list(map(int, input().split()))


ans = 1
D = 0
for i in range(N):
    if D + positions[i] <= X:
        D += positions[i]
        ans += 1
    else:
        print(ans)
        exit()
print(ans)
