questions =[10,501,22,37,100,999,87,351]
even_list = []
odd_list = []

for x in questions:
    if x % 2 == 0:
        even_list.append(x)
    else:
        odd_list.append(x)
print("Even number",even_list)
print("Odd number",odd_list)

