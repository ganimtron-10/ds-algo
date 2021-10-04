class PriorityQueue:
    '''
    Creating A Priority Queue.

    Functions
    ---------
    enqueue: add element to queue.
    dequeue: remove element from queue.
    isempty: checks whether queue is empty.
    print: prints itself.
    '''
    def __init__(self,*elements):
        self.list = list(elements)

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
    
    def isempty(self):
        return not bool(len(self.list))

    def print(self):
        self.list.sort()
        print(self.list)

if __name__ == "__main__":
    q = PriorityQueue()
    q.enqueue("1", 6)
    q.print()
    q.enqueue("2", 1)
    q.print()
    q.enqueue("3", 2)
    q.print()
    q.enqueue("4", 1)
    q.print()
    q.dequeue()
    q.print()
    q.dequeue()
    q.print()
