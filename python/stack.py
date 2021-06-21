class Stack:
    '''
    Creating A Stack.

    Functions
    ---------
    push: add element to stack.
    pop: remove element from stack.
    print: prints itself.
    '''
    def __init__(self,*elements):
        self.list = list(elements)

    def push(self,*elements):
        for element in elements:
            self.list.append(element)

    def pop(self):
        return self.list.pop()

    def isempty(self):
        return not bool(len(self.list))

    def print(self):
        print(self.list)

# s1 = Stack()

# s1.push(5,2,4)
# s1.print()
# s1.pop()
# s1.print()