# python3


from collections import namedtuple
import os
Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i + 1))
        elif next in ")]}":
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
                return i + 1
            opening_brackets_stack.pop()
    if opening_brackets_stack:
        return opening_brackets_stack[0].position
    return "Success"


def main():
    while True:
        vai = input().strip().upper()
        if vai == "I":
            text = input()
            break
        elif vai == "F":
            fails = input()
            if os.path.exists(fails):
                with open(fails) as i:
                    text = i.read()
                break
            else:
                print()
        else:
            print()
            
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    if mismatch == "Success":
        print("Success")
    else:
        print(mismatch)
        

if __name__ == "__main__":
    main()
