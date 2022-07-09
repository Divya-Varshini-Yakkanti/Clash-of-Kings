import os
import sys

def Replay(f_name):
    with open(f_name,'r') as f:
        no=0
        lines=f.readlines()
        lis=[]
        
        for l in lines:
            lis.append(l)
            no+=1
            if(no%100==0):
                os.system('clear')
                print(''.join(lis))
                os.system('sleep 0.175')
                lis=[]

replaynum=input("Enter replay number: ")
f_name="./replays/replay-"+replaynum+".txt"
Replay(f_name)