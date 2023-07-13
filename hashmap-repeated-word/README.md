# Challenge Title
### **Hashmap repeated word**
Function called repeated word that finds the first word to occur more than once in a string


## Whiteboard Process
![Whiteboard](../img/repeated%20word.jpg)

## Approach & Efficiency

1. Split the input string into words and remove punctuation.
2. Create an empty dictionary, `dic1`, to store word frequencies.
3. Iterate through each word in the list of words:
   - If the word is already in `dic1`, increment its frequency.
   - Otherwise, add the word to `dic1` with a frequency of 1.
4. Initialize an empty list, `most_common_word`, to store the most common words.
5. Iterate through the items in `dic1` and check if a word has a higher frequency than the previous most frequent word.
6. If a word has a higher frequency, update the `most_common_word` list with that word.
7. Initialize an empty string, `first_repeated_word`, to store the first repeated word encountered.
8. Create another empty dictionary, `dic2`, to track unique words until the first repeated word is found.
9. Iterate through the list of words:
   - If a word is already in `dic2`, it is the first repeated word.
   - If not, add the word to `dic2`.
10. Return the list of all words and their frequencies (`dic1.items()`), the first repeated word, and the most common words.


Time Complexity:

- Building the `dic1` dictionary by iterating through the words: O(n), where n is the number of words in the input string.
- Finding the first repeated word: O(n), where n is the number of words in the input string.
- Finding the most common words: O(n), where n is the number of words in the input string.
- Overall, the time complexity is O(n).
...
Space Complexity:

- `dic1` dictionary: O(m), where m is the number of unique words in the input string.
- `dic2` dictionary: O(k), where k is the number of unique words encountered until finding the first repeated word.
- `all_words` list: O(m), where m is the number of unique words in the input string.
- `first_repeated_word` string: O(1).
- `most_common_word` list: O(p), where p is the number of most common words.
- Overall, the space complexity is O(m + k + p).

## Solution

Click [here](./hashmap_repeated_word.py) to see the code 

Click [here](./test_hashmap_repeated_word.py) to see the test 

