import datetime
import time

def buy_me(prefix, what): 
    print(prefix, what)
    return

prefix = 'Please buy me'
what = 'a new car'

buy_me(prefix, what)

def show_progress(how_many, character = '*'):
    line = character * how_many
    print(line)

show_progress(10)
show_progress(15)
show_progress(30)
show_progress(10, '-')
show_progress(15, '+')

def buy_me_2(prefix_2, what_2, *args, **kwargs):
    print(prefix, what)
    print(args)
    print(kwargs)

buy_me_2('Please buy me', 'a new car', 'a cat', 'a dog', 'a dragon', shop = 'market', color = 'any')

print('*' * 30)

products = ['milk', 'bread', 'flakes']
parameters = {'price':'low', 'time':'now'}

buy_me_2('Buy me', 'newspaper', *products, **parameters)

def search_words(*args):
    print(args)
list_of_words = ['acceptance', 'criteria', 'requirements']

search_words(*list_of_words)

print('*' * 30)

def calculate_paint(efficency_ltr_per_m2, *rooms):
    total_area = sum(rooms)
    paint = total_area * efficency_ltr_per_m2
    return paint

print(calculate_paint(0.25, 42, 28, 30))
rooms = [42, 28, 30]
print(calculate_paint(0.25, *rooms))

print('*' * 30)

start = datetime.datetime.fromtimestamp(time.time())
start = str(start.strftime('%Y-%m-%d %H:%M:%S'))

def log_it(*args):
    path =r'C:\Mój GitHub\python_code_exercises\log_it.txt'
    with open(path, "a") as f:
        for line in args :
            f.write(line)
            f.write(' ')
        f.write("\n")

log_it('Starting processing forecasting', start)
log_it('ERROR', 'Not enough data', 'invoices', '2020', start)


