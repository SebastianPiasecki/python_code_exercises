var_x = 10
password = 'My super secret password'

source = 'var_x + 2'

result = eval(source)
print(result)

# disadvantages - the user can enter a variable 'password' and retrieve our password

source = 'password'

result = eval(source)
print(result)

print(globals())
print('*'*30)

# how to protect yourself from an office hacker ver_1 :)

source = 'password'

# globals = globals().copy()
# del globals['password']

# result = eval(source, globals)
print(result)

print('*'*30)

# how to protect yourself from an office hacker ver_2 :)


# globals = {}

# result = eval(source, globals)
print(result)

print('*'*30)

# but... :(

source = '__import__("os").getcwd()'   
globals = {} 

result = eval(source, globals)
print(result)

import math

argument_list = []

for i in range(100):
    argument_list.append(i/10)
formula = input("Please enter a formula, use 'x' as the argument: ")

for x in argument_list:
    print("{0:3.1f} {1:6.2f}".format(x, eval(formula)))

