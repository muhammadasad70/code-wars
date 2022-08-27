user_name=input("enter your name:\n")
password=input("enter your password")
password_length=len(password)
hiidden_password='*'*password_length
print(f'{user_name},your password {hiidden_password} is {password_length} letters  long:')
