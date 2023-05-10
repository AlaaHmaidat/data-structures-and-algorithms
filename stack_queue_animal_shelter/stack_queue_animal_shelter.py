class AnimalShelter:

    def __init__(self):
        self.dog_queue = []
        self.cat_queue = []

    def enqueue(self, animal: dict):
        '''
        enqueue in Animal Shelter
        Arguments: animal
            animal can be either a dog or a cat object.
            It must have a species property that is either "cat" or "dog"
            It must have a name property that is a string.
        '''
        # The isinstance() function in Python is used to check the type of an object. It takes two arguments: the object we want to check, and the type we want to check against.

        # if isinstance(animal, dict) and animal.get('species') == 'cat' and isinstance(animal.get('name'), str):
        #     self.cat_queue.append(animal)
        if animal.get('species') == 'cat' and isinstance(animal.get('name'), str):
            self.cat_queue.append(animal)
        elif animal.get('species') == 'dog' and isinstance(animal.get('name'), str):
            self.dog_queue.append(animal)
        else:
            raise ValueError('Invalid animal object')

    def dequeue(self, pref):
        '''
        dequeue from Animal Shelter
        Arguments: pref
            pref can be either "dog" or "cat"
        Return: either a dog or a cat, based on preference.
            If pref is not "dog" or "cat" then return null.
        '''
        if pref == 'cat':
            if self.cat_queue:
                return self.cat_queue.pop(0)
            else:
                return None
        elif pref == 'dog':
            if self.dog_queue:
                return self.dog_queue.pop(0)
            else:
                return None
        else:
            return None

if __name__ == '__main__':
    q = AnimalShelter()

    cat = {'species': 'cat', 'name': 'Fluffy'}
    q.enqueue(cat)

    dog = {'species': 'dog', 'name': 'Boby'}
    q.enqueue(dog)

    dog = {'species': 'dog', 'name': 'Boby2'}
    q.enqueue(dog)

    print(q.dequeue('dog'))
