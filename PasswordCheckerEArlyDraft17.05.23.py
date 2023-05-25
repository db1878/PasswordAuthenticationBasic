import time
total_users = 0
users = {}
def isvalid_username(username):
    allowed_chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                     "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A",
                     "B", "C", "D", "E", 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                     'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    if len(username) == 0:
        print("Username Cannot be empty!")
        return False
    #if the username is empty have to restart
    if not username.strip():
        print("Username Cannot Have Spaces!")
        return False
    #if the username has space have to restart
    for char in username:
        if char not in allowed_chars:
            print("Invalid Username: Only use non special Characters and Numbers!")
            return False
        #if the username not in alphabet + numbers then have to restart
    if username in users:
        print("Username Already Taken!")
        return False
    # if username is taken restart
    return True
#if evrythang is good carry on


def isvalid_password(password):
    #if username and password the same restart
    if len(password) == 0:
        print("Password Cannot be Empty")
        return False
    #if the password is empty restart
    length = len(password)
    if length < 5:
        print("Password Too Short: Password should be between 5 and 24 characters")
        return False
    #does what it says on the tin
    if length > 24:
        print("Password too long: Password should be between 5 and 24 characters")
        return False
    if password == username:
        print("Username and password Cannot be the same!")
        return False
    #ditto
    return True
# if everything is valid then it carries oon

def new_account():
    global username
    while True:
        print("Please Enter USername and password below")
        username = input("Enter Username ")
        if not isvalid_username(username):
            #checks if the value is true, if it isnt the while loop stops running
            continue
        password = input("\nEnter password ")
        if not isvalid_password(password):
            #ditto
            continue
        print("Your username is:", username, "and your password is:", password)
        print("Is this correct?")
        answer = input("Type yes or no ").lower()
        while answer not in ["yes", "no"]:
            #checkls to see if user wants this username and password
            answer = input("Type yes or no").lower()
        if answer == "no" :
            continue
            #starts the function again
        else:
            users.update({username:password})
            #adds the username and password to the dictionary users
            print("Welcome,", username, "!")
        global total_users
        total_users += 1
        print("Would you like to make another account?")
        answer = input("Type 'yes' or 'no': ").lower()
        while answer not in ["yes", "no"]:
            answer = input("Type 'yes' or 'no': ").lower()
        if answer == "no":
            print("Your account has been created successfully")
            break



def verify_account():
    tries = 3
    while tries > 0:
        print(users)
        username_entry = input("Please Re-enter your username ")
        if username_entry not in users:
            print("Invalid username")
            continue
        password_entry = input("Please enter your password ")
        if users[username_entry] == password_entry:
            print("Access Granted")
            break
        else:
            if tries > 0:
                print("Username or password incorrect. Please try again.")
                print("You have", tries, "attempt(s) left.")
            else:
                print("Too many failed attempts: Access denied.")
                quit()
            tries -= 1




new_account()
print("verify ur acc")

verify_account()
