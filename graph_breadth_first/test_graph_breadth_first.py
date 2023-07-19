import pytest
from graph_breadth_first import Node,Graphs

@pytest.fixture
def graph_instance():
    """Fixture to create and return an instance of the Graphs class."""
    graph = Graphs()

    return graph

def test_breadth_first_simple(graph_instance):
    """Test if the breadth_first method returns the correct order of visited nodes for a simple graph."""
    graph = graph_instance

    a = graph.add_vertex("A")
    b = graph.add_vertex("B")
    c = graph.add_vertex("C")
    d = graph.add_vertex("D")

    graph.add_edge(a, b)
    graph.add_edge(a, c)
    graph.add_edge(c, b)
    graph.add_edge(d, b)
    graph.add_edge(d, c)

    assert graph.breadth_first(a) == ['A', 'B', 'C', 'D']


def test_breadth_first_invalid_node(graph_instance):
    """Test if the breadth_first method handles the case when the starting node is not in the graph."""
    graph = graph_instance

    a = graph.add_vertex("A")
    b = graph.add_vertex("B")
    c = graph.add_vertex("C")

    graph.add_edge(a, b)
    graph.add_edge(a, c)

    invalid_node = Node("X")
    assert graph.breadth_first(invalid_node) == 'The starting vertex does not exist'


def test_breadth_first_disconnected_graph(graph_instance):
    """Test if the breadth_first method correctly handles a disconnected graph with multiple connected components."""
    graph = graph_instance
    
    a = graph.add_vertex("A")
    b = graph.add_vertex("B")
    c = graph.add_vertex("C")
    d = graph.add_vertex("D")

    graph.add_edge(a, b)
    graph.add_edge(c, d)

    assert graph.breadth_first(a) == ['A', 'B']
    assert graph.breadth_first(c) == ['C', 'D']


# Running the tests with pytest
if __name__ == "__main__":
    pytest.main()
