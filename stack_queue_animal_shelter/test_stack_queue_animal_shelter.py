import pytest
from stack_queue_animal_shelter.stack_queue_animal_shelter import AnimalShelter

# @pytest.mark.skip
def test_Animal_Shelter_empty():
    """
    Test case to verify the behavior of AnimalShelter.dequeue() when the shelter is empty.
    """
    Animal_Shelter=AnimalShelter()
    actual=Animal_Shelter.dequeue('cat')
    expected = 'The animal shelter empty' 
    assert actual == expected

# @pytest.mark.skip
def test_Animal_Shelter_has_only_cats_and_we_need_dog():
    """
    Test case to verify the behavior of AnimalShelter.dequeue() when the shelter has only cats and we need a dog.
    """
    Animal_Shelter=AnimalShelter()
    cat1 = {'species': 'cat', 'name': 'Fluffy'}
    Animal_Shelter.enqueue(cat1)
    cat2 = {'species': 'cat', 'name': 'Fluffy2'}
    Animal_Shelter.enqueue(cat2)
    actual=Animal_Shelter.dequeue('dog')
    expected = 'There is no dog in the Shelter.' 
    assert actual == expected

# @pytest.mark.skip
def test_Animal_Shelter_has_only_dogs_and_we_need_cat():
    """
    Test case to verify the behavior of AnimalShelter.dequeue() when the shelter has only dogs and we need a cat.
    """
    Animal_Shelter=AnimalShelter()
    dog1 = {'species': 'dog', 'name': 'Boby'}
    Animal_Shelter.enqueue(dog1)
    dog2 = {'species': 'dog', 'name': 'Boby2'}
    Animal_Shelter.enqueue(dog2)

    actual=Animal_Shelter.dequeue('cat')
    expected = 'There is no cat in the Shelter.' 
    assert actual == expected

# @pytest.mark.skip
def test_Animal_Shelter_get_first_cat():
    """
    Test case to verify that AnimalShelter.dequeue() returns the first cat in the shelter.
    """
    Animal_Shelter=AnimalShelter()
    cat1 = {'species': 'cat', 'name': 'Fluffy'}
    Animal_Shelter.enqueue(cat1)
    cat2 = {'species': 'cat', 'name': 'Fluffy2'}
    Animal_Shelter.enqueue(cat2)
    dog1 = {'species': 'dog', 'name': 'Boby'}
    Animal_Shelter.enqueue(dog1)
    dog2 = {'species': 'dog', 'name': 'Boby2'}
    Animal_Shelter.enqueue(dog2)

    actual=Animal_Shelter.dequeue('cat')
    expected = {'name': 'Fluffy', 'species': 'cat'}
    assert actual == expected

def test_Animal_Shelter_get_first_dog():
    """
    Test case to verify that AnimalShelter.dequeue() returns the first dog in the shelter.
    """
    Animal_Shelter=AnimalShelter()
    cat1 = {'species': 'cat', 'name': 'Fluffy'}
    Animal_Shelter.enqueue(cat1)
    cat2 = {'species': 'cat', 'name': 'Fluffy2'}
    Animal_Shelter.enqueue(cat2)
    dog1 = {'species': 'dog', 'name': 'Boby'}
    Animal_Shelter.enqueue(dog1)
    dog2 = {'species': 'dog', 'name': 'Boby2'}
    Animal_Shelter.enqueue(dog2)

    actual=Animal_Shelter.dequeue('dog')
    expected = {'name': 'Boby', 'species': 'dog'}
    assert actual == expected