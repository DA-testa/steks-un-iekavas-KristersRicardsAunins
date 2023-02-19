# python3

def find_mismatch(text):
    opening_brackets = ['[', '{', '(']
    closing_brackets = [']', '}', ')']
    stack = []
    for i, char in enumarate(text):
        if char in opening_brackets:
            stack.append((char, i))
        elif char in closing_brackets:
            if not stack:
                return i + 1
            last_opening_bracket, _ = stack.pop()
            if (last_opening_bracket == '[' and char != ']') or (last_opening_bracket == '{' and char != '}') or (last_opening_bracket == '(' and char != ')'):
                return i + 1
            if stack:
                _, index = stack.pop()
                return index + 1
            return "Success"
        
def main():
    text = input()
    for i in text:
        print(find_mismatch(i))
        
if __name__ == "__main__":
    main()
