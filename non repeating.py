def unique_element(input_list):

        counts = {}
        for element in input_list:
            counts[element] = counts.get(element, 0) + 1


        for element in input_list:
            if counts[element] == 1:
                return element


        return "No unique element found."

my_list = [7, 5, 2, 4, 5, 7, 8, 2, 9]

first_unique = unique_element(my_list)

print(f"The list is: {my_list}")
print(f"The first non-repeating element is: {first_unique}")