N = int(input())
list = sorted(list(set([int(input()) for _ in range(N)])))
print(list[-2])

# reffer https://atcoder.jp/contests/abc009/submissions/4632268
# print(sorted(set(map(int,open(0).read().split()[1:])))[-2])
