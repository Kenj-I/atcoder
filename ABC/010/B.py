N = int(input())
hanabira = list(map(int, input().split()))
ans = 0
d = [0, 0, 1, 0, 1, 2, 3, 0, 1, 0]

for i in range(N):
  ans += d[hanabira[i]]
print(ans)

