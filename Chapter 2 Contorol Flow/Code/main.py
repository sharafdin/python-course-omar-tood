# x = 6
# if x > 5:
#     print('x is greater than 5')
# elif x == 5:
#     print('x is 5')
# else:
#     print('x is less than 5')

# number = int(input('enter the number: '))

# if number % 2 == 0:
#     print('the number is even')
# else:
#     print('the number is odd')

# print(4 / 2)
# print(4 % 2)

# print(3 ** 2)

# print(15 / 6)
# print(int(15 / 6))
# print(15 // 6)

# x = 10

# x = x + 1

# x += 1

# print(x)

# y = 10

# y -= 1 # y = y - 1

# print(y)

# x = 10
# y = 4

# print(x > y)
# print(x < y)

# print(10 >= 4)
# print(10 <= 10)

# x = 4
# y = 6

# print(4 == 4)

# print(x == y)

# print(x != y)

# x = 4
# y = 6
# z = 10

# print(x < y and z > x)
# print(x < y or z < x)

# print(not(x < y))

# for i in range(10):
#     print('Sharafdin')

# name = 'Sharafdin'

# for char in name:
#     print(char)

# colors1 = ["red", "green", "blue"]
# colors2 = ["yellow", "orange", "purple"]

# for color1 in colors1:
#     for color2 in colors2:
#         print(color1, color2)

# i = 0
# while i < 10:
#     print('Sharafdin')
#     i += 1

while True:
    print('Enter (mi) miles or (km) kilometers')
    choice = input('Enter mi or km: ').lower()
    if choice == 'q':
        break
    elif choice == 'mi':
        km = float(input('KM?: '))
        mi = km / 1.609
        print(f'{km} kilometers is equal to {mi} miles')
    elif choice == 'km':
        mi = float(input('MI?: '))
        km = mi * 1.609
        print(f'{mi} miles is equal to {km} kilometers')
    else:
        print('Invalid, please try again...')