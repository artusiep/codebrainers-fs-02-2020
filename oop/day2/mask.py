germs = ["bacteria", "viruses", "fungus"]
filtered_germs = filter(lambda x: x != "viruses", germs)

print()

# Lazy Evaluation

if True:
    exit()

print(list(filtered_germs))

