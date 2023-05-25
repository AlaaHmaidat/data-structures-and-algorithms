#  stack queue brackets
Validate the balance of brackets in a given string.

## Whiteboard Process
![WhiteboardWorkflow01](../img/stack%20queue%20brackets.jpg)

## Approach & Efficiency

1. Initialize an empty stack to store the opening brackets encountered.
2. Define the lists `opening_brackets` and `closing_brackets` containing the respective opening and closing brackets.
3. Create a dictionary `brackets_map` that maps each closing bracket to its corresponding opening bracket.
4. Perform the following checks:
    - If the input `string` is not of type `str`, return the string `'Argument is not a string'`.
    - If the length of the input `string` is 0 (empty string), return the string `'Empty string'`.
5. Initialize a flag `opening_found` to False to keep track of whether any opening brackets are found.
6. Iterate through each character `char` in the `string`:
    - If `char` is an opening bracket, set `opening_found` to True and push `char` onto the stack.
    - If `char` is a closing bracket:
        - If the stack is empty or the corresponding opening bracket for `char` is not at the top of the stack, return False (brackets are not balanced).
        - Otherwise, pop the top element from the stack as the brackets are balanced.
7. After the loop, check if `opening_found` is still False. If so, return the string `'No opening brackets found'`.
8. Finally, return True if the stack is empty (all brackets are balanced), otherwise return False.

    
### Big O
The time complexity of the validate_brackets function is O(n), and the space complexity is also O(n), where n is the length of the input string.

## Solution
Click [here](./stack_queue_brackets.py)
