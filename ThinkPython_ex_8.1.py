## from ThinkPython - Exercise 8.1 Write a function that takes a string
## as an argument and displays the letters backward, one per line.
##
## This is my solution.
## The first while loop iterates through the
## string fruit, and prints each letter on a line.
## The second while loops over the string backwards and prints each
## letter in reverse order.
## By: Roger Stillick Jr.
## 26 Dec 2015
## **no license**

index = 0
fruit = "pineapple"

while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index += 1

print()
index = 0

while (index * -1) < len(fruit):
    letter = fruit[index - 1]
    print(letter)
    index -= 1



