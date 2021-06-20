class Queue:
    '''
    Creating A Stack.

    Functions
    ---------
    enqueue: add element to queue.
    dequeue: remove element from queue.
    print: prints itself.
    '''
    def __init__(self):
        self.list = []

    def enqueue(self,*elements):
        for element in elements:
            self.list.append(element)

    def dequeue(self):
        return self.list.pop(1)
    
    def print(self):
        print(self.list)

# q = Queue()

# q.enqueue(2,2,23,3,4,5,5)
# q.print()
# q.dequeue()
# q.print()

class PriorityQueue:
    def __init__(self):
        self.list = []

    def enqueue(self,element,priority):
        if len(self.list) == 0:
            self.list.append([priority,element])
        else:
            for i in range(len(self.list)):
                if priority == self.list[i][0]:
                    self.list[i].append(element)
                    break
                else:
                    self.list.append([priority,element])
                    break

    def dequeue(self):
        return self.list[0].pop(1)
    
    def print(self):
        self.list.sort()
        print(self.list)

# q = PriorityQueue()
# q.enqueue("1", 6)
# q.print()
# q.enqueue("2", 1)
# q.print()
# q.enqueue("3", 2)
# q.print()
# q.enqueue("4", 1)
# q.print()
# q.dequeue()
# q.print()
# q.dequeue()
# q.print()

