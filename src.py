import sys, random
n=int(input("Number of members in the group: -"))
names=[]
for i in range(0,n):
    name=input("Enter name of member:-")
    names.append(name)

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



print(secret_santa_dict)
