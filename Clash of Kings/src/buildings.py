from colorama import Back, Style

class building():
    def __init__(self,x,y,height,width,health):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.health = health
        
    
class hut(building):
    def __init__(self,x,y,height,width,health):
        self.pixel1 =  Back.WHITE+' '+Style.RESET_ALL
        #self.pixel2 =  Back.CYAN+' '+Style.RESET_ALL
        self.pixel2 =  Back.LIGHTWHITE_EX+' '+Style.RESET_ALL
        self.pixel3 =  Back.LIGHTRED_EX+' '+Style.RESET_ALL

        building.__init__(self,x,y,height,width,health)

class wall(building):
    def __init__(self,x,y,height,width,health):
        self.pixel1 =  Back.RED+' '+Style.RESET_ALL
        self.pixel2 =  Back.LIGHTBLUE_EX+' '+Style.RESET_ALL
        self.pixel3 =  Back.LIGHTYELLOW_EX+' '+Style.RESET_ALL
        building.__init__(self,x,y,height,width,health)

class Townhall(building):
    def __init__(self,x,y,height,width,health):
        self.pixel1 =  Back.CYAN+' '+Style.RESET_ALL
        self.pixel2 =  Back.GREEN+' '+Style.RESET_ALL
        self.pixel3 =  Back.YELLOW+' '+Style.RESET_ALL
        building.__init__(self,x,y,height,width,health)


class canon(building):
    def __init__(self,x,y,height,width,health):
        self.range = 6
        self.damage = 20
        self.pixel1 =  Back.YELLOW+' '+Style.RESET_ALL
        self.pixel2 =  Back.LIGHTGREEN_EX+' '+Style.RESET_ALL
        self.pixel3 =  Back.LIGHTCYAN_EX+' '+Style.RESET_ALL
        building.__init__(self,x,y,height,width,health)

class wizard(building):
    def __init__(self,x,y,height,width,health):
        self.range = 6
        self.damage = 20
        self.pixel1 =  Back.LIGHTGREEN_EX+' '+Style.RESET_ALL
        self.pixel2 =  Back.LIGHTYELLOW_EX+' '+Style.RESET_ALL
        self.pixel3 =  Back.LIGHTCYAN_EX+' '+Style.RESET_ALL
        building.__init__(self,x,y,height,width,health)
