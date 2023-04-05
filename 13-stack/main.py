from stack import Stack

if __name__ == "__main__":
    stack = Stack()

    for i in range(6):
        stack.push(i)
    for i in range(6):
        stack.pop()
