import re

def validate_title(title):
    if not title.strip() or not re.fullmatch(r"[A-Za-z]+", title):
        raise ValueError("Invalid title: use only alphabets and spaces.")
    return title.strip()

def validate_year(year):
    if not re.fullmatch(r"(19|20)\D{2}", year):
        raise ValueError("Invalid year: enter a 4-digit year starting with 19 or 20.")
    return int(year)

def main():
    print("=== Mini Library System ===")
    try:
        title = validate_title(input("Enter book title: "))
        year = validate_title(input("Enter publication year: ").strip())
        print(f"\nBook added successfully: '{title}' ({year})")
    except ValueError as error:
        print(f"\nError: {error}")
    except (EOFError, KeyboardInterrupt):
        print("\nError: Input was interrupted.")
    finally:
        print("Thank you for using the Mini Library System.")
        
        
if __name__ == "__main__":
    main()