#!/usr/bin/env python3
import argparse
import random
import string

def generate_password(length=12, use_digits=True, use_specials=True):
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_specials:
        chars += "!@#$%^&*()-_=+[]{};:,.<>?/"

    return ''.join(random.choice(chars) for _ in range(length))

def main():
    parser = argparse.ArgumentParser(description="Password Generator CLI")
    parser.add_argument("-l", "--length", type=int, default=12, help="Length of the password (default: 12)")
    parser.add_argument("-nd", "--no-digits", action="store_true", help="Exclude digits")
    parser.add_argument("-ns", "--no-specials", action="store_true", help="Exclude special characters")
    args = parser.parse_args()

    password = generate_password(
        length=args.length,
        use_digits=not args.no_digits,
        use_specials=not args.no_specials
    )

    print(password)

if __name__ == "__main__":
    main()
