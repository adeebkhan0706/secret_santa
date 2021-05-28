import sys, random, time
from os import system
n=int(input("Number of members in the group: -"))
names=[]
secret_santa_dict={}
for i in range(0,n):
    name=input("Enter name of member:-")
    names.append(name)
def santa_assigner():  
    secret_santa_dict={}
    temp=names[:]
    for i in range(0,n):
        while True:
            assignee=random.choice(temp)
            
            if assignee==names[i]:
                continue
            else:
                break

        secret_santa_dict[names[i]]= assignee
        del temp[temp.index(assignee)]

"""print(secret_santa_dict)"""

def display(ch):
    you_gift=secret_santa_dict[ch]
    input("Hi "+ch+" press ENTER to see you gift")
    print(you_gift)
    time.sleep(5)
    
def runner():
    while True:
        for i in range(0, n):
            _=system("clear")
            display(names[i])
            _=system("clear")
        print("")