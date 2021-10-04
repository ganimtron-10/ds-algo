from queue import Queue

def bfs(graph, start):
    queue = Queue(start)
    result = []
    result.append(start)
    while not queue.isempty():
        point = queue.dequeue()
        for i in graph[point]:
            if i in result:
                continue
            queue.enqueue(i)
            result.append(i)
    return result

if __name__ == "__main__":
    g = {
        1:[2,4],
        2:[1,3,4,5],
        3:[2,5],
        4:[1,2,5],
        5:[2,3,4]
    }

    print(bfs(g,1))