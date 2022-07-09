from src.input import input_to
from src.main import village
from os.path import exists

no=1
Village = village()

f_name = "./replays/replay-"
while(1):
    if(exists(f_name+str(no)+".txt")):
        no=no+1
    else:
        break   
f_name=f_name+str(no)+".txt"
while(1):
    Village.render(f_name)
    
    input = input_to()
    Village.getinput(input)
    if(input=='q'):
        break
