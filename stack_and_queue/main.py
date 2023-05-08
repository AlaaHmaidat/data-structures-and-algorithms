from stack import stack

stack1 = stack()
stack1.push(1)
stack1.push(2)
stack1.push(3)
print("peek ",stack1.peek())
print("size ",stack1.get_size())
print("is_empty ",stack1.is_empty())
print("pop ",stack1.pop()) # 3
print("pop ",stack1.pop()) # 2
print("pop ",stack1.pop()) # 1
print("pop ",stack1.pop()) # This stack is empty

print("The size = ",stack1.get_size())
print("peek ",stack1.peek())
print("is_empty ",stack1.is_empty())

