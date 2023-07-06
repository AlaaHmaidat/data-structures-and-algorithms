import pytest
from hashtable import Hashtable

@pytest.fixture
def hashtable():
    return Hashtable()

def test_setting_key_and_value_results_in_value_being_in_hashtable(hashtable):
    """
    Test that setting a key/value pair in the hashtable correctly stores the value.
    """
    hashtable.set("A", 70)
    assert hashtable.get("A") == 70

def test_retrieving_based_on_key_returns_value_stored(hashtable):
    """
    Test that retrieving a value based on a key returns the correct value stored in the hashtable.
    """
    hashtable.set("A", 70)
    assert hashtable.get("A") == 70

def test_returns_null_for_key_that_does_not_exist(hashtable):
    """
    Test that retrieving a key that does not exist in the hashtable returns None.
    """
    assert hashtable.get("X") is None

def test_returns_list_of_all_unique_keys_in_hashtable(hashtable):
    """
    Test that the keys() method returns a list of all unique keys in the hashtable.
    """
    hashtable.set("A", 70)
    hashtable.set("B", 90)
    hashtable.set("C", 80)
    assert set(hashtable.keys()) == {"A", "B", "C"}

def test_successfully_handle_collision_within_hashtable(hashtable):
    """
    Test that the hashtable can handle collisions correctly and retrieve values from buckets with collisions.
    """
    hashtable.set("A", 70)
    hashtable.set("B", 90)
    hashtable.set("C", 80)
    hashtable.set("D", 60)
    hashtable.set("E", 50)
    hashtable.set("F", 40)
    hashtable.set("G", 30)
    hashtable.set("H", 20)
    hashtable.set("I", 10)
    assert hashtable.get("A") == 70
    assert hashtable.get("B") == 90
    assert hashtable.get("C") == 80
    assert hashtable.get("D") == 60
    assert hashtable.get("E") == 50
    assert hashtable.get("F") == 40
    assert hashtable.get("G") == 30
    assert hashtable.get("H") == 20
    assert hashtable.get("I") == 10

def test_successfully_retrieve_value_from_bucket_with_collision(hashtable):
    """
    Test that the hashtable can retrieve a value from a specific bucket within the hashtable that has a collision.
    """
    hashtable.set("A", 70)
    hashtable.set("B", 90)
    hashtable.set("C", 80)
    hashtable.set("D", 60)
    hashtable.set("E", 50)
    hashtable.set("F", 40)
    hashtable.set("G", 30)
    hashtable.set("H", 20)
    hashtable.set("I", 10)
    assert hashtable.get("G") == 30

def test_successfully_hash_key_to_in_range_value(hashtable):
    """
    Test that the hash method correctly hashes a key to an index within the range of the hashtable.
    """
    key = "Test"
    index = hashtable.hash(key)
    assert index >= 0 and index < hashtable.size
