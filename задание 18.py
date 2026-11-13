x = int(input())
count = 0
for a in range(1, x + 1):
    for b in range(a, x + 1):
        if a * a + b * b == x:
            count = count + 1
print(count)