def first_digit_last_digit(n):
    num_str = str(n)
    first_digit = int(num_str[0])
    last_digit = int(num_str[-1])

    return first_digit + last_digit


number = 21012024
result = first_digit_last_digit(number)
print(f"The first digit of {number} is {result}")



