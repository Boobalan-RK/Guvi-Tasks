def is_prime(x):
    is_prime = True
    for i in range(2, x):
        if x % i == 0:
            is_prime = False
            break
    return is_prime

questions =[10,501,22,37,100,999,87,351]
prime_list = []
non_prime_list = []
for x in questions:
    if is_prime(x):
        prime_list.append(x)
    else:
        non_prime_list.append(x)
print("Prime numbers:", prime_list)
print("Non-prime numbers:", non_prime_list)

