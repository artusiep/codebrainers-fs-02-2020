# To see more: https://www.programiz.com/python-programming/dictionary-comprehension

# Dict Comprehension

accounts = {'Artur': 10, 'Karolina': 1000, 'Michal': 1000}

new_accounts = {name: balance * 1.01 for (name, balance) in accounts.items()}

print(new_accounts)

# Map
# (key, value)
new_accounts2 = dict(map(lambda items: (items[0], items[1] * 1.01), accounts.items()))
print(new_accounts2)