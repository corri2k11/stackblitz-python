import random

def generate_random_numbers(count, min_value=1, max_value=1000):
    """Generate a list of random numbers."""
    return [random.randint(min_value, max_value) for _ in range(count)]

def main():
    """Main function to generate and display 200 random numbers in descending order."""
    print("Generating 200 random numbers (1-1000) in descending order:")
    print("=" * 60)
    
    # Generate 200 random numbers between 1 and 1000
    random_numbers = generate_random_numbers(200, 1, 1000)
    
    # Sort the numbers in descending order
    sorted_numbers = sorted(random_numbers, reverse=True)
    
    # Display the numbers in a formatted way (10 per line)
    for i, number in enumerate(sorted_numbers):
        print(f"{number:4d}", end="  ")
        if (i + 1) % 10 == 0:
            print()  # New line after every 10 numbers
    
    print(f"\n\nTotal numbers generated: {len(sorted_numbers)}")
    print(f"Smallest number: {min(sorted_numbers)}")
    print(f"Largest number: {max(sorted_numbers)}")
    print(f"Average: {sum(sorted_numbers) / len(sorted_numbers):.2f}")

if __name__ == "__main__":
    main()