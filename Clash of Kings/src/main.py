from colorama import Fore,Back, Style 
from os import system
from src.buildings import hut,Townhall,canon,building,wall,wizard
from src.troops import barbarians,archers,balloon
from src.king import King
from src.queen import Archer_queen
from time import time
from math import sqrt,floor


class village():
    def __init__(self):
        self.row = 100
        self.col = 175
        self.town = Townhall(50,50,4,3,300)
        self.walls = [wall(49,50,1,1,100),wall(49,51,1,1,100),wall(49,52,1,1,100),wall(49,53,1,1,100),wall(49,54,1,1,100),wall(49,49,1,1,100),wall(50,49,1,1,100),wall(51,49,1,1,100),wall(52,49,1,1,100),wall(53,49,1,1,100),wall(53,54,1,1,100),wall(52,54,1,1,100),wall(50,54,1,1,100),wall(51,54,1,1,100),wall(53,50,1,1,100),wall(53,51,1,1,100),wall(53,52,1,1,100),wall(53,53,1,1,100)]
        self.huts =[hut(14,11,1,1,150),hut(69,69,1,1,150),hut(90,20,1,1,150),hut(80,50,1,1,150),hut(20,5,1,1,150)]
        self.canons = [canon(35,20,1,1,200),canon(70,17,1,1,200)]
        self.king = King(57,45,1,1)
        self.queen = Archer_queen(57,45,1,1)
        self.wizard = [wizard(70,5,1,1,160),wizard(5,70,1,1,160)]
        self.barbarians = []
        self.archers = []
        self.tpbool = 0
        self.balloons = []
        self.troops = []
        self.start=-0.6
        self.game_over=1
        self.c_time=0
        self.rtime=0
        self.flag_rage=0
        self.rinterval = 4
        self.bg_pixel = Back.BLACK+' '+Style.RESET_ALL
        
    
    def getinput(self,input):
        var=0
        troop = []
        buildings = []
        defensive = []
        ndefensive = []
        nwall = []
        ndefensive.append(self.town)
        nwall.append(self.town)
        buildings.append(self.town)
        if input=='0':
            self.leviathan_axe()
        if input=='h':
            self.king.health = 1.5*self.king.health
            for t in self.troops:
                t.health = 1.5*t.health
        if input=='r':
            self.rtime=time()
        
        if(time()-self.rtime<self.rinterval):
            
            self.flag_rage=1
            

        if(self.flag_rage==0):
            if self.king.flag==1:
                self.king.damage=40
            for t in troop:
                t.damage = 5
            if input=='w' and self.king.flag==1:
                self.king.moveup(self.matrix)
            if input=='s' and self.king.flag==1:
                self.king.movedown(self.matrix)
            if input=='d'and self.king.flag==1:
                self.king.moveright(self.matrix)
            if input=='a'and self.king.flag==1:
                self.king.moveleft(self.matrix)
            if input=='w' and self.queen.flag==1:
                self.queen.prevk='w'
                self.queen.moveup(self.matrix)
            if input=='s' and self.queen.flag==1:
                self.queen.movedown(self.matrix)
                self.queen.prevk='s'
            if input=='d'and self.queen.flag==1:
                self.queen.prevk='d'
                self.queen.moveright(self.matrix)
            if input=='a'and self.queen.flag==1:
                self.queen.prevk='a'
                self.queen.moveleft(self.matrix)
        else:
            self.bg_pixel = Back.BLACK+' '+Style.RESET_ALL
            if input=='w' and self.king.flag==1:
                self.king.moveup(self.matrix)
                self.king.moveup(self.matrix)
            if input=='s' and self.king.flag==1:
                self.king.movedown(self.matrix)
                self.king.movedown(self.matrix)
            if input=='d' and self.king.flag==1:
                self.king.moveright(self.matrix)
                self.king.moveright(self.matrix)
            if input=='a' and self.king.flag==1:
                self.king.moveleft(self.matrix)
                self.king.moveleft(self.matrix)
        if input=='k' and self.king.flag==0:
            self.king = King(57,45,1,1)
            self.king.flag = 1
        if input =='e' and self.queen.flag==0:
            self.queen = Archer_queen(57,45,1,1)
            self.queen.flag = 1
        if input=='1':
            self.barbarians.append(barbarians(5,4,1,1,120,6))
        if input=='2':
            self.barbarians.append(barbarians(95,95,1,1,120,6))
        if input=='3':
            self.barbarians.append(barbarians(97,4,1,1,120,6))
        if input=='4':
            self.archers.append(archers(4,95,1,1,60,3))
        if input=='5':
            self.archers.append(archers(45,95,1,1,60,3))
        if input=='6':
            self.archers.append(archers(97,45,1,1,60,3))
        if input=='7':
            self.balloons.append(balloon(45,45,1,1,120,12))
        if input=='8':
            self.balloons.append(balloon(10,70,1,1,120,12))
        if input=='9':
            self.balloons.append(balloon(70,10,1,1,120,12))
        
        if(self.king.flag==1):
            troop.append(self.king)
        if(self.queen.flag==1):
            troop.append(self.queen)
        for w in self.walls:
            buildings.append(w)
        for h in self.huts:
            ndefensive.append(h)
            nwall.append(h)
            buildings.append(h)
        for c in self.canons:
            defensive.append(c)
            nwall.append(c)
            buildings.append(c)
        for b in self.barbarians:
            troop.append(b)
            self.troops.append(b)
        for a in self.archers:
            troop.append(a)
            self.troops.append(a)
        for b in self.balloons:
            troop.append(b)
            self.troops.append(b)
        for b in self.barbarians:
            b.movement(nwall,buildings,self.matrix)
        for a in self.archers:
            a.movement(nwall,buildings,self.matrix)
        tp = 1
        for b in self.balloons:
            b.movement(defensive,ndefensive,self.matrix)
        
        for w in self.wizard:
            defensive.append(w)
            buildings.append(w)
        for w in self.wizard:
            for t in troop:
                if(sqrt((t.x-w.x)**2+(t.y-w.y)**2)<=w.range):
                    for i in range(t.x-1,t.x+2):
                        for j in range(t.y-1,t.y+2):
                            for t in troop:
                                if(t.x==i and t.y==j):
                                    t.health = t.health - w.damage

         
        
        self.nw = nwall
        ## kING ATTACK
        if input==' ' and self.king.flag==1:
            flag = 0
            #walls attack
            if self.town.health > 0:
                for wa in self.walls:
                    if(wa.x==self.king.x and wa.y==self.king.y):
                        self.town.health = self.town.health - self.king.damage
                        flag=1

            
            if flag==0 or (self.town.health<=0):
                for w in self.walls:
                    if((w.x==self.king.x-1 and w.y==self.king.y) or (w.x-1==self.king.x and w.y==self.king.y) or (w.x==self.king.x and w.y-1==self.king.y) or (w.x==self.king.x and w.y==self.king.y-1) ):
                        w.health = w.health - self.king.damage
                        break
                
            
                
            for h in self.huts:
                if((h.x==self.king.x-1 and h.y==self.king.y) or (h.x-1==self.king.x and h.y==self.king.y) or (h.x==self.king.x and h.y-1==self.king.y) or (h.x==self.king.x and h.y==self.king.y-1)):
                    h.health = h.health - self.king.damage
                    flag = 1
                    break
                if((h.x==self.king.x-1 and h.y==self.king.y-1) or (h.x==self.king.x+1 and h.y==self.king.y-1) or (h.x==self.king.x-1 and h.y==self.king.y+1) or (h.x==self.king.x+1 and h.y==self.king.y+1)):
                    h.health = h.health - self.king.damage
                    flag=1
                    break

            for c in self.canons:
                if((c.x==self.king.x-1 and c.y==self.king.y) or (c.x-1==self.king.x and c.y==self.king.y) or (c.x==self.king.x and c.y-1==self.king.y) or (c.x==self.king.x and c.y==self.king.y-1)):
                    c.health = c.health - self.king.damage
                if((c.x==self.king.x-1 and c.y==self.king.y-1) or (c.x==self.king.x+1 and c.y==self.king.y-1) or (c.x==self.king.x-1 and c.y==self.king.y+1) or (c.x==self.king.x+1 and c.y==self.king.y+1)):
                    c.health = c.health - self.king.damage
        
        # QUEEN ATTACK

        if input==' ' and self.queen.flag==1:
            
            if self.queen.prevk == 'w' :
                y=self.queen.y-10
                x=self.queen.x-2

            elif self.queen.prevk == 's':
                y=self.queen.y+6
                x=self.queen.x-2

            elif self.queen.prevk == 'a':
                y=self.queen.y-2
                x=self.queen.x-10

            elif self.queen.prevk == 'd':
                y=self.queen.y - 2
                x=self.queen.x+6

            for i in range(x,x+5):
                for j in range(y,y+5):
                    for b in buildings:
                        if(b.x==i and b.y==j):
                            b.health=b.health-self.queen.damage
            te = 0
            for i in range(self.town.x,self.town.x+self.town.width):
                for j in range(self.town.y,self.town.y+self.town.height):
                    for k in range(x,x+5):
                        for l in range(y,y+5):
                            if(i==k and j==l):
                                te = 1
            if te==1:
                self.town.health = self.town.health - self.queen.damage       
            
        prev_key='w'   
        
        if input=='l' and self.queen.flag==1:
            
            prev_key = self.queen.prevk
            self.c_time = time()
            self.tpbool = 1
       
        if(time()-self.c_time>=1 and self.tpbool==1):
            f = open("demofile7.txt", "a+")
            f.write(str(self.queen.prevk)+"\n")
            f.close()
            
            if self.queen.prevk == 'w' :
                y=self.queen.y-20
                x=self.queen.x-4

            elif self.queen.prevk == 's':
                y=self.queen.y+12
                x=self.queen.x-4

            elif self.queen.prevk == 'a':
                y=self.queen.y-4
                x=self.queen.x-20

            elif self.queen.prevk == 'd':
                y=self.queen.y - 4
                x=self.queen.x+12
            
            for i in range(x,x+9):
                for j in range(y,y+9):
                    for b in buildings:
                        
                        if(b.x==i and b.y==j):
                            
                             
                            b.health=b.health-self.queen.damage
                            
                            self.tpbool=0
            te = 0
            for i in range(self.town.x,self.town.x+self.town.width):
                for j in range(self.town.y,self.town.y+self.town.height):
                    for k in range(x,x+9):
                        for l in range(y,y+9):
                            if(i==k and j==l):
                                te = 1
            if te==1:
                self.town.health = self.town.health - self.queen.damage
                self.tpbool=0

       
       
    
    def leviathan_axe(self):
        for h in self.huts:
            if(sqrt((h.x-self.king.x)**2+(h.y-self.king.y)**2)<=4):
                h.health = h.health - self.king.damage

        for c in self.canons:
            if(sqrt((c.x-self.king.x)**2+(c.y-self.king.y)**2)<=4):
                c.health = c.health - self.king.damage
        
        for w in self.walls:
            if(sqrt((w.x-self.king.x)**2+(w.y-self.king.y)**2)<=4):
                w.health = w.health - self.king.damage
        
        for i in range(self.town.y, self.town.y+self.town.height):
            for j in range(self.town.x, self.town.x+self.town.width):
                if(sqrt((i-self.king.y)**2+(j-self.king.x)**2)<=4):
                    self.town.health = self.town.health - self.king.damage
        
    def game_status(self):
        self.victory=1
        self.defeat=1
        if(self.town.health>0):
            self.victory=0
        for h in self.huts:
            if(h.health>0):
                self.victory=0
                break
        for c in self.canons:
            if(c.health>0):
                self.victory=0
                break
        for w in self.wizard:
            if(w.health>0):
                self.victory=0
                break

        
        if(self.king.health>0 or self.queen.health>0):
            self.defeat=0
    
        for t in self.troops:
            if(t.health>0):
                self.defeat=0
                break
                        #self.victory=0

    def cannon_attack(self):
        for c in self.canons:
            if(self.king.flag==1 and sqrt((c.x-self.king.x)**2+(c.y-self.king.y)**2)<=c.range):
                self.king.health = self.king.health - c.damage
            if(self.queen.flag==1 and sqrt((c.x-self.queen.x)**2+(c.y-self.queen.y)**2)<=c.range):
                self.queen.health = self.queen.health - c.damage
            for t in self.barbarians:
                if(sqrt((c.x-t.x)**2+(c.y-t.y)**2)<=c.range):
                    t.health = t.health - c.damage
            for t in self.archers:
                if(sqrt((c.x-t.x)**2+(c.y-t.y)**2)<=c.range):
                    t.health = t.health - c.damage            

    def render(self,f_name):
        system('clear')

        self.game_status()
        if(time()-self.rtime<self.rinterval):
            
            self.bg_pixel = Back.LIGHTMAGENTA_EX+' '+Style.RESET_ALL
        else:
            self.bg_pixel = Back.BLACK+' '+Style.RESET_ALL
        self.matrix = [[self.bg_pixel for i in range(self.col)] for j in range(self.row)]
        
       
            
        if(time()-self.start>=0.6):
            self.cannon_attack()
            self.start = time()
        
    
        
        Healthbar_text = "Health bar".format(self.king.health)
        
        
        for i in range(100,140):
            for j in range(35,50):
                self.matrix[j][i]=Back.BLUE+' '+Style.RESET_ALL
        for j in range(0, len(Healthbar_text)):
            self.matrix[40][110+j] = Back.BLUE+Fore.RED+Healthbar_text[j]+Style.RESET_ALL
        for i in range(0,floor(self.king.health/25)):
            self.matrix[44][110+i] = Back.RED+' '+Style.RESET_ALL
        for i in range(0,floor(self.queen.health/20)):
            self.matrix[46][110+i] = Back.BLACK+' '+Style.RESET_ALL

        
        for p in self.huts:
            for i in range(p.y, p.y+p.height):
                for j in range(p.x, p.x+p.width):
                    if(p.health<=150 and p.health>75):
                        self.matrix[i][j] = p.pixel1
                    elif(p.health<=75 and p.health>30):
                        self.matrix[i][j] = p.pixel2
                    elif(p.health<=30 and p.health>0):
                        self.matrix[i][j] = p.pixel3

        for p in self.wizard:
            for i in range(p.y, p.y+p.height):
                for j in range(p.x, p.x+p.width):
                    if(p.health<=160 and p.health>75):
                        self.matrix[i][j] = p.pixel1
                    elif(p.health<=75 and p.health>30):
                        self.matrix[i][j] = p.pixel2
                    elif(p.health<=30 and p.health>0):
                        self.matrix[i][j] = p.pixel3
        
        for p in self.barbarians:
            for i in range(p.y, p.y+p.height):
                for j in range(p.x, p.x+p.width):
                    self.matrix[i][j] = p.pixel

        for p in self.archers:
            for i in range(p.y, p.y+p.height):
                for j in range(p.x, p.x+p.width):
                    self.matrix[i][j] = p.pixel

        for p in self.balloons:
            for i in range(p.y, p.y+p.height):
                for j in range(p.x, p.x+p.width):
                    self.matrix[i][j] = p.pixel

        for p in self.walls:
            for i in range(p.y, p.y+p.height):
                for j in range(p.x, p.x+p.width):
                    if(p.health<=100 and p.health>50):
                        self.matrix[i][j] = p.pixel1
                    elif(p.health<=50 and p.health>20):
                        self.matrix[i][j] = p.pixel2
                    elif(p.health<=20 and p.health>0):
                        self.matrix[i][j] = p.pixel3
                    

        for p in self.canons:
            for i in range(p.y, p.y+p.height):
                for j in range(p.x, p.x+p.width):
                    if(p.health<=200 and p.health>100):
                        self.matrix[i][j] = p.pixel1
                    elif(p.health<=100 and p.health>40):
                        self.matrix[i][j] = p.pixel2
                    elif(p.health<=40 and p.health>0):
                        self.matrix[i][j] = p.pixel3


        for i in range(self.town.y, self.town.y+self.town.height):
            for j in range(self.town.x, self.town.x+self.town.width):
                if(self.town.health<=300 and self.town.health>150):
                    self.matrix[i][j] = self.town.pixel1
                elif(self.town.health<=150 and self.town.health>60):
                    self.matrix[i][j] = self.town.pixel2
                elif(self.town.health<=60 and self.town.health>0):
                    self.matrix[i][j] = self.town.pixel3
        if self.king.flag==1:
            for i in range(self.king.y, self.king.y+self.king.height):
                for j in range(self.king.x, self.king.x+self.king.width):
                    if(self.king.health>0):
                        self.matrix[i][j] = self.king.pixel

        if self.queen.flag==1:
            for i in range(self.queen.y, self.queen.y+self.queen.height):
                for j in range(self.queen.x, self.queen.x+self.queen.width):
                    if(self.queen.health>0):
                        self.matrix[i][j] = self.queen.pixel

        if self.victory == 1 or self.defeat==1:
            game_over_screen_height = 7
            game_over_screen_width = self.col//2
            self.matrix = [[Back.BLUE+' '+Style.RESET_ALL for i in range(game_over_screen_width)] for j in range(game_over_screen_height)]
            
            if(self.victory==1):
                game_over = "Game Over! Victory xD"
            if(self.defeat==1):
                game_over = "Game Over! Defeat :("
            game_over_offset = (game_over_screen_width-len(game_over)) // 2
            for j in range(0, len(game_over)):
                self.matrix[1][game_over_offset+j] = Back.BLUE+Fore.BLACK+game_over[j]+Style.RESET_ALL

        #for hut in self.huts:
            #print(hut.health)
        #print(self.queen.flag)
        #print("\n".join(["".join(row) for row in self.screen]))
        f = open(f_name,"a")
        print("\n".join(["".join(row) for row in self.matrix]))
        #f.write("\n".join(["".join(row) for row in self.matrix]))
        #f.write("\n")
        f.close()

        if(self.victory==1 or self.defeat==1):
            exit()