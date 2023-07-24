import pytest

from hashmap_left_join import Hashtable,left_join

def test_left_join_basic():
    hashmap = Hashtable()
    hashmap2 = Hashtable()

    hashmap.set("A", 70)
    hashmap.set("B", 90)
    hashmap.set("C", 80)
    hashmap.set("E", 60)

    hashmap2 = Hashtable()
    hashmap2.set("x", 70)
    hashmap2.set("C", 2)
    hashmap2.set("A", 3)

    result = left_join(hashmap, hashmap2)
    expected = [['A', 70, 3], ['B', 90, None], ['C', 80, 2], ['E', 60, None]]
    assert result == expected

def test_left_join_empty_left_hashmap():
    result = left_join({}, {"x": 1, "y": 2})
    assert result == None

def test_left_join_empty_hashmaps():
    hashmap1 = Hashtable()
    hashmap2 = Hashtable()

    result = left_join(hashmap1, hashmap2)
    assert result == []