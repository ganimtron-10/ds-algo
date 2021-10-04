class Queue:
    '''
    Creating A Queue.

    Functions
    ---------
    enqueue: add element to queue.
    dequeue: remove element from queue.
    isempty: checks whether queue is empty.
    print: prints itself.
    '''
    def __init__(self,*elements):
        self.list = list(elements)

    def enqueue(self,*elements):
        for element in elements:
            self.list.append(element)

    def dequeue(self):
        return self.list.pop(0)
    
    def isempty(self):
        return not bool(len(self.list))

    def print(self):
        print(self.list)


if __name__ == "__main__":
    q = Queue()
    print(q.isempty())
    q.enqueue(2,2,23,3,4,5,5)
    q.print()
    print(q.isempty())
    q.dequeue()
    q.print()