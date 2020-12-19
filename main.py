import json
import time


def storeTheDate(name, password):

    is_firstTime = True
    with open('db.json', 'r+') as file:
        d = file.read()
    if len(d) > 0:
        is_firstTime = False
    else:
        is_firstTime = True

    current_Data = {name: [name, password]}

    if is_firstTime:
        with open('db.json', 'w+') as file:
            data = current_Data
            json.dump(data, file)
            print("You Successfully Create your Account")
            is_firstTime == False
    elif not is_firstTime:
        with open('db.json', 'r+') as file:
            previous_data = json.load(file)
        with open('db.json', 'w+') as file:
            new_data = {**previous_data, **current_Data}
            json.dump(new_data, file)
            print("You Successfully Create your Account")


def checkUser(username):
    with open('db.json', 'r+') as file:
        data = json.load(file)
        if username in data:
            return True
        elif len(file.read()) > 0:
            return False
        else:
            return False


def checkPassword(username, password):
    with open('db.json', 'r+') as file:
        data = json.load(file)
        if username in data:
            if data[username][1] == password:
                return True
            else:
                return False


def handleCommandLine():
    print("""My First Python Project

          press 1 for Create a New Account

          press 2 for Login
  """)

    choice = input("Enter the option !")

    while str(choice) != str(1) and str(2) and '':
        choice = input("Enter the option correctly!")

    is_firstTime = True
    with open('db.json', 'r+') as file:
        d = file.read()
    if len(d) > 0:
        is_firstTime = False
    else:
        is_firstTime = True

    if int(choice) == 1:
        newAccount()
    elif int(choice) == 2 and is_firstTime == False:
        Login()
    else:
        print("No Data Found For Login")
        handleCommandLine()


def newAccount():
    is_firstTime = True
    with open('db.json', 'r+') as file:
        d = file.read()
    if len(d) > 0:
        is_firstTime = False
    else:
        is_firstTime = True

    if is_firstTime:
        name = input("Enter your Name ?")
        while name == '':
            name = input(
                "UserName Wrong or already Taken ? Enter New UserName ?")
        password = input("Enter your Password ?")
        while password == '' or len(str(password)) < 8:
            password = input("Your Password Must Have 8 Characters ?")
        storeTheDate(name, password)
    if is_firstTime == False:
        name = input("Enter your Name ?")
        while name == '' or checkUser(name) == True:
            name = input(
                "UserName Wrong or already Taken ? Enter New UserName ?")
        password = input("Enter your Password ?")
        while password == '' or len(str(password)) < 8:
            password = input("Your Password Must Have 8 Characters ?")
        storeTheDate(name, password)

    handleCommandLine()


def Logout(username):
    print('Logd Out Bro')
    print(f'Come Again bro {username}')

    handleCommandLine()


def Login():
    with open('db.json', 'r+') as file:
        d = file.read()
    name = input("Enter your UserName ?")
    while checkUser(name) == False:
        name = input("Olunga Enter Pannula Mandaya UserName !")
        continue

    if checkUser(name) == True:
        password = input("Enter The Password Bro ? ")
        while checkPassword(name, password) == False:
            password = input("Enter The crct Password Bro Mannangatti ? ")

        print("Access Granted")
        print(f'Welcome Ney! {name} {password}')
        print("Wait For 1 sec")
        time.sleep(1)
        print("Lets Logout")
        Logout(name)


# Login()
with open('db.json', 'w+') as file:
    d = file.read()
handleCommandLine()
