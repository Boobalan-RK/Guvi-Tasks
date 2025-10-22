from _functools import reduce

numbers = [4,3,6,7]


product = reduce(lambda x,y: x*y, numbers)
print(f"The list of number  is {numbers}")
print(f" the product of number  is {product}")