for i in range(10, 0, -3):
    print(i)

list_ = list(range(10))
print('List :', list_, type(list_), id(list_))

print(list_[5:-1])

print(list_[-2:])

list2 = list_[:]
print('List :', list2, type(list2), id(list2))


list3 = list(range(20))
print(list3)


def get_list_of_colors(colors, n):
    return colors[:n]

colors = ["red", "orange", "green", "violet", "blue", "yellow"]

for i in range(1, len(colors)+1):
    print(get_list_of_colors(colors,i))

work_days = [19, 21, 22, 21, 20, 22]
print(work_days)

enumerate_days = list(enumerate(work_days))
print(enumerate_days)

for pos , value in enumerate_days:
    print('Position:', pos, 'Value:', value)

months = ['I', 'II', 'III', 'IV', 'V', 'VI']

months_day = zip(months, work_days)
months_day = list(months_day)
print(months_day)

for m, d in months_day:
    print('Month', m, 'Day', d)

for pos, (m, d) in enumerate(zip(months, work_days)):
    print('Position', pos, 'Month', m, 'Day', d )


projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']


leaders_project = list(zip(projects, leaders))
print(leaders_project)

for p, l in leaders_project:
    print('The laeders of', p, 'is', l)

dates = ['2016-06-23', '2016-08-29', '1994-01-01']

nowa_lista = list(zip(dates, projects, leaders))

print(nowa_lista)

for d, p, l in nowa_lista:
    print('The leader of', p, 'started', d, 'is', l)

for e, (d, p, l) in enumerate(zip(dates, projects, leaders)):
    print(e+1, 'The leader of', p, 'started', d, 'is', l)