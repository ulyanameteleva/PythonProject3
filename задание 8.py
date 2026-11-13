n = int(input())
questions = 0
max_numbers = 1
while max_numbers < n:
    max_numbers = max_numbers * 2
    questions = questions + 1
print(questions)