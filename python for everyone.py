# Exercise 2: Write a program that uses input to prompt a user for their name and then welcomes them.

# Enter your name: Chuck
# Hello Chuck

# name = input("Enter your name: ")
# print("Hello " + name + "\n")


# Exercise 3: Write a program to prompt the user for hours and rate per hour to compute gross pay.

# Enter Hours: 35
# Enter Rate: 2.75
# Pay: 96.25

# hours = input("Enter Hours: ")

# rate = input("Enter Rate: ")

# pay = float(hours) * float(rate)
# print("Pay: " + str(pay))


# Exercise 4: Assume that we execute the following assignment statements:

# width = 17
# height = 12.0
# For each of the following expressions, write the value of the expression and the type (of the value of the expression).

# 1. width//2 (8) int

# 2. width/2.0 (8.5) float

# 3. height/3 (4.0) float

# 4. 1 + 2 * 5 (11) int

# width = 17
# height = 12.0

# one = width // 2
# two = width / 2.0
# three = height / 3
# four = 1 + 2 * 5
# print(type(one))
# print(type(two))
# print(type(three))
# print(type(four))

# Exercise 5: Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.

# celsius = input("Enter a temerature in Celsius: ")

# CelsiusToFahrenheit = (float(celsius) * (9/5)) + 32
# print("Temerature in Fahrenheit is: " + str(CelsiusToFahrenheit))


# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

# hours = input("Enter Hours: ")

# rate = input("Enter Rate: ")

# if float(hours) > 40:
#     extra_hours_rate = (float(hours) - 40) * 1.5 * float(rate)
#     pay = 40 * float(rate) + extra_hours_rate
#     print("Pay: " + str(pay))

# else:
#     pay = float(hours) * float(rate)
#     print("Pay: " + str(pay))


# Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program.
# The following shows two executions of the program:

# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input

# Enter Hours: forty
# Error, please enter numeric input

# try:
#     hours = float(input("Enter Hours: "))
#     rate = float(input("Enter Rate: "))
#     if hours > 40:
#         extra_hours_rate = (hours - 40) * 1.5 * rate
#         pay = 40 * rate + extra_hours_rate
#         print("Pay: " + str(pay))

#     else:
#         pay = hours * rate
#         print("Pay: " + str(pay))
# except:
#     print("Error, please enter numeric input!")


'''
Exercise 3: Write a program to prompt for a score between 0.0 and 1.0.
If the score is out of range, print an error message.
If the score is between 0.0 and 1.0, print a grade using the following table:

    Score       Grade
     >= 0.9       A
     >= 0.8       B
     >= 0.7       C
     >= 0.6       D
      < 0.6       F

Enter score: 0.95
A

Enter score: perfect
Bad score

Enter score: 10.0
Bad score

Enter score: 0.75
C

Enter score: 0.5
F
'''

# try:
#     score = input("Enter a score between 0.0 and 1.0: ")
#     score = float(score)
#     if not (score >= 0.0 and score <= 1.0):
#         print("Bad score")
#     else:
#         if score >= 0.9:
#             print("A")
#         elif score >= 0.8:
#             print("B")
#         elif score >= 0.7:
#             print("C")
#         elif score >= 0.6:
#             print("D")
#         elif score < 0.6:
#             print("F")
# except:
#     print("Bad score")


# Exercise 1: Run the program on your system and see what numbers you get. Run the program more than once and see what numbers you get.
''' 
import random

for i in range(10):
    x = random.random()
    print(x)
'''
# 0.3096038797345676
# 0.9265366211034308
# 0.4577348805035417
# 0.620418084049225
# 0.6886868019386183
# 0.11781020258142716
# 0.13829063909090855
# 0.5888685843295853
# 0.2499555658916115
# 0.8007398461917219
'''
import random

for i in range(10):
    x = random.random()
    print(x)
'''
# 0.9155322243512732
# 0.749013053009494
# 0.639625103780832
# 0.9368352900142266
# 0.10245888964862448
# 0.2577505557980976
# 0.05988898951740884
# 0.9055724382828312
# 0.9211993238574279
# 0.2874347166176323


# Exercise 2: Move the last line of this program to the top, so the function call appears before the definitions.
# Run the program and see what error message you get.
'''
repeat_lyrics()

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')


def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()
'''
# Exercise 3: Move the function call back to the bottom and move the definition of print_lyrics after the definition of repeat_lyrics.
# What happens when you run this program?

'''
def repeat_lyrics():
    print_lyrics()
    print_lyrics()

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

repeat_lyrics()
'''

# Exercise 4: What is the purpose of the "def" keyword in Python? d) b and c are both true

# a) It is slang that means "the following code is really cool"
# b) It indicates the start of a function
# c) It indicates that the following indented section of code is to be stored for later
# d) b and c are both true
# e) None of the above


# Exercise 5: What will the following Python program print out? d)

# def fred():
#    print("Zap")

# def jane():
#    print("ABC")

# jane()
# fred()
# jane()

# a) Zap ABC jane fred jane
# b) Zap ABC Zap
# c) ABC Zap jane
# d) ABC Zap ABC
# e) Zap Zap Zap


# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).

# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0
'''
def computepay(hours, rate):
    try:
        hours = float(hours)
        rate = float(rate)
        if hours > 40:
            extra_hours_rate = (hours - 40) * 1.5 * rate
            pay = 40 * rate + extra_hours_rate
            print("Pay: " + str(pay))        
        else:
            pay = hours * rate
            print("Pay: " + str(pay))
    except:
        print("Error, please enter numeric input!")

hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
computepay(hours, rate)
'''
'''
Exercise 7: Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.

    Score       Grade
     >= 0.9       A
     >= 0.8       B
     >= 0.7       C
     >= 0.6       D
      < 0.6       F

Program Execution:
Enter score: 0.95
A
Enter score: perfect
Bad score
Enter score: 10.0
Bad score
Enter score: 0.75
C
Enter score: 0.5
F
Run the program repeatedly to test the various different values for input.
'''
'''
def computegrade(score):
    try:
        score = float(score) 
        if not (score >= 0.0 and score <= 1.0):
            print("Bad score")
        else:
            if score >= 0.9:
                print("A")
            elif score >= 0.8:
                print("B")
            elif score >= 0.7:
                print("C")
            elif score >= 0.6:
                print("D")
            elif score < 0.6:
                print("F")
    except:
        print("Bad score")

score = input("Enter a score between 0.0 and 1.0: ")
computegrade(score)
'''

# continue puts you at the start, break puts you after the end
'''
while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')


while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')
'''


'''
Exercise 1: Write a program which repeatedly reads numbers until the user enters "done".
Once "done" is entered, print out the total, count, and average of the numbers. 
If the user enters anything other than a number,
detect their mistake using try and except and print an error message and skip to the next number.

Enter a number: 4
Enter a number: 5
Enter a number: bad data
Invalid input
Enter a number: 7
Enter a number: done
16 3 5.333333333333333
'''
'''
total = 0
count = 0

while True:
    try:
        input_text = input("Enter a number: ")
        if input_text == 'done':
            break
        count += 1
        total += int(input_text)
    except:
        print("Not a number!")
        continue
average = total / count
print('Total: ', total)
print('Count: ', count)
print('Average: ', average)
'''


'''    
Exercise 2: Write another program that prompts for a list of numbers as above and at the end prints out 
both the maximum and minimum of the numbers instead of the average.
'''
'''
total = 0
count = 0
minimum = None
maximum = None

while True:
    try:
        input_text = input("Enter a number: ")
        if input_text == 'done':
            break
        input_num = int(input_text)
        count += 1
        total += int(input_text)
        if minimum is None or input_num < minimum:
            minimum = input_num
        if maximum is None or input_num > maximum:
            maximum = input_num
    except:
        print("Not a number!")
        continue

print('Total: ', total)
print('Count: ', count)
print('Minimum: ', minimum, input_num)
print('Maximum: ', maximum, input_num)
'''

''' 
This code prompts the user to enter numbers until they type "done". It keeps track of the number of entries made by the user, calculates the sum of the entries, and finds the minimum number entered by the user. If the user enters an invalid input, the program prints an error message and continues to prompt for input.

After the user has entered "done", the program prints the total number of entries, the sum of the entries, and the minimum number entered.

The variable total keeps track of the sum of all the numbers entered by the user, and count keeps track of the number of entries made. The variable minimum is used to store the smallest number entered by the user.

The code has some errors that would prevent it from working correctly. The line contain = int(input_text) is placed inside the try-except block, which means that if an invalid input is entered, contain will not be defined, and the program will raise a NameError when trying to print its value at the end.

Also, the if statement that compares contain with contain instead of minimum is incorrect, and the subsequent print statement is placed outside the loop and would not execute as intended.

Here's a corrected version of the code:

python
Copy code
total = 0
count = 0
minimum = None

while True:
    try:
        input_text = input("Enter a number: ")
        if input_text == 'done':
            break
        input_num = int(input_text)
        count += 1
        total += input_num
        if minimum is None or input_num < minimum:
            minimum = input_num
        print("Before", minimum, input_num)
    except ValueError:
        print("Not a number!")
        continue

print('Total: ', total)
print('Count: ', count)
print('Minimum: ', minimum)

This version of the code should work as intended.
'''


'''
Exercise 1: Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string,
printing each letter on a separate line, except backwards.

'''
'''
fruit = 'banana'
index = -1

while index >= -1 * len(fruit):
    letter = fruit[index]
    print(letter)
    index = index - 1
'''

'''
Exercise 2: Given that fruit is a string, what does fruit[:] mean?

'''
'''
fruit = 'banana'
print(fruit[:])
# it shows the whole string, meaning starts at the beginning and ends at the end of the string
'''


'''
Exercise 3: Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments.
'''
'''
def count(string, letter_count):
    count = 0
    for letter in string:
        if letter == letter_count:
            count = count + 1
    print(count)

count('banana', 'a')
'''


'''
Exercise 4: There is a string method called count that is similar to the function in the previous exercise.
Read the documentation of this method at https://docs.python.org/3.5/library/stdtypes.html#string-methods and
write an invocation that counts the number of times the letter a occurs in "banana".
'''

'''
string = 'banana'
print(string.count('a'))
'''


'''
Exercise 5: Take the following Python code that stores a string: 

str = 'X-DSPAM-Confidence:0.8475'

Use find and string slicing to extract the portion of the string after the colon character
and then use the float function to convert the extracted string into a floating point number.
'''
'''
dank = "dank"
type(dank)
print(help(str.find))
'''
'''
# X-DSPAM-Confidence:0.8475 --> 0.8475 
# 

str = 'X-DSPAM-Confidence:0.8475'

poscolon = str.find(':')
print(poscolon)

length = len(str)
print(len(str))

new_string = str[poscolon + 1:length]
print(new_string)

'%g' % float(new_string)
'''

'''
Exercise 6:
Read the documentation of the string methods at: https://docs.python.org/3.5/library/stdtypes.html#string-methods

You might want to experiment with some of them to make sure you understand how they work. strip and replace are particularly useful.

The documentation uses a syntax that might be confusing. For example, in find(sub[, start[, end]]), the brackets indicate optional arguments.
So sub is required, but start is optional, and if you include start, then end is optional.
'''
'''
dank = 'Hella Dank'
#print(len(dank))
#print(dank.capitalize())
#print(dank.casefold()) 
#print(dank.center(40, '🔺'))
#print(dank.count('a'))
#print(dank.expandtabs(16))
#print('www.example.com'.strip('w.com'))
print(dank.replace('Hella Dank','hella dank'))
'''

'''
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)

# Open the file 
f = open('mbox.txt', 'r') # Initialize a counter 
line_count = 0 # Iterate over each line in the file 
while True:
    line = f.readline()
    if not line:
        break 
    line_count += 1
    # Print the number of lines
print(line_count)
'''
'''
fhand = open('mbox-short.txt')
inp = fhand.read()
print(len(inp))
print(inp[:20])
'''
'''
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    if line.startswith('From:'):
        print(line)
'''
'''        
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)
'''
'''
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    # Skip 'uninteresting lines'
    if not line.startswith('From:'):
        continue
    # Process our 'interesting' line
    print(line)
'''
'''
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.find('@uct.ac.za') == -1: continue
    print(line)
'''
'''
fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)
'''
'''
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)
'''
'''
fout = open('output.txt', 'w')
print(fout)
line1 = "This here's the wattle,\n"
fout.write(line1)
'''

'''
Exercise 1: Write a program to read through a file and print the contents of the file (line by line) all in upper case. Executing the program will look as follows:

python shout.py
Enter a file name: mbox-short.txt
FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN  5 09:14:16 2008
RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
     BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
     SAT, 05 JAN 2008 09:14:16 -0500
'''
'''
fName = input('Enter the file name: ')
try:
    fHandle = open(fName)
except:
    print('File cannot be opened:', fName)
    exit()
for line in fHandle:
    print(line.upper())
'''


'''
# Exercise 2: Write a program to prompt for a file name, and then read through the file and look for lines of the form:

# X-DSPAM-Confidence:0.8475

When you encounter a line that starts with "X-DSPAM-Confidence:" pull apart the line to extract the floating-point number on the line.
Count these lines and then compute the total of the spam confidence values from these lines.
When you reach the end of the file, print out the average spam confidence.

# Enter the file name: mbox.txt
# Average spam confidence: 0.894128046745

# Enter the file name: mbox-short.txt
# Average spam confidence: 0.750718518519

Test your file on the mbox.txt and mbox-short.txt files.
'''
'''
# 1. prompt for a file name
fName = input('Enter the file name: ')
try:
    fHandle = open(fName)
except:
    print('File', fName, 'not found!')
    exit()

# 2. read through file find lines that start with: "X-DSPAM-Confidence:"
count = 0
total = 0.0
for line in fHandle:
    if line.startswith('X-DSPAM-Confidence: '):

# 3. extract the floating point which comes after the ":"
        #gString = line
        #poscolon = gString.find(':')
        #strlen = len(gString)
        #new_gString = gString[poscolon + 1: strlen]
        #gExtracted = '%g' % float(new_gString)
        #total += float(gExtracted) 
        total += float(line[line.find(':') + 2:])
# 4. count the number of lines
        count += 1
        
# 5. calculate the average spam confidence
average = total / count
print("Average spam confidence: ", average)
'''

'''
Exercise 3: Sometimes when programmers get bored or want to have a bit of fun,
they add a harmless Easter Egg to their program.
Modify the program that prompts the user for the file name so that it prints a funny message when the user types in the exact file name "na na boo boo".
The program should behave normally for all other files which exist and don't exist. Here is a sample execution of the program:

python egg.py
Enter the file name: mbox.txt
There were 1797 subject lines in mbox.txt

python egg.py
Enter the file name: missing.tyxt
File cannot be opened: missing.tyxt

python egg.py
Enter the file name: na na boo boo
NA NA BOO BOO TO YOU - You have been punk'd!

We are not encouraging you to put Easter Eggs in your programs; this is just an exercise.


fName = input('Enter the file name: ')
try:
    fHandle = open(fName)

except:
    if fName == "na na boo boo":
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
        exit()
    print('File', fName, 'not found!')
    exit()

count = 0
total = 0.0
for line in fHandle:
    if line.startswith('X-DSPAM-Confidence: '):
        #gString = line
        #poscolon = gString.find(':')
        #strlen = len(gString)
        #new_gString = gString[poscolon + 1: strlen]
        #gExtracted = '%g' % float(new_gString)
        #total += float(gExtracted) 
        total += float(line[line.find(':') + 2:])
        count += 1
average = total / count
print("Average spam confidence: ", average)
'''


'''
Exercise 1: Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None.
Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.
'''
""" 
def chop(t):
    del t[0]
    del t[len(t) - 1]

def middle(t):
    return t[1:len(t) - 1]

a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]

chop(a)
print(a)
print(middle(b))
 """ 

""" 
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    print('Debug lines: ', line)
    print('Debug words: ', words)
    print(words[2])
 """
"""
Exercise 2: Figure out which line of the above program is still not
properly guarded. See if you can construct a text file which causes the
program to fail and then modify the program so that the line is properly
guarded and test it to make sure it handles your new text file.
"""

""" 
fhand = open('mbox-short-1.txt')
count = 0
dayOfTheWeek = ['Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thur', 'Fri']

for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) == 0: continue
    if words[0] != 'From' : continue
    if len(words) < 3:
        for word in words:
            if word == dayOfTheWeek:
                print(word)
    else:
        print(words[2]) 
 """        

"""
Exercise 3: Rewrite the guardian code in the above example without
two if statements. Instead, use a compound logical expression using
the or logical operator with a single if statement. 
"""
""" 
fhand = open('mbox-short-1.txt')
count = 0
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) == 0 or words[0] != 'From' or len(words) < 3: continue
    print(words[2])
    count += 1 
print(count) 
 """

 
""" 
Exercise 4: Find all unique words in a file
# Shakespeare used over 20,000 words in his works. But how would you
# determine that? How would you produce the list of all the words that
# Shakespeare used? Would you download all his work, read it and track
# all unique words by hand?
Let’s use Python to achieve that instead. List all unique words, sorted
in alphabetical order, that are stored in a file romeo.txt containing a
subset of Shakespeare’s work.
To get started, download a copy of the file www.py4e.com/code3/romeo.txt.
Create a list of unique words, which will contain the final result. Write
a program to open the file romeo.txt and read it line by line. For each
line, split the line into a list of words using the split function. For
each word, check to see if the word is already in the list of unique
words. If the word is not in the list of unique words, add it to the list.
When the program completes, sort and print the list of unique words
in alphabetical order.
Enter file: romeo.txt
['Arise', 'But', 'It', 'Juliet', 'Who', 'already',
'and', 'breaks', 'east', 'envious', 'fair', 'grief',
'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft',
'sun', 'the', 'through', 'what', 'window',
'with', 'yonder']
 """
"""  
fName = input('Enter the file name: ')
try:
    fHand = open(fName)
except:
    print('File', fName, 'not found!')
    exit()

uniqueWords = list()

for line in fHand:
    words = line.split()
    for word in words:
        if word not in uniqueWords:
            uniqueWords.append(word)
        else: continue
    uniqueWords.sort()
print('unique words: ', uniqueWords)
 """

""" 
Exercise 5: Minimalist Email Client.
MBOX (mail box) is a popular file format to store and share a collection
of emails. This was used by early email servers and desktop apps.
Without getting into too many details, MBOX is a text file, which
stores emails consecutively. Emails are separated by a special line which
starts with From (notice the space). Importantly, lines starting with
From: (notice the colon) describes the email itself and does not act as
a separator. Imagine you wrote a minimalist email app, that lists the
email of the senders in the user’s Inbox and counts the number of emails.
# Write a program to read through the mail box data and when you find
# line that starts with “From”, you will split the line into words using the
# split function. We are interested in who sent the message, which is the
# second word on the From line.
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# You will parse the From line and print out the second word for each
# From line, then you will also count the number of From (not From:)
# lines and print out a count at the end. This is a good sample output
# with a few lines removed:
# python fromcount.py
# Enter a file name: mbox-short.txt
# stephen.marquard@uct.ac.za
# louis@media.berkeley.edu
zqian@umich.edu
[...some output removed...]
ray@media.berkeley.edu
cwen@iupui.edu
cwen@iupui.edu
cwen@iupui.edu
There were 27 lines in the file with From as the first word 
"""
"""  
fName = input('Enter the file name: ')
try:
    fHand = open(fName)
except:
    print('File', fName, 'not found!')
    exit()
    
lineCount = 0 
for line in fHand:
    if not line.startswith('From '): continue
    words = line.split()
    print(words[1])
    lineCount += 1
print('There were', lineCount ,'lines in the file with From as the first word')
 """

""" 
Exercise 6: Rewrite the program that prompts the user for a list of
numbers and prints out the maximum and minimum of the numbers at
the end when the user enters “done”. Write the program to store the
numbers the user enters in a list and use the max() and min() functions to
compute the maximum and minimum numbers after the loop completes.
Enter a number: 6
Enter a number: 2
Enter a number: 9
Enter a number: 3
Enter a number: 5
Enter a number: done
Maximum: 9.0
Minimum: 2.0
"""
"""   
numlist = list()

while True:
    try:
        input_text = input("Enter a number: ")
        if input_text == 'done': break
        num = float(input_text)
        numlist.append(num)
    except:
        print("Not a number!")
        continue
print(max(numlist))
print(min(numlist))
"""

""" 
Exercise 1: Download a copy of the file www.py4e.com/code3/words.txt
Write a program that reads the words in words.txt and stores them as
keys in a dictionary. It doesn’t matter what the values are. Then you
can use the in operator as a fast way to check whether a string is in the
dictionary.
"""

""" 
open('words.txt', 'r')
fHand = open('words.txt')
wordDict = dict()
for line in fHand:
    words = line.split()
    for word in words:
        wordDict[word] = ' '
print('for' in wordDict)

 """

""" word = 'brontosaurus'
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1
print(d)
 """
'''
counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
print(counts.get('jan', 0))
print(counts.get('tim', 0))
'''
""" 
word = 'brontosaurus'
d = dict()
for c in word:
    d[c] = d.get(c, 0) + 1
print(d)
 """
""" 
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
print(counts)
 """
"""  
counts = { 'chuck' : 1, 'annie' : 42, 'jan' : 100}
lst = list(counts.keys())
print(lst)
lst.sort()
for key in lst:
    print(key, counts[key])
 """

""" 
import string

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
print(counts)
"""

""" 
Exercise 2: Write a program that categorizes each mail message by
which day of the week the commit was done. To do this look for lines
that start with “From”, then look for the third word and keep a running
count of each of the days of the week. At the end of the program print
out the contents of your dictionary (order does not matter).
Sample Line:
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
Sample Execution:
python dow.py
Enter a file name: mbox-short.txt
{'Fri': 20, 'Thu': 6, 'Sat': 1}
"""

"""
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
counts = dict()
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    if len(words) < 3: continue
    day = words[2]
    if day not in counts:
        counts[day] = 1
    else:
        counts[day] += 1
print(counts)
"""

""" 
Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from
each email address, and print the dictionary.

Enter file name: mbox-short.txt
{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
'ray@media.berkeley.edu': 1}
"""

""" 
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
counts = dict()
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    if len(words) < 2: continue
    email = words[1]
    if email not in counts:
        counts[email] = 1
    else:
        counts[email] += 1
print(counts)
"""

"""
Exercise 4: Add code to the above program to figure out who has the
most messages in the file. After all the data has been read and the dictionary has been created, look through the dictionary using a maximum
loop (see Chapter 5: Maximum and minimum loops) to find who has
the most messages and print how many messages the person has.

Enter a file name: mbox-short.txt
cwen@iupui.edu 5
Enter a file name: mbox.txt
zqian@umich.edu 195
"""

""" 
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
counts = dict()
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    if len(words) < 2: continue
    email = words[1]
    if email not in counts:
        counts[email] = 1
    else:
        counts[email] += 1
maxCount = None
maxEmail = None
for email, count in counts.items():
    if maxCount is None or count > maxCount:
        maxCount = count
        maxEmail = email
print(maxEmail, maxCount)
"""

""" 
Exercise 5: This program records the domain name (instead of the
address) where the message was sent from instead of who the mail came
from (i.e., the whole email address). At the end of the program, print
out the contents of your dictionary.

python schoolcount.py
Enter a file name: mbox-short.txt
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}
"""


fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    if len(words) < 2: continue
    email = words[1]
    domain = email.split('@')[1]
    if domain not in counts:
        counts[domain] = 1
    else:
        counts[domain] += 1
