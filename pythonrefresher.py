###### Variables ##########

age = 27

name = "Brian"

todayisCold = False

print("Hey my name is {} and I'm {}".format(name, age))

if age > 18:
    print("you are older than 18")
else:
    print("you are younger than 18")


if age > 18:
    # do this
elif age < 16:
    # do this
else:
    age == 17:
        # now do this

        # comments or """ multi line """
        # if name == "Brian" or !=




########  Functions ###########

def hello():
    print("hello")

hello()

def hello2(param):
    print("hello" + param)

hello("brian")

def hello3(param1, param2=0):  # default param
    return "hello {} you are {} years old".format(param1, param2)


# Lists are Arrays

# can mutate list
dognames = ["Mila", "Sean", "Zoey"]

# add item to List
dognames.insert(0, "Jane")

# add item to end
dognames.append("Buttons")

# delete item is list
del(dognames[2])

# delete from end   or can add index in pop to get certain item
dognames.pop()

# get length
len(dognames)

# replace item
dognames[1] = "Jane"

# concat list
newlist = mylist + mylist_two  # now combined

# slice
mylist[2:]  # same for strings from position 2 on is included in new list

# sort
mylist.sort()  # sorts list in place
# or sorted
sorted(mylist)

#######  Loops ######
for dog in dognames:
    print(dog)

for x in range(1, 10):
    print(x)  # will print 1-9

for x in range(0, 10, 2):  #3 argument is the step size
    print(x) # 0 2 4 6 8

list(range(0,10,2)) #[0,2,4,6,8]

for num in range(10)
    print(num) # 0 through 9

age = 0
while age < 18:
    print(age)
    age += 1

# Dictionary ###########
    # A dictionary is a collection which is unordered, changeable and indexed.
    # In Python dictionaries are written with curly brackets, and they have keys and values.
dogs = {"Fido": 8, "Sally": 17}

print(dogs["Sally"])  # 17
del(dogs["Sally"])
dogs["Sarah"] = 6  # add

dict = {"key": 1, "key2": [0, 1, 2]}
dict["key2"][2]  # 2
dict["key"] = 3  # assign key a new value
dict.keys()
dict.values()

# Classes  #######

class Dog:
    def bark(self):
        print("Bark")


mydog = Dog()
mydog.bark()

mydog.name = "Fido"

# init functions with Classes

class Dog:
    def __init__(self, name, age, fur):
        self.name = name
        self.age = age
        self.fur = fur

    def bark(self):
        print("Bark")

mydog = Dog("Fido", 13, "Brown")


# Strings ##########
print("The {1} {0} {2}".format("brown", "quick", "fox"))
print("The {q} {b} {f}".format("b = brown", "q = quick", "f = fox"))

# String literals
name = "Jose"
print(f"Hello, my name is {Jose}")


# Float formatting   {value:width.precision f}

result = 100/777
print("The result was {r:1.2f}".format(r=result))  # The result was 104.12


# Tuples ######## , similar to lists but they are immutable (1,2,3)
mytuple = (1, 2, 3, 3)
mytuple.count(3)  # 2
mytuple.index(3)  # 2 only 1st indexof


###### Sets ##########
# unordered collections of unique elements

myset = set()
myset.add(1)

mylist = [1, 1, 1, 2, 2, 2]
set(nymlist)  # {1,2}


mylist.remove(2) # will get error if 2 doesn't exist
mylist.discard(4) # won't get an error if doesn't exist

mylist.clear() #removes all items out of the set

odds = set([1, 3, 5, 7, 9])
evens = set([2,4,6,8,10])

2 in evens
True



#  Comparison Operators ########

1 < 2 and 2 < 3  # True is 1 less than 2 and 2 less than 3
1 == 1 or 2 == 3
not 1 == 1  # false  # returns opposite

# Enumerate function
    # returns index and the object enumerating over
word = 'abcde'

for item in enumerate(word):
    print(item)  # (0, 'a')(1, 'b') etc..  tuples

# Zip function
    # zips items together and returns tuples
    # extra items in 1 list will be ignored.
mylist1 = [1,2]
mylist2 = ['a', 'b']
for item in zip(mylist1, mylist2):
    (1, 'a')
    (2, 'b')

list(zip(mylist1, mylist2)) [(1, 'a'),(2, 'b')]

# In operator

'x' in [1,2,3]
# returns False
'a' in 'a world'
# returns True

d = {'mykey' :345}
345 in d.values()
# True

# Min Max functions

mylist = [1,2,3]
min(mylist)
max(mylist)

# Random function
    # python has built in random library
    # from random import ......

from random import shuffle

mylist = [1,2,3,4]
shuffle(mylist)
# [3,2,4,1]

# get random int
from random import randint

randint(0,100) #range
79
mynum = randint(1,10) # assign it to mynum

# using input

result = input('Enter a number here: ')
Enter a number here:

# the input value is always a string
# int(result) will turn it into an int



# nested loops
mylist = []

for x in [2,4,6]:
    for y in [100,200,300]:
        mylist.append(x*y)
# [200,400,600,400 etc..]


# List Comprehensions  , unique way to quickly create a list
mystring = 'Hello'

mylist = []

for letter in mystring:
    mylist.append(letter)

mylist = []
mylist = [letter for letter in mystring]
#['h', etc...]

mylist = [x for x in 'word']
mylist = [x for x in range(0,11) if x%2==0]

## help method
help(mylist.insert)
#will give you info on the insert meto


# *args  can add many arguments and not a set number, returns a tuple
def myfunc(*args):
    return sum(args)

# **kwargs  keyword arguments,  returns a dictionary
def myfunc(**kwargs):
    if "fruit" in kwargs:
        print('my fruit is {}'.format(kwargs["fruit"]))
    else:
        print("No fruit here")

myfunc(fruit='apple')
#my fruit is apple
