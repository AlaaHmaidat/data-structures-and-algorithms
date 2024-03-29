class Node:
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return self.value


class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight


class Graphs:
    def __init__(self):
        self.dict_list = {}

    def add_vertex(self, value):
        '''Arguments: value
        Returns: The added vertex
        Add a vertex to the graph'''
        new_vertex = Node(value)
        self.dict_list[new_vertex] = []
        return new_vertex

    def add_edge(self, vertex1, vertex2, weight=0):
        '''Arguments: 2 vertices to be connected by the edge, weight (optional)
        Returns: nothing
        Adds a new edge between two vertices in the graph
        If specified, assign a weight to the edge
        Both vertices should already be in the Graph'''
        if not vertex1 in self.dict_list.keys():
            return 'This vertex does not exist'

        if not vertex2 in self.dict_list.keys():
            return 'This vertex does not exist'

        edge1 = Edge(vertex2, weight)
        self.dict_list[vertex1].append(edge1)

        edge2 = Edge(vertex1, weight)
        self.dict_list[vertex2].append(edge2)

    def get_vertices(self):
        '''Arguments: none
        Returns all of the vertices in the graph as a collection (set, list, or similar)
        Empty collection returned if there are no vertices'''

        collection = []

        # if len(self.dict_list) == 0:
        #     return 'There are no vertice'
        for i in self.dict_list:
            collection.append(i)

        return collection

    def get_neighbors(self, vertex):
        '''Arguments: vertex
        Returns a collection of edges connected to the given vertex
        Include the weight of the connection in the returned collection
        Empty collection returned if there are no vertices'''

        if vertex not in self.dict_list:
            return 'There are no vertices'

        length = len(self.dict_list[vertex])
        collection = []
        for i in range(length):
            neighbor = self.dict_list[vertex][i].vertex.value
            weight = self.dict_list[vertex][i].weight

            collection.append((neighbor, weight))

        return collection

    def size(self):
        '''Arguments: none
        Returns the total number of vertices in the graph
        0 if there are none'''

        return len(self.dict_list)

    def __str__(self):
        output = ''
        for vertex in self.dict_list.keys():
            output += f'{vertex}: '
            for edge in self.dict_list[vertex]:
                output += f'{edge.vertex} --> '

            output += '\n'

        return output


if __name__ == '__main__':
    graph = Graphs()

    a = graph.add_vertex("A")
    b = graph.add_vertex("B")
    c = graph.add_vertex("C")
    d = graph.add_vertex("D")

    graph.add_edge(a, b)
    graph.add_edge(a, c)
    graph.add_edge(c, b)
    graph.add_edge(d, b)
    graph.add_edge(d, c)

    neighbors = graph.get_neighbors(a)

    print(graph)
    print('neighbors', neighbors)