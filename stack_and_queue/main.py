from stack import stack

stack1 = stack()
stack1.push(1)
stack1.push(2)
stack1.push(3)

print("size",stack1.get_size())
print(stack1.is_empty())
print(stack1.pop()) # 3
print(stack1.pop()) # 2
print(stack1.pop()) # 1
print(stack1.pop()) # This stack is empty

print("The size = ",stack1.get_size())
print(stack1.peek())
print(stack1.is_empty())

