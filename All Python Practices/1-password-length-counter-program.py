full_name = input("Enter Your Name: ")
password = input("Enter your password: ")

length_password = len(password)

hidden_password = '*' * len(password)

print(f"Hello! {full_name}, your password {hidden_password} is {length_password} letters long")