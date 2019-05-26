N, M = map(int, input().split())
A = list(map(int, input().split()))
BC = [list(map(int, input().split())) for _ in range(M)]
BC = sorted(BC, key= lambda x:x[1], reverse=True)


BC2 = []
for i in range(M):
  BC2.extend([BC[i][1]] * BC[i][0])
  if len(BC2) > N : break
A.extend(BC2)
A.sort(reverse=True)

print(sum(A[:N]))