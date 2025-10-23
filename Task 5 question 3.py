#Write a list comprehension that creates a new list of squares of even numbers from a given list,
# using a lambda function to check for even numbers.

Even_numbers = lambda n: n % 2 == 0

input_numbers = [1,2,3,4,5,6,7,8,9,10]

squared_even_of_input_number = [n**2 for n in input_numbers if Even_numbers(n)]


print(f"Squared even numbers is {squared_even_of_input_number}")