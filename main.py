# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(next, i+1)
            pass

        if next in ")]}":
            # Process closing bracket, write your code here
            if not opening_brackets_stack or not opening_brackets_stack[-1].Matchc(next) :
                return i+1
            opening_brackets_stack.pop()
            pass


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
if not opening_brackets_stack:
    return 'Success'
else:
    return stack[-1].position

if __name__ == "__main__":
    main()
