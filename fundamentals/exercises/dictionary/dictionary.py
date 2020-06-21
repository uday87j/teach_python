#!python3
import sys
import os
import argparse

def main():
    parser = argparse.ArgumentParser(description="Dictionary")
    parser.add_argument("--is_word", type=str, help="Find if this word exists in dictionary")
    parser.add_argument("--word", type=str, help="Find this word in dictionary")
    parser.add_argument("--words", type=str, help="Find these words in dictionary")
    parser.add_argument("--after", type=int, help="Print N words after a word is found")
    parser.add_argument("--before", type=int, help="Print N words before a word is found")
    args = parser.parse_args()

    if args.is_word:
        print(args.is_word)
        # Add your code here for Part 1

    if args.word:
        print(args.word)
        # Add your code here for Part 1
    
    if args.words:
        print(args.words)
        # Add your code here for Part 2

    if args.after:
        print(args.after)
        # Add your code here for Part 3

    if args.before:
        print(args.before)
        # Add your code here for Part 3

if __name__ == "__main__":
    main()