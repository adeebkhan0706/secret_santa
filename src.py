import sys, random
n=input("Number of members in the group")
names=[]
for i in range(0,n):
    name=input("Enter name of member",(i+1))
    names.append(name)

secret_santa_dict=()
for i in range(0,n):
    secret_santa_dict[names[i]]= random.choice(names)

print(secret_santa_dict)