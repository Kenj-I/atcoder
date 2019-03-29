dirs = "N NNE NE ENE E ESE SE SSE S SSW SW WSW W WNW NW NNW".split()

deg, dis = map(int, input().split())
Dir = dirs[((deg * 10 + 1125) // 2250) % 16]

l = list(map(float, "0.25 1.55 3.35 5.45 7.95 10.75 13.85 17.15 20.75 24.45 28.45 32.65".split()))
W = 0
for i, x in enumerate(l):
  if dis >= x * 60: W = i+1
  else: break
if W == 0: Dir = 'C'
print(Dir, W)
