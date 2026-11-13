n, k, r = map(int, input().split())
day = 1
while n < r:
    n = n + n * (k / 100)
    day = day + 1
print(day)