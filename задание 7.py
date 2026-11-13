ans = int(input())
current = 1
while current < ans:
    current = current * 2
if current == ans:
    print("верно")
else:
    print("неверно")