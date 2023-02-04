
# Python program Set1 (30th Jan 2023)

Conditional Structures

1.  Write a program that prompts the user to input a year and determine whether the year is a leap year or not.

  Leap Years are any year that can be evenly divided by 4. A year that is evenly divisible by 100 is a leap year only if it is also evenly divisible by 400. Example :

1.  1992        Leap Year
2.  2000        Leap Year
3.  1900        NOT a Leap Year
4.  1995        NOT a Leap Year

2.  Write a program that prompts the user to input number of calls and calculate the monthly telephone bills as per the following rule:

.  Minimum Rs. 200 for up to 100 calls.
.  Plus Rs. 0.60 per call for next 50 calls.
.  Plus Rs. 0.50 per call for next 50 calls.
.  Plus Rs. 0.40 per call for any call beyond 200 calls.

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

![https://javaconceptoftheday.com/wp-content/uploads/2015/12/FloydTriangle.png](images/image1.jpg)

Write a program to print the Floy'd triangle.

1.  Write a program that prompts the user to input a positive integer. It should then output a message indicating whether the number is a prime number. A prime number is a number that is evenly divisible only by itself and 1. For example, the number 5 is prime because it can be evenly divided only by 1 and 5. The number 6, however, is not prime because it can be divided evenly by I, 2, 3, and 6.

Dictionary:

1.  Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.Sample Dictionary

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

2.  Write a Python program to combine two dictionaries by adding values for common keys. 

d1 = {'a': 100, 'b': 200, 'c':300}

d2 = {'a': 300, 'b': 200, 'd':400}

Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
