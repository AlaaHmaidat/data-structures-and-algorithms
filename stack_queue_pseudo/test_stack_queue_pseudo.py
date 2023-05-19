import pytest
from stack_queue_pseudo.stack_queue_pseudo import PseudoQueue

# @pytest.mark.skip
def test_successfully_pushed_into_stack1():
    '''
    Test to verify if a value is successfully pushed into stack1.
    '''
    pseudo=PseudoQueue() # Create an instance of the PseudoQueue class
    pseudo.enqueue(1)
    
    actual = pseudo.enqueue(1)
    expected = 'successfully pushed into stack1'
    assert actual == expected

def test_if_stack1_have_one_value():
    '''
    Test to verify if the stack implemented with a pseudo queue correctly enqueues and dequeues one value.
    '''
    pseudo=PseudoQueue() # Create an instance of the PseudoQueue class
    pseudo.enqueue(1)
    
    actual = pseudo.dequeue()
    expected = 1
    assert actual == expected

def test_if_stack1_have_multi_value():
    '''
    Test to verify if the stack implemented with a pseudo queue correctly enqueues and dequeues multi value.
    '''
    pseudo=PseudoQueue() # Create an instance of the PseudoQueue class
    pseudo.enqueue(1)
    pseudo.enqueue(2)
    pseudo.enqueue(3)
    pseudo.dequeue()
    pseudo.dequeue()
    actual = pseudo.dequeue()
    expected = 3
    assert actual == expected

def test_if_stack_is_empty():
    """
    Test to verify if the stack implemented with a pseudo queue correctly handles dequeuing when the stack is empty.
    """
    pseudo = PseudoQueue()  # Create an instance of the PseudoQueue class
    
    actual = pseudo.dequeue()  # Attempt to dequeue a value from the pseudo queue
    expected = 'Queue is empty'  # The expected value when the stack is empty
    assert actual == expected

def test_enqueue_and_dequeue_sequence():
    """
    Test to verify if the stack implemented with a pseudo queue correctly enqueues and dequeues values in a sequence.
    """
    pseudo = PseudoQueue()  # Create an instance of the PseudoQueue class
    pseudo.enqueue(1)
    pseudo.enqueue(2)
    pseudo.enqueue(3)
    pseudo.dequeue()
    pseudo.enqueue(4)
    actual = pseudo.dequeue()
    expected = 2
    assert actual == expected