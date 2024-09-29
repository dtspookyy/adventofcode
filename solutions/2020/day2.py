lines = open("../../input.txt").read().splitlines()

total = 0
for i in lines:
    rule, password = i.split(": ")
    lower, higher = rule.split()[0].split("-")
    letter = rule[-1]

    if password[int(lower) - 1] == letter and password[int(higher) - 1] == letter:
        total = total
    elif password[int(lower) - 1] == letter or password[int(higher) - 1] == letter:
        total += 1

print(total)