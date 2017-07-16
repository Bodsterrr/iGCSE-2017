## Functions ##

def isName( string ):
    return len(string) > 0 and all(c.isalpha() or c.isspace() for c in string)

def isNumber( string ):
    try:
        number = int(string)
        return True
    except:
        return False

def toBoolean( string ):
    if (string.lower() in ("y", "yes", "true", "1")):
        return True
    else:
        return False

def booleanToString( boolean ):
    if (boolean):
        return "Yes"
    else:
        return "No"

def moneyFormat( money ):
    return str(math.ceil(money * 100.0)/100.0)

## Task 1 ##

import math

coachCost = 550.00
entryCost = 30.00

print("School Trip Cost Calculator\n")

valid = False
while (not valid):
    studentsStr = input("How many students will be attending? ")
    if (isNumber(studentsStr)):
        studentsNum = int(studentsStr)
        if (studentsNum > 45 or studentsNum < 1):
            print("Enter a number between 1 and 45")
        else:
            valid = True
    else:
        print("Please enter a number...\n")
freeTickets = math.floor(studentsNum/10)
print("You will receive " + (str(freeTickets)) + " free ticket(s)")
ticketsCost = entryCost * (studentsNum-freeTickets)
print("The tickets will cost $" + str(moneyFormat(ticketsCost)))
print("The coach will cost $" + str(moneyFormat(coachCost)))
totalCost = ticketsCost + coachCost
sharedCost = totalCost/studentsNum
print("The recommended cost per student is $" + moneyFormat(sharedCost) + "\n")

## Task 2 ##

from tabulate import tabulate
import os

maxStudents = 45
students = {}

print("Now entering student data...\nType 'exit' to stop entering data\n")

i = 1
exiting = False
while (i < 46):
    valid = False
    while (not valid):
        studentName = input("Enter the full name of student #" + str(i) + " ")
        if (studentName.lower() == "exit"):
            exiting = True
            break
        if (isName(studentName)):
            valid = True
        else:
            print("\nPlease enter a valid name...\n")
    if (exiting):
        break
    hasPaidStr = input("Has " + studentName + " paid? (y/N) ")
    hasPaid = toBoolean(hasPaidStr)
    students[studentName] = hasPaid
    i = i + 1
    print("")

print("\n" + tabulate(sorted([(k,booleanToString(v)) for k,v in students.items()]), headers=["Student's Name", "Has Paid?"], tablefmt="orgtbl"))
if (studentsNum > len(students)):
    print("and " + str(studentsNum-len(students)) + " other students who did not attend...")

## Task 3 ##

studentsPaid = 0
for name in students:
    if (students[name]):
        studentsPaid = studentsPaid + 1
        
actualCost = studentsPaid * sharedCost
totalCost = (studentsPaid - math.floor(studentsPaid/10)) * entryCost + coachCost
print("\nThe school trip cost a total of $" + moneyFormat(totalCost))
print("The recommended cost per student was $" + moneyFormat(sharedCost))
print("A total of " + str(studentsPaid) + " students have paid out of an estimate of " + str(studentsNum) + " students")

print("The total amount collected is $" + moneyFormat(actualCost))
if (actualCost > totalCost):
    print("The school trip made a profit of $" + moneyFormat(actualCost-totalCost))
elif (actualCost == totalCost):
    print("The school trip broke even")
else:
    print("The school trip made a loss of $" + moneyFormat(totalCost-actualCost))
