import pytest
from stack_and_queue.stack import stack
from stack_and_queue.queue import queue

# @pytest.mark.skip()


def test_can_successfully_push_onto_a_stack(stack_list):
    actual = stack_list.push(1)
    expected = "successfully push 1 item onto a stack"
    assert actual == expected


def test_can_successfully_push_multiple_values_onto_a_stack(stack_list):
    items = stack_list.push(1)
    items = stack_list.push(2)
    items = stack_list.push(3)
    actual = items
    expected = "successfully push 3 item onto a stack"
    assert actual == expected


def test_can_successfully_pop_off_the_stack(stack_list):
    stack_list.push(1)
    items_pop = stack_list.pop()

    actual = items_pop
    expected = "successfully pop 1 from the stack"
    assert actual == expected


def test_can_successfully_empty_a_stack_after_multiple_pops(stack_list):
    stack_list.push(1)
    stack_list.pop()
    items_pop = stack_list.pop()

    actual = items_pop
    expected = "Sorry, This stack is empty"
    assert actual == expected

# @pytest.mark.skip()


def test_can_successfully_peek_the_next_item_on_the_stack(stack_list):
    stack_list.push(1)
    item = stack_list.peek()

    actual = item
    expected = 1
    assert actual == expected

# @pytest.mark.skip()


def test_can_successfully_instantiate_an_empty_stack(stack_list):

    actual = stack_list.is_empty()
    expected = "This stack is empty"
    assert actual == expected

# @pytest.mark.skip()


def test_calling_pop_or_peek_on_empty_stack_raises_exception(stack_list):

    actual = stack_list.pop() and stack_list.peek()
    expected = "Sorry, This stack is empty"
    assert actual == expected

# @pytest.mark.skip()


def test_can_successfully_enqueue_into_a_queue(queue_list):
    actual = queue_list.enqueue(1)
    expected = "successfully push onto a queue"
    assert actual == expected

# @pytest.mark.skip()


def test_can_successfully_enqueue_multiple_values_into_a_queue(queue_list):
    queue_list.enqueue(1)
    actual = queue_list.enqueue(2)
    expected = "successfully push onto a queue"
    assert actual == expected

# @pytest.mark.skip()


def test_can_successfully_dequeue_out_of_a_queue_the_expected_value(queue_list):
    queue_list.enqueue(1)
    items_pop = queue_list.dequeue()

    actual = items_pop
    expected = f"successfully dequeue 1 from the queue"
    assert actual == expected


# @pytest.mark.skip()
def test_can_successfully_peek_into_a_queue_seeing_the_expected_value(queue_list):
    queue_list.enqueue(1)
    item = queue_list.peek()

    actual = item
    expected = 1
    assert actual == expected


# @pytest.mark.skip()
def test_can_successfully_empty_a_queue_after_multiple_dequeues(queue_list):
    queue_list.enqueue(1)
    queue_list.dequeue()
    items_dequeue = queue_list.dequeue()

    actual = items_dequeue
    expected = "Sorry, This queue is empty"
    assert actual == expected

# @pytest.mark.skip()
def test_can_successfully_instantiate_an_empty_queue(queue_list):

    actual = queue_list.is_empty()
    expected = "This queue is empty"
    assert actual == expected

# @pytest.mark.skip()
def test_calling_dequeue_or_peek_on_empty_queue_raises_exception(queue_list):
    actual = queue_list.dequeue() or queue_list.peek()
    expected = "Sorry, This queue is empty"
    assert actual == expected

@pytest.fixture
def stack_list():
    stack_list = stack()
    return stack_list


@pytest.fixture
def queue_list():
    queue_list = queue()
    return queue_list
