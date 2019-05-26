N, M = map(int, input().split())

L_list = []
R_list = []
for i in range(M):
  L, R = map(int, input().split())
  L_list.append(L)
  R_list.append(R)

L = max(L_list)
R = min(R_list)

if R < L:
  print(0)
else:
  print(R - L + 1)