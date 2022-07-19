from dis import Instruction


def buy_me(what):
    print('Give me', what)

buy_me('a new car')

print('*' * 30)

steal_for_me = buy_me

steal_for_me('a new car')

print('*' * 30)

def go_left(*args):
    print('PLACEHOLDER - turning left with', *args)

def go_right(*args):
    print('PLACEHOLDER - turning right with', *args)

def go_forward(*args):
    print('PLACEHOLDER - going forward with', *args)

def go_back(*args):
    print('PLACEHOLDER - going back with', *args)

def start(*args):
    print('PLACEHOLDER - starting with', *args)

def stop(*args):
    print('PLACEHOLDER - stopping', *args)

instruction = [start, go_forward, go_forward,  go_left, go_forward, go_right, stop]

dish = 'pizza'
for instr in instruction:
    instr(dish)

print('*' * 30)

def double(x):
    return 2 * x

def square(x):
    return x ** 2

def negative(x):
    return -x

def div2(x):
    return x/2

number = 8

transformations = [double, square, negative, div2]

print('Starting transformations')
tmp_return_value = number

for transformation in transformations:
    tmp_return_value = transformation(tmp_return_value)
    print('{}: temporal result is {}'.format(transformation.__name__, tmp_return_value))

number = 125
transformations = [square, square, div2, double]

print('Starting transformations')
tmp_return_value = number

for transformation in transformations:
    tmp_return_value = transformation(tmp_return_value)
    print('{}: temporal result is {}'.format(transformation.__name__, tmp_return_value) )
