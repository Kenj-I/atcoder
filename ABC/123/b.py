times = [int(input()) for i in range(5)]
ans = 0
minutes = []
for i in range(len(times)):
  ans += times[i]
  if (times[i] % 10) != 0:
    minutes.append(str(times[i])[-1])

minutes.sort(reverse=True)

for j in range(len(minutes) - 1):
  ans += 10 - int(minutes[j])
print(ans)
