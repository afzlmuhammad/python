def get_feedback():
    name = input("Enter your name: ").strip()
    feedback = input("Enter your feedback: ").strip()
    
    if not name:
        raise ValueError("Name cannot be empty.")
    if not feedback:
        raise ValueError("Feedback cannot be empty.")
    
    return name, feedback

def main():
    try:
        name, feedback = get_feedback()
    except ValueError as error:
        print(f"Error: {error}")
    else:
        print(f"\nThank you for your feedback, {name}!")
        print(f"Your feedback: {feedback}")
    finally:
        print("\nThe feedback process has ended.")
        

if __name__ == "__main__":
    main()
    
    
