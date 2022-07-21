def bake(what):
    print('Baking {}'.format(what))

def add(what):
    print('Adding {}'.format(what))

def mix(what):
    print('Mixing {}'.format(what))

cookbook = [(add, 'milk'), (add, 'eggs'), (add, 'flour'), (add, 'sugar'), (mix, 'ingredients'), (bake, 'cookies')]

for activity, obj in cookbook:
    activity(obj)

print('*' * 30)

def cook(activity, obj):
    activity(obj)

cook(bake,'brownies')

for activity, obj in cookbook:
    cook(activity,obj)

print('*' * 30)

def say_hello(name):
    print("Hello {}!".format(name))
 
def say_good_morning(name):
    print("Good morning {}!".format(name))
 
def greet(how, name):
    how(name)
 
greet(say_hello, 'Captain')

print('*' * 30)

def say_hello(name):

    print("Hello {}!".format(name))

def say_good_morning(name):

    print("Good morning {}!".format(name))

def greet(how, name):

    how(name)

greet(say_good_morning,'Captain')

print('*' * 30)

def double(x):
    return 2 *x
 
def square(x):
    return x**2
 
def negative(x):
    return -x
 
def div2(x):
    return x/2
 
 
def generate_values(how, x_table):
 
    value_list = []
    
    for x in x_table:
        value_list.append(how(x))
 
    return value_list
 
 
x_table = list(range(11))
 
print(generate_values(double, x_table))
print(generate_values(square, x_table))
print(generate_values(negative, x_table))
print(generate_values(div2, x_table))