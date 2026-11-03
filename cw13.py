import os

item = input("Enter the name of a new item: ").strip()

if os.path.exists("items.txt"):
    with open("items.txt", "a") as f:
        f.write(item + "\n")
else:
    with open("items.txt", "w") as f:
        f.write(item + "\n")
        
print("\nAll items:")
with open("items.txt", "r") as f:
    print(f.read())
    
    