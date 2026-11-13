previous = float(input())
count = 0
while True:
    current = float(input())
    if current == 0:
        break
    if current < previous:
        count = count + 1
    prev = current
print(count)