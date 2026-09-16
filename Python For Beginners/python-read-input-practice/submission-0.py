def add_two_numbers() -> int:
    n = input()
    num = n.split(",")
    sum = 0
    for n in num:
        sum += int(n) 
    return sum


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
