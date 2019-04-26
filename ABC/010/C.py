ax, ay, bx, by, T, V = map(int, input().split())
N = int(input())
girls = list(list(map(int, input().split())) for _ in range(N))

for i in range(N):
  move = ((girls[i][0] - ax) ** 2 + (girls[i][1] - ay) ** 2) ** 0.5 + ((bx - girls[i][0]) ** 2 + (by - girls[i][1]) ** 2 ) ** 0.5
  if T * V >= move:
    print('YES')
    exit()
print('NO')