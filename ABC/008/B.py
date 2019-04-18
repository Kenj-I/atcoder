# import collections

# N = int(input())
# S = [input() for _ in range(N)]

# counts = collections.Counter(S)
# ansName = ''
# ansCount = 0
# for name, count in counts.items():
#   if ansCount < count:
#     ansName = name
#     ansCount = count
# print(ansName)



# reffer https://atcoder.jp/contests/abc008/submissions/4434904
import collections

N = int(input())
S = [input() for _ in range(N)]
print(collections.Counter(S).most_common()[0][0])