import pytest
from stack_and_queue.stack import stack

@pytest.mark.skip()
def Can_successfully_push_onto_a_stack(stack_list):
    
    actual = stack_list.push(1)
    expected = "successfully push onto a stack"
    assert actual == expected

@pytest.fixture
def stack_list():
    stack_list = stack()
    return stack_list