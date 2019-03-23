# Otoshidama
n, total = map(int, input().split())
total //=1000
for noguchi in range(n + 1):
  for higuchi in range(n + 1 - noguchi):
    yukichi = n - noguchi - higuchi
    if(noguchi + higuchi * 5 + yukichi * 10 == total):
      print(yukichi, higuchi, noguchi)
      exit(0)

print('-1 -1 -1')