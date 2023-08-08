name = input('Enter your name: ')
password = input('Enter your password: ')

hidden_password = '*' * len(password)

len_pass = len(password)

print(f'ASC, {name} your password {hidden_password} is {len_pass} letters long')