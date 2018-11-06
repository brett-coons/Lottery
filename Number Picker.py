## MEGAMILLIONS LOTTERY: Players may pick six numbers from two separate pools of 
## numbers - five different numbers from 1 to 70 and one number from 1 to 25.


import random
import re

def main():
    print (generate(draw_5(), draw_1()))
    
def draw_5():
    pick_five = [x for x in range(1,71)]
    ## pick five numbers
    numbers = random.choices(pick_five, k = 5)
    ## make sure no duplicate numbers are generated
    while (checkDuplicates(numbers) == True):
            numbers = random.choices(pick_five, k = 5)
    ## sort numbers
    quickSort(numbers)
    return (numbers)
       
def draw_1():
    pick_one = [x for x in range(1,26)]    
    ## pick one number
    money_ball = random.choices(pick_one, k = 1)
    return (money_ball)

def generate(numbers, money_ball):
    ticket = numbers + money_ball
    while (checkHistorical(ticket) == True):
        numbers = draw_5()
        ticket = numbers + money_ball
    return (ticket)
   
## this step is needed to ensure no draw contains duplicates in the first five numbers because random.choices
## does not always guarantee unique results
def checkDuplicates(array):
    if len(array) != len(set(array)):
        return (True) ## match found
    return (False)

## checks array against historic numbers
def checkHistorical(array):
    D = {}
    with open("historic_draws.txt", "r") as F:
        for line in F:
            split = re.split(r'\s',line)
            date = split[0]
            ## convert list of strings to list of integers
            ticket = [int(x) for x in split[1:7]]
            ## build dictionary formatted as {date: [ticket]}
            D[date] = ticket
    if (array in D.values()):
        return (True)       ## match found
    else:
        return (False)      

###################################################################################################################
## The following code was liberated from
## https://interactivepython.org/courselib/static/pythonds/SortSearch/TheQuickSort.html
    
def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp

   return rightmark


