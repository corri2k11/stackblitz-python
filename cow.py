def draw_cow():
    """Draw an ASCII art cow with a speech bubble saying 'Mooo'."""
    cow_art = """
     ______
    < Mooo >
     ------
            \\   ^__^
             \\  (oo)\\_______
                (__)\\       )\\/\\
                    ||----w |
                    ||     ||
    """
    print(cow_art)

def main():
    """Main function to display the cow."""
    print("Here's your ASCII cow:")
    print("=" * 30)
    draw_cow()
    print("=" * 30)

if __name__ == "__main__":
    main()