# created by matthew walsh
# created for ics3u
# created on dec 2017
# finds the average of a set of numbers

from numpy import random

def average_elements(array = []):
    average = 0
    total = 0
    counter = 0
    while counter < len(array):
    	total = total + array[counter]
    	counter = counter + 1
    average = total / counter
    return average

number_of_rows = raw_input("Enter the number of rows you would like: ")
number_of_rows = int(number_of_rows)
table = []
for rows in range(0, number_of_rows):
    table.append(random.randint(1, 50))
    
print(table)
table_values_average = average_elements(table)
print("The average of the numbers is: " + str(table_values_average))
