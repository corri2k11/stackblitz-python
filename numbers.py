def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def generate_primes(limit):
    """Generate all prime numbers up to the given limit."""
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def main():
    """Main function to display prime numbers from 1 to 1000."""
    print("Prime numbers from 1 to 1000:")
    print("=" * 40)
    
    primes = generate_primes(1000)
    
    # Display primes in a formatted way (10 per line)
    for i, prime in enumerate(primes):
        print(f"{prime:4d}", end="  ")
        if (i + 1) % 10 == 0:
            print()  # New line after every 10 numbers
    
    print(f"\n\nTotal prime numbers found: {len(primes)}")

if __name__ == "__main__":
    main()