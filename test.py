'''from Test_code import add


result = add(1, 2)
print(result)'''

def add (*args):
    total = 0
    for num in args:
        total +=num


    return total

print(add(1, 2,2))
