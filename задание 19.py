n = int(input())
total_dots = 0
for a in range(0, n + 1):
    for b in range(a, n + 1):
        total_dots = total_dots + a + b
print(total_dots)
