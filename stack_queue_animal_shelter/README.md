#  Animal Shelter
First-in, First out Animal Shelter.

## Approach & Efficiency

1. __init__(self): Initializes an empty queue(cat_queue,dog_queue).

2. enqueue(self, animal: dict):enqueue in Animal Shelter

    * Git the value species in animal and check (If) the value of species equal cat and git the name of the animal 
    * add the animal onto cat_queue 
    * Git the value species in animal and check (If) the value of species equal dog and git the name of the animal 
    * add the animal onto dog_queue 
    * else raise ValueError('Invalid animal object')

3. dequeue(self, pref):dequeue from Animal Shelter
    * check the prefar if it eqal cat 
    * check the cat_queue if it not empty return the first cat was added else return none
    * else check the prefar if it eqal dog 
    * check the dog_queue if it not empty return the first dog was added else return none
    * if perf not eqaul cat or dog return none


    
### Big O
The time complexity: O(1) because we never loop in any part
The space complexity: O(n) where n is the total number of animals enqueued, because we create an empty queues and we enqueue in those queues


## Solution
Click [here](./stack_queue_animal_shelter.py)
