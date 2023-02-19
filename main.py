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
            opening_brackets_stack.append(Bracket(next, i))
        elif next in ")]}":
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
                return i + 1
            opening_brackets_stack.pop()
    if opening_brackets_stack:
        return opening_brackets_stack[0].position + 1
    return "Success"



def main():
    
    while True:
        vai = input().strip().upper()
        if vai == "I":
            iekavas = input()
            break
        elif vai == "F":
            fails = input()
            if os.path.exists(fails):
                with open(fails) as i:
                    iekavas = i.read()
                break
            else:
                print("wrong file")
        else:
            print("wrong input format")
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    #if mismatch == "Success":
        #print("Success")
    #else:
        #print(mismatch)
        

if __name__ == "__main__":
    main()
