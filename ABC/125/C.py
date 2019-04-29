from fractions import gcd
N = int(input())
A = [int(i) for i in input().split()]

L, R = [], []
for i in range(N):
  L.append(gcd(L[i-1],A[i-1]) if i else 0)
  R.append(gcd(R[i-1],A[N-i]) if i else 0)
print(max([gcd(L[i],R[N-i-1]) for i in range(N)]))