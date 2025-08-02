#checking username
#username can't be more than 12 characters
#username can't contain digits 
#username can't contain spaces

username = input("Enter your username:")
if len(username) > 12:
    print("username can't be greater than 12.")
elif any(char.isdigit() for char in username):
    #If any character in the username is a digit, show an error message. where 'any', as soon as it finds true in the whole expression, runs the code in the if statement. And the rest of the expression is called generator expression.
    print("Username can't contain digits!")
elif not username.find(" ") == -1:
    print("username can't contain spaces!")
else:
    print(f"welcome {username}")
