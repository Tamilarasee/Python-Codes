# weight convertor
'''
weight = int(input('Weight: '))
unit = input('(L)lbs or (K)kg ')
if unit.upper() == 'L':
    msg = f'you are {weight * 0.45} kilos'
elif unit == 'K' or unit =='k':
    msg = f'you are {weight / 0.45} lbs'
print(msg)


#Car game

start = False
while True:
        prompt = input().lower()
        if prompt == 'start':
            if start:
                print("started already")
            else:
                print("started")
                start = True
        elif prompt == 'stop':
            if not start:
                print("stopped already")
            else:
                print("stopped")
                start = False
        elif prompt == 'help':
                print("""
start - to start the car
stop - to stop the car
quit - to exit 
                """)
        elif prompt == 'quit':
            break
        else:
            print('I dont understand')


#printing F in x

numbers = [5,2,5,2,2]
for num in numbers:
    letter = ""
    for i in range(num):
        letter += 'x'
    print(letter)


#largest number - also created module
numbers = [44,3,7,10,35]
max=numbers[0]
for i in numbers:
    if max<i:
        max=i
print(max)


#Remove duplicates in a list
numbers = [44,3,7,7,3,10,35]
distinct = []
for num in numbers:
    if num not in distinct:
        distinct.append(num)
numbers=distinct.copy()
print(numbers)


#dictionary example
phone = input ("Phone: ")
num_letters = {'0': "zero", '1': "one", '2':"two", '3':"three", '4': "four", '5': "five", '6': "six", '7': "seven",
               '8': "eight", '9': "nine"}
word = ""
for digit in phone:
    word+=(num_letters.get(digit,'!')) + ' '
print(word)



#smiley with function

def smile(message):
    word = message.split(' ')
    smilies = {':)': '😅', ':(': '😋'}
    final = ""
    for word in word:
        final+= smilies.get(word, word) + ' '
    return final


msg = input('> ')
print(smile(msg))



#try and catch

try:
    age = int(input('Age: '))
    Income = 200000
    risk = Income/age
    print(age, risk)
except ValueError:
    print("Invalid value.Enter numbers only ")
except ZeroDivisionError:
    print("Age cannot be zero")


#Class-new user defined type , #def __init__ is a constructor
class Point:
    def move(self):
        print("Move")

    def draw(self):
        print("Draw")

    def __init__(self,x,y):
        self.x= x
        self.y=y


pt = Point(10,20)
print(f'({pt.x},{pt.y})')


class Person:
    def __init__(self,name):
        self.name = name

    def talk(self):
        print(f'Hi, I am {self.name}')

john = Person("Jhonny")
john.talk()



#Inhertiance
class Mammal:
    def walk(self):
        print("Walk")

class Dog(Mammal):
    def bark(self):
        print("bark")

class Cat(Mammal):
    def meow(self):
        print("Meow")

cat1 = Cat()
cat1.walk()
cat1.meow()
dog1=Dog()
dog1.bark()
dog1.walk()



#modules - created utils file with function for largest num
#2 ways

import utils
print(utils.find_max([1,4,6,3,0,-11]))

from utils import find_max
print(find_max([1,4,8,3,0,-11]))



# Packages - created pack - ecommerce and a module in it with a function which we call below

import ecommerce.shipping
ecommerce.shipping.shipping_cost()

from ecommerce import shipping
shipping.shipping_cost()

from ecommerce.shipping import shipping_cost
shipping_cost()



# using built in packages and modules -random
import random
class Dice:
    def roll(self):
        return random.randint(1, 6), random.randint(1, 6)


dice1 = Dice()
print(dice1.roll())


#accessing paths

from pathlib import Path
path = Path()
for file in path.glob('*'):
    print(file )

#slicing
a ="Tamil"
b=slice(3)
print(a[b])



# define the Vehicle class example
class Vehicle:
    def __init__(self, name, kind, color, value):
        self.name = name
        self.kind = kind
        self.color = color
        self.value = value

    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str


car1 = Vehicle("Fer", "convertible", "red", 60000.00)
car2 = Vehicle("Jump", "Jump", "blue", 10000.00)
# test code
print(car1.description())
print(car2.description())

#understanding list outputs - Run and check
a = []
b= [2,3]
a = b
b.append(4)
print(a)


#printing in same line with multiple print statements
print("Hi,", end="  ")
print("How are you?")

#You are given an array A of N  integers. The task is to determine if the value of frequency of each element in the array is unique.
test_case = int(input())
for test in range(test_case):
    size = input()
    num_list = input().split(' ')
    value = set(num_list)
    freq = []
    for num in value:
        freq.append(num_list.count(num))
    freq_count = set(freq)
    if len(freq_count)==len(freq):
        print("Yes")
    else:
        print("No")


#Pivot Index
# You are given an array A of N integers. The task is to determine the pivot index of the given array.The pivot index is defined as the index where the sum of all the numbers to the left of the index is equal to the sum of all the numbers to the right of the index.
# test_case = int(input())
# for test in range(test_case):
size = input()
num_list = input().split(' ')
num_list = [int(num) for num in num_list]
total_sum = sum(num_list)
left_sum = 0
right_sum = total_sum
for index, num in enumerate(num_list):
    right_sum -= num
    print(index,left_sum,right_sum)
    if left_sum == right_sum:
        print(index)
        break
    else:
        left_sum += num
if left_sum != right_sum:
    print("-1")

# different method for above

size = input()
num_list = input().split(' ')
num_list = [int(num) for num in num_list]
for index in range(len(num_list)):
    left_sum = sum(num_list[:index])
    right_sum = sum(num_list[index+1:])
    print(left_sum,right_sum)
    if  left_sum== right_sum:
        print(index)
        break
    else:
        continue
if left_sum != right_sum:
      print("-1")

# Print all combinations
# of balanced parentheses

def generateParenthesis(left, right, s, answer):
    # terminate
    if left == 0 and right == 0:
        answer.append(s)
    if left > right or left < 0 or right < 0:
        # wrong
        return
    s += '{'
    generateParenthesis(left - 1, right, s, answer)
    s = s[:-1]
    s += '}'
    generateParenthesis(left, right - 1, s, answer)
    s = s[:-1]


n = 3
# list ans is created to store all the possible valid
# combinations of the parentheses.
ans = []
s = ""
# initially we are passing the counts of open and close
# as 0, and the string s as an empty string.
generateParenthesis(n, n, s, ans)
# Now, here we print out all the combinations.
for k in ans:
    print(k)
 '''


