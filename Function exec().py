var_x = 10
var_y = 10
source = input("wprowadz zmienna dostępu do minecraft")

result = exec(source)

print(result)

print(var_x)

print('*'*30)

source = '''
new_var = 1
for i in range(var_y):
    print('-' * i)
    new_var += i
'''

result = exec(source)

print(result)
print(new_var)
print(var_y)

source = input("Enter your expression: ")
print(eval(source))

print('*'*30)

import os

# if you want to use it, adjust the path to the files

files_to_process = [
    r"/home/sebastian/python_code_repo/python_code_exercises/math_sin_square.py",
    r"/home/sebastian/python_code_repo/python_code_exercises/math_square_root.py"
]

for file_path in files_to_process:
    with open(file_path, 'r') as f:
        print("File {} ...".format(os.path.basename(file_path)))
        source_file = f.read()
        exec(source_file)

