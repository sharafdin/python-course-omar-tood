# def greeting():
#     print("Hello, world")

# greeting() 

# def greeting(name):
#     print(f'Hello {name}!')
    
# greeting("Omar","oksdjdf")

# def add(a,b):
#     return a+b
# result = add(3,5)
# print(result)
# 1,3,4,677, = 84  total 

# def sum_numbers(*number):
#     total = 0;
#     for num in number:
#         total += num
#     return total  
# result = sum_numbers(10,20,40,50,60,70,80) 
# print(result) 


# def my_function(*number):
#     for num in number:
#         print(num)

# my_function(1,2,3,4,5,6,7,8)


# def getNames(**kwargs):
#     for key, value in kwargs.items():
#         print(f'{key}: {value}')
        
    
# getNames(name="Omar", age= 23, city ="Mogadishu", email="Omar@gmail.com" )




# global_variable = 10;

# def my_function():
#     local_variable =20
#     print(global_variable)
#     print(local_variable)

# my_function()  

# print(global_variable) 
    
    

# def find_maximum(*numbers):
#     if len(numbers) == 0:
#         return "No numbers provided."
#     maximum = numbers[0]
#     for num in numbers:
#         if num > maximum:
#             maximum = num
#     return maximum

# number_List = [10,100,200,1000,10000]
# maximum_number = find_maximum(*number_List)
# print(f'The maximum Number is {maximum_number}')


# def check_password_length(password , min_length):
#     if len(password) >= min_length:
#         return True
#     else:
#         return False
    
# password = input("Enter Your Password: ")
# minimum_length = 8;
# if check_password_length(password ,minimum_length):
#     print("Password meets the minimum length requirement")
# else:
#     print("Password  does not meets the minimum length requirement")



# def age_teller():
#     current_year = 2023
#     birth_year = int(input('Enter Your Birth Year:'))
#     age = current_year - birth_year
    
#     if age < 0:
#         print("Invalid birth Year. Please try again")
#     elif age > 150:
#         print(f"You seem to be too old to use this system. and Your age {age}")
#     else:
#         print(f'You are {age} years old.')

# age_teller()

# def calculate_total_grade(grades):
#     total = sum(grades)
#     return total
# grades = [100,90,89,88,90,78]
# total_grades = calculate_total_grade(grades)
# print(f'Total Grades: {total_grades}')
    
    
    
balance  = 0.0
def deposit(amount):
    global balance
    balance += amount
    print(f'Deposit of {amount} successful. Current Balance: {balance}')

def withdraw(amount):
    global balance
    if balance >= amount:
        balance -= amount
        print(f'Withdrawal of {amount} successful. Remaining Balance: {balance}')
    else:
        print('Insufficient funds!. Withdraw Unsuccessful')
        
def get_balance():
    return balance

def perform_payment():
    deposit(400)
    withdraw(50)
    withdraw(70)
    withdraw(280)
    withdraw(100)
    deposit(4000)
    current_balance = get_balance()
    print(f'Current Balance: {current_balance}')
    
perform_payment()

    












    



