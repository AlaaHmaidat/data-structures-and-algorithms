def validate_brackets(string):
    """
    Validate the balance of brackets in a given string.

    Arguments:
    - string (str): The string to validate.

    Returns:
    - True if the brackets in the string are balanced.
    - False if the brackets in the string are not balanced.
    - 'Argument is not a string' if the input is not a string.
    - 'Empty string' if the input string is empty.
    - 'No opening brackets found' if there are no opening brackets in the string.
    """

    stack = []
    opening_brackets = ["[", "{", "("]
    closing_brackets = ["]", "}", ")"]
    brackets_map = {')': '(', ']': '[', '}': '{'}

    
    if type(string) != str: # Edge case
        return 'Argument is not a string'
    elif len(string) == 0: # Edge case
        return 'Empty string'

    opening_found = False

    for char in string:
        if char in opening_brackets:
            opening_found = True
            stack.append(char)
        elif char in closing_brackets:
            if not stack or brackets_map[char] != stack.pop():
                return False

    if not opening_found: # Edge case
        return 'No brackets found'

    return len(stack) == 0

if __name__ == "__main__":
    print(validate_brackets('({})'))