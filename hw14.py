import random
import math

customer_input = input("Enter names of customers who placed orders today (comma-separated): ")

# Clean names and drop empty entries
names = [n.strip() for n in customer_input.split(",") if n.strip()]

# Remove duplicates (case-insensitive), keeping original order
unique_cus = []
seen = set()
for n in names:
    if n.lower() not in seen:
        seen.add(n.lower())
        unique_cus.append(n)

total = len(unique_cus)
print("Unique customer list:", unique_cus)

if total < 2:
    print("Need at least 2 unique participants to pick 2 winners.")
else:
    # Shuffle the final list
    random.shuffle(unique_cus)
    print("Shuffled list:", unique_cus)

    # Pick 2 distinct winners
    winners = random.sample(unique_cus, k=2)

    # Reverse each winner's name for fun
    reversed_winners = [w[::-1] for w in winners]

    print("Winners:", winners)
    print("Winners (reversed):", reversed_winners)

print("Total unique participants:", total)
print("Square root of participants (rounded):", round(math.sqrt(total)))