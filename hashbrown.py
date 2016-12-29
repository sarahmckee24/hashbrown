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
        printUsers()
    elif(stageone==1):
        print("create user")

def printUsers():
    users = [f for f in listdir("usrs/") if isfile(join("usrs/", f))]
    for i, user in enumerate(users):
        print(str(i)+": "+user)

if __name__ == "__main__":
    printInit()
