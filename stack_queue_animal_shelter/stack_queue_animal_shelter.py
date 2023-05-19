class AnimalShelter:

    def __init__(self):
        # self.dog_queue = []
        # self.cat_queue = []
        self.animal_shelter=[]

    def enqueue(self, animal):
        '''
        enqueue in Animal Shelter
        Arguments: animal
            animal can be either a dog or a cat object.
            It must have a species property that is either "cat" or "dog"
            It must have a name property that is a string.
        '''
        # The isinstance() function in Python is used to check the type of an object. It takes two arguments: the object we want to check, and the type we want to check against.

        if isinstance(animal, dict) and animal.get('species') == 'cat' and isinstance(animal.get('name'), str):
            self.animal_shelter.append(animal)

        elif isinstance(animal, dict) and animal.get('species') == 'dog' and isinstance(animal.get('name'), str):
            self.animal_shelter.append(animal)
        # if animal.get('species') == 'cat' and isinstance(animal.get('name'), str):
        #     self.cat_queue.append(animal)
        # elif animal.get('species') == 'dog' and isinstance(animal.get('name'), str):
        #     self.dog_queue.append(animal)
        else:
            raise ValueError('Invalid animal object')

    def dequeue(self, pref):
        '''
        Dequeue from Animal Shelter
        Arguments: pref
            pref can be either "dog" or "cat"
        Return: either a dog or a cat, based on preference.
            If pref is not "dog" or "cat", return the animal that has been waiting the longest.
        '''
        if self.animal_shelter:
            if pref == 'cat' or pref == 'dog':
                for i, animal in enumerate(self.animal_shelter):
                    if animal['species'] == pref:
                        return self.animal_shelter.pop(i)
                
                # return f"There is no {pref} in the Shelter"
                return "There is no {} in the Shelter.".format(pref)
            else: 
                return self.animal_shelter.pop(0) 
        return 'The animal shelter empty' 
    
if __name__ == '__main__':
    Animal_Shelter = AnimalShelter()

    cat1 = {'species': 'cat', 'name': 'Fluffy'}
    Animal_Shelter.enqueue(cat1)
    cat2 = {'species': 'cat', 'name': 'Fluffy2'}
    Animal_Shelter.enqueue(cat2)
    dog1 = {'species': 'dog', 'name': 'Boby'}
    Animal_Shelter.enqueue(dog1)
    dog2 = {'species': 'dog', 'name': 'Boby2'}
    Animal_Shelter.enqueue(dog2)

    print(Animal_Shelter.dequeue('cat'))
    print(Animal_Shelter.dequeue('dog'))