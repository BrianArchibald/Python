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

# get lenght
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

age = 0
while age < 18:
    print(age)
    age += 1

    # Dictionary ###########
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


#  Comparison Operators ########

1 < 2 and 2 < 3  # True is 1 less than 2 and 2 less than 3

1 == 1 or 2 == 3

not 1 == 1  # false  # returns opposite
