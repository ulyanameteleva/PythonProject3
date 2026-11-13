n = int(input())
for num in range(2, n + 1):
    sum_div = 0
    for d in range(1, num // 2 + 1):
        if num % d == 0:
            sum_div = sum_div + d
    if sum_div == num:
        print(num)