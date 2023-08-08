print('Welcome to distance converter program')
while True:
    choice = input('(MI) for miles, (KM) for kilometers & (q) for quit: ').lower()
    if choice == 'q':
        break
    elif choice == 'mi':
        km = int(input('Enter the kilometers: '))
        mi = km / 1.609
        print(f'{km} killometers is {mi} miles')
    elif choice == 'km':
        mi = int(input('Enter the miles: '))
        km = mi * 1.609
        print(f'{mi} miles is {km} killometers')
    else:
        print('Invalid! please try again.')