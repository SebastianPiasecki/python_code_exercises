def DisplayOptions(skrypt):
    for i in range(len(skrypt)):
        print("{} - {}".format(i + 1, skrypt[i]))

    choice = input("Wprowadz dane 1: load data, 2: export data, 3: analyze $ predict ")
    return choice

choice = 'x'
skrypt = ['load data', 'export data', 'analyze & predict']

while choice:
    choice = DisplayOptions(skrypt)
    if choice:
        try:
            choice_num = int(choice) -1
            if choice_num >= 0 and choice_num < len(skrypt):
                print("you have selected {} - {}".format(choice_num+1, skrypt[choice_num]))
            else:
                print("choose a value from a list or press enter")
        except:
            print("You need to enter a number")
    else:
        print('-------END-------')