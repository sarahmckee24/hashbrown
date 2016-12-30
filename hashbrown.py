#!/usr/bin/env python

from os import listdir
from os.path import isfile, join

VERSION = "0.0.1"

def printInit():
    print("Hashbrown")
    print("Version: " + VERSION)
    print("===================")
    print("")
    stageone = int(raw_input("(0) Login or (1) Create Profile: "))
    if(stageone==0):
        selectUser()
    elif(stageone==1):
        createUser()

def selectUser():
    users = [f for f in listdir("usrs/") if isfile(join("usrs/", f))]
    inpoot = ''

    #Get rid of DS_store file, only print .usr files
    for i, user in enumerate(users):
        print(str(i)+": "+user)
    userPicked = False

    #Add more Validation!!
    while(userPicked==False):
        inpoot = raw_input("Select User: ")
        user = users[int(inpoot)]
        userPicked = True
    userFile = open('usrs/'+str(i)+'.usr', 'r')
    userInfo = userFile.readline().rstrip('\n').split(',')
    password = raw_input("Password: ")
    if(userInfo[2]==password):
        loginUser(userInfo[0], userInfo[1])

def createUser():
    passwordSet = False
    name = raw_input("Username: ")
    password = ""
    password2 = ""

    while(passwordSet == False):
        password = raw_input("Password: ")
        password2 = raw_input("Re-enter Password: ")
        #Better Validation
        if(password==password2):
            passwordSet = True
        else:
            print("Passwords don't match, retype passwords!!")

    #BEtter way to get ID of new user
    users = [f for f in listdir("usrs/") if isfile(join("usrs/", f))]
    ID = len(users)

    #Add hashing to password!!!!
    userFile = open('usrs/'+str(ID)+'.usr', 'w+')
    userFile.write(str(ID)+","+name+","+password)
    loginUser(ID, name)

def loginUser(userId, username):
    #Create User Object
    print("Logged In "+username+"!")

if __name__ == "__main__":
    printInit()
