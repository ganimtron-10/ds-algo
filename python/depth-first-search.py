from stack import Stack

def dfs(graph, start):
    '''
    Using Depth First Search to traverse Graph.
    Method: iterative

    Parameter
    ---------
    graph: (dictionary of list)
    A dictionary of list on which we are going to apply dfs
    
    start: (key of dictionary)
    The element from which we are starting the traverse

    Returns
    -------
    (list) List of points in traverse order
    '''
    result = []
    result.append(start)
    stack = Stack(start)
    point = start
    while not stack.isempty():
        for i in graph[point]:
            if i in result:
                continue
            else:
                result.append(i)
                stack.push(i)
                point = i
                break
        else:
            point = stack.pop()
    return result

if __name__ == "__main__":
    g = {
        1:[2,4],
        2:[1,3,4,5],
        3:[2,5],
        4:[1,2,5],
        5:[2,3,4]
    }

    print(dfs(g,1))