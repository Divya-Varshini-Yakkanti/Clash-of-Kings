from colorama import Back, Style
import math
from math import sqrt
class troop():
    def __init__(self,x,y,height,width,health,damage):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.health = health
        self.damage = damage
        self.speed = 1

class barbarians(troop):
    def __init__(self,x,y,height,width,health,damage):
        self.pixel = Back.LIGHTBLUE_EX+' '+Style.RESET_ALL
        self.speed_x = 1
        self.speed_y = 1
        troop.__init__(self,x,y,height,width,health,damage)

    def obstacle(self,buildings):
        if(self.health>0):
            for b in buildings:
                if b.health>0:
                    if(b.x==self.x and b.y==self.y):
                        b.health = b.health - self.damage
                        return 1
            return 0
        return 0


    def movement(self,nwall,buildings,matrix):
        
        if self.health>0:
            newx = 0
            newy = 0
            d = 2000
            for n in nwall:
                if n.health>0:
                    dis = abs(n.x-self.x)+abs(n.y-self.y)
                    if dis < d:
                        d = dis
                        newx = n.x
                        newy = n.y
            '''f = open("demofile2.txt", "a+")
            f.write(str(dis)+"\n")
            f.close()'''
            new_positionsy = []
            new_positionsx = []
            if newy > self.y:
                self.y = self.y + self.speed_y
                new_positionsy.append(self.y)
                if self.y > 99:
                    self.y = 99
                if self.obstacle(buildings) == 1:
                    self.y = self.y - self.speed_y
            elif newy < self.y:
                self.y = self.y - self.speed_y
                new_positionsy.append(self.y)
                if self.y < 0:
                    self.y = 0
                if self.obstacle(buildings) == 1:
                    self.y = self.y + self.speed_y
            if newx > self.x:
                self.x = self.x + self.speed_x
                new_positionsx.append(self.x)
                if self.x > 99:
                    self.x = 99
                if self.obstacle(buildings) == 1:
                    self.x = self.x - self.speed_x
            elif newx < self.x:
                self.x = self.x - self.speed_x
                new_positionsx.append(self.x)
                if self.x < 0:
                    self.x = 0
                if self.obstacle(buildings) == 1:
                    self.x = self.x + self.speed_x
            
class archers(troop):
    def __init__(self,x,y,height,width,health,damage):
        self.pixel = Back.LIGHTGREEN_EX+' '+Style.RESET_ALL
        self.speed_x = 2
        self.speed_y = 2
        self.range = 4
        troop.__init__(self,x,y,height,width,health,damage)

    def obstacle(self,buildings):
        if(self.health>0):
            for b in buildings:
                if b.health>0:
                    if((b.x-self.x)**2+(b.y-self.y)**2 <= self.range*self.range):
                        b.health = b.health - self.damage
                        return 1
            return 0
        return 0

    def movement(self,nwall,buildings,matrix):
        
        if self.health>0:
            newx = 0
            newy = 0
            d = 2000
            for n in nwall:
                if n.health>0:
                    dis = sqrt((n.x-self.x)**2+(n.y-self.y)**2)
                    if dis < d:
                        d = dis
                        newx = n.x
                        newy = n.y

            new_positionsy = []
            new_positionsx = []
            if newy > self.y:
                self.y = self.y + self.speed_y
                new_positionsy.append(self.y)
                if self.y > 99:
                    self.y = 99
                if self.obstacle(buildings) == 1:
                    self.y = self.y - self.speed_y
            elif newy < self.y:
                self.y = self.y - self.speed_y
                new_positionsy.append(self.y)
                if self.y < 0:
                    self.y = 0
                if self.obstacle(buildings) == 1:
                    self.y = self.y + self.speed_y
            if newx > self.x:
                self.x = self.x + self.speed_x
                new_positionsx.append(self.x)
                if self.x > 99:
                    self.x = 99
                if self.obstacle(buildings) == 1:
                    self.x = self.x - self.speed_x
            elif newx < self.x:
                self.x = self.x - self.speed_x
                new_positionsx.append(self.x)
                if self.x < 0:
                    self.x = 0
                if self.obstacle(buildings) == 1:
                    self.x = self.x + self.speed_x

'''class balloon(troop):
    def __init__(self,x,y,height,width,health,damage):
        self.pixel = Back.LIGHTCYAN_EX+' '+Style.RESET_ALL
        self.speed_x = 2
        self.speed_y = 2
        
        troop.__init__(self,x,y,height,width,health,damage)

    def obstacle(self,buildings):
        if(self.health>0):
            for b in buildings:
                if b.health>0:
                    if((b.x==self.x and b.y==self.y) or (b.x==self.x and b.y==self.y+1) or (b.x==self.x and b.y==self.y-1) or (b.x==self.x+1 and b.y==self.y) or (b.x==self.x-1 and b.y==self.y)):
                        b.health = b.health - self.damage
                        return 1
            return 0
        return 0

    def movement(self,nwall,buildings,matrix):
        
        if self.health>0:
            newx = 0
            newy = 0
            d = 2000
            for n in nwall:
                if n.health>0:
                    dis = sqrt((n.x-self.x)**2+(n.y-self.y)**2)
                    if dis < d:
                        d = dis
                        newx = n.x
                        newy = n.y

            new_positionsy = []
            new_positionsx = []
            if newy > self.y:
                self.y = self.y + self.speed_y
                new_positionsy.append(self.y)
                if self.y > 99:
                    self.y = 99
                a = self.obstacle(buildings)
            elif newy < self.y:
                self.y = self.y - self.speed_y
                new_positionsy.append(self.y)
                if self.y < 0:
                    self.y = 0
                a = self.obstacle(buildings)
            if newx > self.x:
                self.x = self.x + self.speed_x
                new_positionsx.append(self.x)
                if self.x > 99:
                    self.x = 99
                a = self.obstacle(buildings)
            elif newx < self.x:
                self.x = self.x - self.speed_x
                new_positionsx.append(self.x)
                if self.x < 0:
                    self.x = 0
                a = self.obstacle(buildings)
'''

class balloon(troop):
    def __init__(self,x,y,height,width,health,damage):
        self.pixel = Back.LIGHTCYAN_EX+' '+Style.RESET_ALL
        self.speed_x = 2
        self.speed_y = 2
        
        troop.__init__(self,x,y,height,width,health,damage)

    def obstacle(self,buildings):
        if(self.health>0):
            for b in buildings:
                if b.health>0:
                    if((b.x==self.x and b.y==self.y) or (b.x==self.x and b.y==self.y+1) or (b.x==self.x and b.y==self.y-1) or (b.x==self.x+1 and b.y==self.y) or (b.x==self.x-1 and b.y==self.y)):
                        b.health = b.health - self.damage
                        return 1
            return 0
        return 0

    def movement(self,defensive,ndefensive,matrix):
        
        if self.health>0:
            newx = 0
            newy = 0
            d = 2000
            for n in defensive:
                if n.health>0:
                    dis = sqrt((n.x-self.x)**2+(n.y-self.y)**2)
                    if dis < d:
                        d = dis
                        newx = n.x
                        newy = n.y

            new_positionsy = []
            new_positionsx = []
            if newy > self.y:
                self.y = self.y + self.speed_y
                new_positionsy.append(self.y)
                if self.y > 99:
                    self.y = 99
                a = self.obstacle(defensive)
            elif newy < self.y:
                self.y = self.y - self.speed_y
                new_positionsy.append(self.y)
                if self.y < 0:
                    self.y = 0
                a = self.obstacle(defensive)
            if newx > self.x:
                self.x = self.x + self.speed_x
                new_positionsx.append(self.x)
                if self.x > 99:
                    self.x = 99
                a = self.obstacle(defensive)
            elif newx < self.x:
                self.x = self.x - self.speed_x
                new_positionsx.append(self.x)
                if self.x < 0:
                    self.x = 0
                a = self.obstacle(defensive)

            tp = 1
            
            for c in defensive:
                if c.health>0:
                    tp = 0
                    break
            
            if tp==1:
                f = open("demofiless.txt", "a+")
                f.write(str(ndefensive)+"\n")
                f.close()
                newx = 0
                newy = 0
                d = 2000
                for n in ndefensive:
                    if n.health>0:
                        dis = sqrt((n.x-self.x)**2+(n.y-self.y)**2)
                        if dis < d:
                            d = dis
                            newx = n.x
                            newy = n.y

                new_positionsy = []
                new_positionsx = []
                if newy > self.y:
                    self.y = self.y + self.speed_y
                    new_positionsy.append(self.y)
                    if self.y > 99:
                        self.y = 99
                    a = self.obstacle(ndefensive)
                elif newy < self.y:
                    self.y = self.y - self.speed_y
                    new_positionsy.append(self.y)
                    if self.y < 0:
                        self.y = 0
                    a = self.obstacle(ndefensive)
                if newx > self.x:
                    self.x = self.x + self.speed_x
                    new_positionsx.append(self.x)
                    if self.x > 99:
                        self.x = 99
                    a = self.obstacle(ndefensive)
                elif newx < self.x:
                    self.x = self.x - self.speed_x
                    new_positionsx.append(self.x)
                    if self.x < 0:
                        self.x = 0
                    a = self.obstacle(ndefensive)

