list_A = list(range(6))
list_B = list(range(6))

print(list_A, list_B)

print('-----'*30)

product = []



gen = ((a,b) for a in list_A for b in list_B if a % 2==1 and b % 2==0)
print("generator", gen)

print('-----'*30)

print("generator", next(gen))
print("generator", next(gen))

print('-----'*30)

for x in gen:
    print(x)

print('****'*30)

for x in gen:
    print(x)

print('****'*30)

gen = ((a,b) for a in list_A for b in list_B if a % 2==1 and b % 2==0)
while True:
    try:
        print(next(gen))
    except StopIteration:
        print('all values have been generated')
        break

print('****'*30)

ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ', 'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

routes = ((start, stop) for start in ports for stop in ports)

counter = 0

for (start, stop) in routes:
    print('{} - {}'.format(start,stop))
    counter += 1

print(counter)

print('****'*30)

routes = ((start, stop) for start in ports for stop in ports if start != stop)

counter = 0

for (start, stop) in routes:
    print('{} - {}'.format(start, stop))
    counter += 1

print(counter)

print('****'*30)

routes = ((start, stop) for start in ports for stop in ports if start < stop)

counter = 0
for (start, stop) in routes:
    print('{} - {}'.format(start, stop))
    counter += 1

print(counter)