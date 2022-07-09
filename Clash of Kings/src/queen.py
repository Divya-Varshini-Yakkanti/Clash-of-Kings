from colorama import Back, Style
from src.buildings import hut,Townhall,canon,building,wall

class Archer_queen():
    def __init__(self,x,y,height,width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.damage = 30
        self.health = 210
        self.flag = 0
        self.prevk = 'w'
        self.pixel =  Back.GREEN+' '+Style.RESET_ALL
        self.speed = 1

    

    def moveup(self,matrix):
        if(self.y-1>0 and (matrix[self.y-1][self.x] == Back.BLACK+' '+Style.RESET_ALL or matrix[self.y-1][self.x] == Back.LIGHTMAGENTA_EX+' '+Style.RESET_ALL) ):
            self.y = self.y-1
        self.prevk = 'w'
    def movedown(self,matrix):
        if(self.y+1<100 and (matrix[self.y+1][self.x] == Back.BLACK+' '+Style.RESET_ALL or matrix[self.y+1][self.x] == Back.LIGHTMAGENTA_EX+' '+Style.RESET_ALL)):
            self.y = self.y+1
        self.prevk = 's'
    def moveright(self,matrix):
        if(self.x+1<100 and (matrix[self.y][self.x+1] == Back.BLACK+' '+Style.RESET_ALL or matrix[self.y][self.x+1] == Back.LIGHTMAGENTA_EX+' '+Style.RESET_ALL)):
            self.x = self.x+1
        self.prevk = 'd'
    def moveleft(self,matrix):
        if(self.x-1>0 and (matrix[self.y][self.x-1] == Back.BLACK+' '+Style.RESET_ALL or matrix[self.y][self.x-1] == Back.LIGHTMAGENTA_EX+' '+Style.RESET_ALL)):
            self.x = self.x-1    
        self.prevk = 'a'
