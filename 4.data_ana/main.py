import os
import sys
name=open("./name.txt","r").readlines()
vote=open("./vote.txt","r").readlines()
f=open("./vote1.txt","w")
NUM=0
dict={}
for i in vote:
    n=len(i.split())
    if n==1 and i in name:
        dict[i[:-1]]=dict.get(i[:-1],0)+1
        NUM+=1
    else:
        f.write(i)
f.close()
l=list(dict.items())
l.sort(key=lambda x:x[1],reverse=True)
print('{}{}{}'.format(NUM,l[0][0],l[0][1]))
    