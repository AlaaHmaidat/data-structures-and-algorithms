import pytest
from stack_queue_brackets.stack_queue_brackets import validate_brackets

def test_if_we_send_empty_value():
    """
    Test the behavior of the validate_brackets function when an empty string is provided.
    """
    actual = validate_brackets('')
    expected = 'Empty string'
    assert actual == expected

def test_if_we_send_int_value():
    """
    Test the behavior of the validate_brackets function when an integer value is provided.
    """
    actual = validate_brackets(1)
    expected = 'Argument is not a string'
    assert actual == expected

def test_if_we_send_str_without_brackets():
    """
    Test the behavior of the validate_brackets function when a string without brackets is provided.
    """
    actual = validate_brackets('test')
    expected = 'No brackets found'
    assert actual == expected

def test_if_we_send_balance_brackets():
    """
    Test the behavior of the validate_brackets function when a string with balanced brackets is provided.
    """
    actual = validate_brackets('{()}')
    expected = True
    assert actual == expected

def test_if_we_send_unbalance_brackets():
    """
    Test the behavior of the validate_brackets function when a string with unbalanced brackets is provided.
    """
    actual = validate_brackets('{(}')
    expected = False
    assert actual == expected
