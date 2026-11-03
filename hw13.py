import os

FILENAME = "students.txt"


def read_names():
    with open(FILENAME, "r") as f:
        return [line.strip() for line in f if line.strip()]
    
def main():
    if os.path.exists(FILENAME):
        existing = read_names()
        print("Existing student names: ")
        if existing:
            for i, name in enumerate(existing, 1):
                print(f" {i}. {name}")
        else:
            print(" (file is empty)")
        print()
        
    while True:
        try:
            count = int(input("How many student names do you want to add? "))
            if count < 0:
                print("Please enter a non-negative number.")
                continue
            break
        except ValueError:
            print("Please enter a valid whole number.")
            
    new_names = []
    for i in range(1, count + 1):
        name = input(f"Enter name {i}: ").strip()
        new_names.append(name)
        
    with open(FILENAME, "a") as f:
        for name in new_names:
            f.write(name + "\n")

    print("\nUpdated list of all student names:")
    for i, name in enumerate(read_names(), 1):
        print(f" {i}. {name}")
        
        
if __name__ == "__main__":
    main()