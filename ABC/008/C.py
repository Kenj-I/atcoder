# reffer https://qiita.com/anieca/items/ba38d6093b9b117b9530#c
N = int(input())
C = [int(input()) for _ in range(N)]

p = 0
for i in range(N):
  S = [C[j] for j in range(N) if i != j and C[i] % C[j] == 0]
  s = len(S)
  p += (s + 2) / (2 * s + 2) if s % 2 == 0 else 0.5
print(p)