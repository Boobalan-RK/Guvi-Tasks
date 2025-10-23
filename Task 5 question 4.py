#Write a lambda function to check if a given string is a number.

Given_input = lambda s: s.replace('.', '', 1) .isdigit()

print(f"'123 is number' {Given_input('123')}")
print(f"'abc is number' {Given_input('abc')}")

