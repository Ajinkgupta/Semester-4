
Python program Set1 (30th Jan 2023)

Conditional Structures

1.  Write a program that prompts the user to input a year and determine whether the year is a leap year or not.

1.  Leap Years are any year that can be evenly divided by 4. A year that is evenly divisible by 100 is a leap year only if it is also evenly divisible by 400. Example :

1.  1992        Leap Year
2.  2000        Leap Year
3.  1900        NOT a Leap Year
4.  1995        NOT a Leap Year

2.  Write a program that prompts the user to input number of calls and calculate the monthly telephone bills as per the following rule:

5.  Minimum Rs. 200 for up to 100 calls.
6.  Plus Rs. 0.60 per call for next 50 calls.
7.  Plus Rs. 0.50 per call for next 50 calls.
8.  Plus Rs. 0.40 per call for any call beyond 200 calls.

3.  3.The marks obtained by a student in 3 different subjects are input by the user. Your program should calculate the average of subjects and display the grade. The student gets a grade as per the following rules:

1.  Average        Grade
2.  90-100        A
3.  80-89        B
4.  70-79        C
5.  60-69        D

1.  0-59        F

Looping Structures
------------------

1.Floyd's triangle is a right-angled triangular array of natural numbers as shown below:

![data:image/jpeg;base64,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](images/image1.jpg)

Write a program to print the Floy'd triangle.

1.  Write a program that prompts the user to input a positive integer. It should then output a message indicating whether the number is a prime number. A prime number is a number that is evenly divisible only by itself and 1. For example, the number 5 is prime because it can be evenly divided only by 1 and 5. The number 6, however, is not prime because it can be divided evenly by I, 2, 3, and 6.

Dictionary:

1.  Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.Sample Dictionary

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

2.  Write a Python program to combine two dictionaries by adding values for common keys. 

d1 = {'a': 100, 'b': 200, 'c':300}

d2 = {'a': 300, 'b': 200, 'd':400}

Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
