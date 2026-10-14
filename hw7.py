inventory = []

def add_item(item):
    inventory.append(item)
        
def count_items(items):
    if not items:
        return 0
    return 1 + count_items(items[1:])

show_item = lambda item: print(f"item in Stock: {item}")

def main():
    add_item("dog food")
    add_item("cat toy")
    add_item("bird cage")
    add_item("fish tank")
    
    for item in inventory:
        show_item(item)
    
    total = count_items(inventory)
    print(f"Total items in stock: {total}")
    
main()    

