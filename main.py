# python3


from collections import namedtuple


Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i))
        if next in ")]}":
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
                return i + 1
            opening_brackets_stack.pop()
    if opening_brackets_stack:
        return opening_brackets_stack[0].position + 1
    return "Success"



def main():
    textc = input()
    if textc.upper() == "F":
        file_name = input()
        if not os.path.isfile(file_name):
            print("Error")
            return
        with open(file_name, 'r') as f:
            text = f.read()
        elif input_choice.upper() == "I":
            text = input():
        else:
            print("Error")
            return
        
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    if mismatch == "Success":
        print("Success")
    else:
        print(mismatch)
        

if __name__ == "__main__":
    main()
