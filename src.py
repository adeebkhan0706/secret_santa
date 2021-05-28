import sys, random, time
from os import system
n=int(input("Number of members in the group: -"))
names=[]
secret_santa_dict={}

for i in range(0,n):
    name=input("Enter name of member:-")
    names.append(name)

def santa_assigner():  
    temp=names[:]
    for i in range(0,n):
        assignee=random.choice(temp)
           
        if assignee==names[i]:               
            i=i-1
            continue

        secret_santa_dict[names[i]]= assignee
        del temp[temp.index(assignee)]

"""print(secret_santa_dict)"""

def display(ch):
    _=system("clear")
    you_gift=secret_santa_dict[str(ch)]
    input("Hi "+ch+" press ENTER to see whose Secret Santa are you")
    print("You are Secret Santa to "+you_gift)
    time.sleep(5)
    
def runner():
    while True:
        
        for i in range(0, n):
            _=system("clear")
            display(names[i])
            _=system("clear")
        flag=input("If you want to repeat the process press ENTER")
        time.sleep(5)
        if flag == True:   
            continue

        else:
            break
santa_assigner()
runner()