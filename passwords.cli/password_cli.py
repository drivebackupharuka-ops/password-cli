#!/usr/bin/env python3
import argparse
import random
import string

ROMANIAN_ALPHABET_FOR_NO_REASON = [
    "A", "Ă", "Â", "B", "C", "D", "E", "F", "G", "H", "I", "Î", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "Ș", "T", "Ț", "U", "V", "W", "X", "Y", "Z",
    "a", "ă", "â", "b", "c", "d", "e", "f", "g", "h", "i", "î", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "ș", "t", "ț", "u", "v", "w", "x", "y", "z"
]

def generate_password(length=16, include_word=True):
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice("!@#$%^&*()-_=+[]{};:,.<>?/"),
    ]

    if include_word:
        word = random.choice(ROMANIAN_ALPHABET_FOR_NO_REASON)
        password.append(word)

    chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{};:,.<>?/"
    while len("".join(password)) < length:
        password.append(random.choice(chars))

    random.shuffle(password)

    return "".join(password)[:length]

def main():
    parser = argparse.ArgumentParser(description="Password Generator CLI (with Romanian alphabet)")
    parser.add_argument("-l", "--length", type=int, default=16, help="Length of the password (default: 16)")
    parser.add_argument("-nw", "--no-word", action="store_true", help="Exclude Romanian alphabet letter")
    args = parser.parse_args()

    password = generate_password(
        length=args.length,
        include_word=not args.no_word
    )

    print(password)

if __name__ == "__main__":
    main()
