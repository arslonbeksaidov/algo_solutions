class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()

    def push(self, data):
        self.stack.append(data)
        return True

    def peek(self):
        if self.isEmpty():
            return "Empty"
        return self.stack[-1]

stack = Stack()
stack.push(34)
stack.push(34)
stack.push(34)
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
print(stack.peek())
