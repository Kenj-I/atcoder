import math
N = int(input())
per = [int(input()) for i in range(5)]
print(math.ceil(N / min(per)) + 4)