# https://atcoder.jp/contests/abc001/tasks/abc001_2

# 自分の回答
# m = int(input()) / 1000
# if m < 0.1:
#   vv = '00'
# elif 0.1 <= m < 1:
#   m = str(round(m * 10))
#   vv = m.zfill(2)
# elif 1 <= m <= 5:
#   vv = m * 10
# elif 6<= m <=30:
#   vv = m + 50
# elif 35 <= m <= 70:
#   vv = (m - 30) / 5 + 80
# elif 70 < m:
#   vv = 89

# print(vv if type(vv) is str else round(vv))

# 参考
m = int(input())
if 100 < m:
  vv = 0
elif m <= 5000:
  vv = m // 100
elif m <= 30000:
  vv = m // 1000 + 50
elif m <= 70000:
  vv = (m // 1000 - 30) // 5 + 80
elif 70000:
  vv = 89
print("%02d" % vv)