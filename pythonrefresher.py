###### Variables

age = 27

name = "Brian"

todayisCold = False

print("Hey my name is {} and I'm {}".format(name, age))

if age > 18:
    print("you are older than 18")
else:
    print("you are younger than 18")


# comments or """ multi line """

# if name == "Brian" or !=

########  Functions
def hello():
    print("hello")

hello()

def hello2(param):
    print("hello" + param)

hello("brian")

def hello3(param1, param2=0): #default param
    return "hello {} you are {} years old".format(param1, param2)


#####  Lists are Arrays

dognames = ["Mila", "Sean", "Zoey"]


# add item to List
dognames.insert(0, "Jane")

# delete item is list
del(dognames[2])

# get lenght
len(dognames)

# replace item
dognames[1] = "Jane"


# Loops
for dog in dognames:
    print(dog)

for x in range(1,10):
    print(x)  # will print 1-9

age = 0
while age < 18:
    print(age)
    age += 1