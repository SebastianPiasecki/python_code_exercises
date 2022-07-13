list_A = list(range(6))
list_B = list(range(6))

print(list_A, list_B)

print('-----'*30)

product = []

for a in list_A:
    for b in list_B:
        product.append((a,b))
print("ver_1", product)

print('-----'*30)

product = [(a,b) for a in list_A for b in list_B]
print("Ver_2", product)

print('-----'*30)

product = [(a,b) for a in list_A for b in list_B if a % 2==1 and b % 2==0]
print("Ver_3", product)

print('-----'*30)

product = {a:b for a in list_A for b in list_B if a % 2==1 and b % 2==0}
print("Ver_4", product)

print('-----'*30)

numbers = list(range(1,10))
 
new_numbers = [x**2 for x in numbers]
print(new_numbers)

print('-----'*30)

tie = ['green tie', 'gray tie', 'red tie']
shirt = ['white shirt', 'blue shirt', 'green shirt']

print(["I wear {} with {}".format(t,s)for t in tie for s in shirt])

print('-----'*30)

clients = ['A-company', 'B-company']
projects = [300,400,1500,2340,50]

investments = [(c,p) for c in clients for p in projects if c == 'A-company' and p<1000 or c=='B-company' and p>=1000]
print(investments)

print('-----'*30)

ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ','LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

routes = [ (start, stop) for start in ports for stop in ports]
print(routes)
print(len(routes))

print('-----'*30)

routes = [ (start, stop) for start in ports for stop in ports if start != stop]
print(routes)
print(len(routes))

print('-----'*30)

routes = [ (start, stop) for start in ports for stop in ports if start < stop]
print(routes)
print(len(routes))