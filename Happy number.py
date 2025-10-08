def is_happy_num(num):
    while num > 9:
        num = sum([int(d) * int(d) for d in str(num)])
    return num == 1

question = [10, 501, 22, 37, 100, 999, 87, 351]
happy_number_list = []
for x in question:

    if is_happy_num(x):
        happy_number_list.append(x)

print("Happy List is: ", happy_number_list)