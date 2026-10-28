import random
import math


names_input = input("Enter names of invited guests (comma-separated): ")


names = [n.strip() for n in names_input.split(",") if n.strip()]


unique_names = []
seen = set()
for n in names:
    if n.lower() not in seen:
        seen.add(n.lower())
        unique_names.append(n)


chosen = random.choice(unique_names)
reversed_name = chosen[::-1]


total = len(unique_names)
root = round(math.sqrt(total))

print("Unique guest list:", unique_names)
print("Selected name:", chosen)
print("Reversed name:", reversed_name)
print("Total unique names:", total)
print("Square root (rounded):", root)