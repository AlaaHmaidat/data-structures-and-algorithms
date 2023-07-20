# hashmap-left-join
function that LEFT JOINs two hashmaps into a single data structure.

## Whiteboard Process
![WhiteboardWorkflow01](../img/_left%20join%20two%20hashmaps.jpg)

## Approach & Efficiency
### Approach
1. Define the function and its parameters:
   The `left_join` function takes two hashmaps as input parameters. The first hashmap has word strings as keys and synonyms of the keys as values. The second hashmap has word strings as keys and antonyms of the keys as values.

2. Check if either of the input hashmaps is empty or None:
   The function checks if either of the input hashmaps is empty or None. If any of the hashmaps is empty or None, the function returns `None` since there's nothing to perform the left join on.

3. Initialize an empty list to store the results:
   The function creates an empty list called `result`, which will be used to store the final output of the left join operation.

4. Iterate through the keys of `hashmap1`:
   The function iterates through each key in `hashmap1`.

5. Check if the current key exists in `hashmap2`:
   For each key in `hashmap1`, the function checks if the key also exists in `hashmap2`. This step determines if the left join operation can be performed for the current key.

6. Append the result to the result list:
   If the key is found in both `hashmap1` and `hashmap2`, the function retrieves the synonym from `hashmap1` and the antonym from `hashmap2` for that key. It then creates a list with the key, synonym, and antonym (if available) and appends it to the `result` list.

7. Handle the case where the key is not present in `hashmap2`:
   If the key is only present in `hashmap1` and not in `hashmap2`, the function appends the key and its synonym from `hashmap1` to the `result` list. The antonym value is set to `None` since there is no corresponding antonym for this key.

8. Return the final result list:
   After iterating through all the keys in `hashmap1`, the function returns the `result` list, which contains the left join of the two hashmaps, as per the specified rules.


### Big O

The left_join function has a time complexity of O(n) and a space complexity of O(n), both of which are linear.

## Solution

Click [here](./hashmap_left_join.py) to see the code 

Click [here](./test_hashmap_left_join.py) to see the test 