fruits = ["apple", "orange", "mango"]
vegetables = ["brocolli", "carrot", "tomato"]
beverages = ["water", "milk", "coffee"]

fruits.append("watermelon")

vegetables.insert(1, "spinach")

beverages.pop()

inventory = [fruits, vegetables, beverages]

print(fruits[0:2])

print(vegetables[-1])

fruit_lengths = [len(fruit) for fruit in fruits]
print(fruit_lengths)

print("water" in beverages)

in_tuple = ("apple", "brocolli", "water")
print(in_tuple)