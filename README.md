# day2challenge2
Application of list,string,loops and conditional logic

Lists and strings , loops:  Question1

Count vowels in a string, every letter in the english alphabet is either a vowel or consonant, [a, e, i, o, u] is a list of all vowels. The rest are all considered consonants. Write a function that takes a string and returns a tuple containing a new string made of all and only the  vowels from the original  string and the number of duplicates in the original string. Only the first instance of the vowel is considered.

For example:
countVowels(‘dahdah’)  # will return (‘a’, 3)
countVowels(‘drink water’) # will return (‘iae’, 1)

Python programming challenge : Fizzbuzz  , (lists and conditional logical): Question2

Write a function named Fizzbuzz that takes two(2) lists  and returns Fizz if the combined length of the lists is divisible by 3,  Buzz if it is divisible by 5, Fizzbuzz if it is divisible by both 5 and 3  or the combined length of the list.

For example:
fizzbuzz([1, 2, 3], [ ])    # will return “fizz”
fizzbuzz([1, 2, 3], [1, 2])  # will return “buzz”  
fizzbuzz([1, 2, 3], [1]) # will return 4 

In the fizzbuzz folder there is fizzbuzz.py and fizzbuzz_test.py, implement the fizzbuzz function in fizzbuzz.py, the implementation should pass all the tests in fizzbuzz_test.py. The goal is to write clean readable code that implements fizzbuzz and passes all the tests. Feel free to add more tests.

