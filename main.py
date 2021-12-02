from user import User

#Dictionary creation.
users = {}

status = True

#Creates New User
def new_user():
    global n_user

    name = input("What is your name: ")
    tel = input("Please enter your phone number: ")
    mail = input("We'd be glad to have your email: ")
    n_user = User(name, tel, mail)

    users[n_user.name] = {'name': n_user.name, 'tel': n_user.tel, 'mail': n_user.mail}
    print(users)

#Login if old user
def old_user():
    login =input("Enter your name: ")

    if login in users:
        print("Login successful!")
        print("Welcome ", n_user.name, "!\n")
        
        log_status = True
        while log_status:

            print("Choose on of the actions bellow:")
            option = input("Type 'i' to show your details or Type 'r' to remove user:  ")

            if option == 'i':
                print(users)
            elif option == 'r':
                users.pop(login)
                log_status = False

    else:
        print("User doesn't exist!")

while status:
    choice =input("Are you a registered user? (Yes/y)  or (No/n)? Press q to quit: ")
    if choice == "Yes" or choice == 'y':
        old_user()
    elif choice == "No" or choice == 'n':
        new_user()
    elif choice == "q":
        status = False
       