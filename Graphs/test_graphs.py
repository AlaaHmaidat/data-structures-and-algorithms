import pytest
from graphs import Graphs


def test_get_vertices_if_graph_empty():
    graph = Graphs()

    # a = graph.add_vertex("A")
    # b = graph.add_vertex("B")
    # c = graph.add_vertex("C")
    # d = graph.add_vertex("D")

    # graph.add_edge(a,b)
    # graph.add_edge(a,c)
    # graph.add_edge(c,b)
    # graph.add_edge(d,b)
    # graph.add_edge(d,c)

    # neighbors = graph.get_vertices()

    actual = graph.get_vertices()
    expected = []
    assert actual == expected

def test_vertex_successfully_added_to_graph():
    graph = Graphs()

    a = graph.add_vertex("A")
    # b = graph.add_vertex("B")
    # c = graph.add_vertex("C")
    # d = graph.add_vertex("D")

    # graph.add_edge(a,b)
    # graph.add_edge(a,c)
    # graph.add_edge(c,b)
    # graph.add_edge(d,b)
    # graph.add_edge(d,c)

    # neighbors = graph.get_vertices()

    actual = graph.__str__()
    expected = 'A: \n'
    assert actual == expected

def test_edge_successfully_added_to_graph():
    graph = Graphs()

    a = graph.add_vertex("A")
    b = graph.add_vertex("B")
    # c = graph.add_vertex("C")
    # d = graph.add_vertex("D")

    graph.add_edge(a,b)
    # graph.add_edge(a,c)
    # graph.add_edge(c,b)
    # graph.add_edge(d,b)
    # graph.add_edge(d,c)

    # neighbors = graph.get_vertices()

    actual = graph.get_neighbors(a)
    expected = [('B', 0)]
    assert actual == expected

def test_collection_of_vertices_properly_retrieved_from_graph():
    graph = Graphs()

    a = graph.add_vertex("A")
    b = graph.add_vertex("B")
    c = graph.add_vertex("C")
    d = graph.add_vertex("D")

    graph.add_edge(a,b)
    # graph.add_edge(a,c)
    # graph.add_edge(c,b)
    # graph.add_edge(d,b)
    # graph.add_edge(d,c)

    # neighbors = graph.get_vertices()

    actual = graph.get_neighbors(a)
    expected = [('B', 0)]
    assert actual == expected