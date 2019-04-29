N = int(input())
A = list(map(int,input().split()))
count = 0

for i in range(N):
  if A[i] < 0:
    count += 1
    A[i] *= -1
print(sum(A) if count % 2 == 0 else sum(A) - min(A) * 2)
