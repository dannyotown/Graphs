"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """

        # create an empty queue and enqueue the starting_vertex
        que = []
        # create an empty set to track visited verticies
        que.insert(0, starting_vertex)
        tracker = set()
        # while the queue is not empty:
        while len(que) != 0:
            # get current vertex
            current = que[-1]
            que.pop()
            # check if current vertex has not been visited
            if current not in tracker:
                # mark the current vertex as visited
                tracker.add(current)
                # print the current vertex
                print(current)
                for values in self.vertices[current]:
                    que.insert(0, values)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create an empty stack and pop the starting_vertex
        stack = []
        # create an empty set to track visited verticies
        stack.insert(0, starting_vertex)
        tracker = set()
        # while the stack is not empty:
        while len(stack) != 0:
            # get current vertex
            current = stack[0]
            stack.pop(0)
            # check if current vertex has not been visited
            if current not in tracker:
                # mark the current vertex as visited
                tracker.add(current)
                # print the current vertex
                print(current)
                for values in self.vertices[current]:
                    stack.insert(0, values)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        pass  # TODO

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create an empty queue and enqueue the starting_vertex
        que = []
        que.append([starting_vertex])
        # create an empty set to track visited verticies
        tracker = set()
        # while the queue is not empty:
        while len(que) != 0:
            # get current vertex path
            current_path = que[0]
            current_vertex = current_path[-1]
            que.pop(0)
            # check if current vertex has not been visited
            if current_vertex not in tracker:
                # mark the current vertex as visited
                tracker.add(current_vertex)
                # Check if the current vertex is destination and return
                if current_vertex == destination_vertex:
                    return current_path
                for value in self.vertices[current_vertex]:
                    que.append(current_path + [value])

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create an empty stack and start at the starting_vertex
        stack = []
        stack.insert(0, [starting_vertex])
        # create an empty set to track visited verticies
        tracker = set()
        # while the stack is not empty:
        while len(stack) != 0:
            # get current vertex path
            current_path = stack[-1]
            current_vertex = current_path[-1]
            stack.pop(-1)
            # check if current vertex has not been visited
            if current_vertex not in tracker:
                # mark the current vertex as visited
                tracker.add(current_vertex)
                # Check if the current vertex is destination and return
                if current_vertex == destination_vertex:
                    return current_path
                for value in self.vertices[current_vertex]:
                    stack.insert(0, current_path + [value])

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
