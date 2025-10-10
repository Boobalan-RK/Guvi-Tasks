list_a = [10, 20, 30, 40, 50, 60]
list_b = [50, 65, 85, 20, 30, 120]
list_c = [50, 65, 70, 80, 90]

set_a = set(list_a)
set_b = set(list_b)
set_c = set(list_c)

comman_number = set_a & set_b & set_c

duplicates = list(comman_number)

print(f"List A: {list_a}")
print(f"List B: {list_b}")
print(f"List C: {list_c}")
print(f"\nDuplicates found in all three lists: {duplicates}")
