grocery = ["milk", "bread", "eggs"]

def add_item(item):
    grocery.append(item)
    print(grocery)

add_item("butter")

def remove_last_item():
    grocery.pop()
    print(grocery)

remove_last_item()     

x = lambda item : print("Item:" + item)
for item in grocery:
    x(item)
    
def count_characters(items):
    if not items:              
        return 0
    return len(items[0]) + count_characters(items[1:])

print(count_characters(grocery))
   
print(count_characters(["milk", "bread"]))   