## to identify the members list who are above 18.
members = [
    {"name": 'Boobalan', 'age': '26'},
    {"name": 'kavitha', 'age': '42'},
    {"name": 'Dhiyan', 'age': '14'},
    {"name": 'Dhanyasri', 'age': '16'}
]


age_above_18 = list(map(lambda p: p['name'], filter(lambda p: int(p['age']) >= 18, members)))

print(age_above_18)
