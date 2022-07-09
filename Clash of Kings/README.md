This is a 2 D game in Python3 (terminal-based), heavily inspired by Clash of clans where the user will control the king, move it up, down, forward and backward, while destroying buildings and fighting defences on its way.
The objective of the game is to destroy as many buildings as possible
- Each game can end in either victory or defeat. Victory occurs when all the buildings are destroyed and defeat when troops are destroyed .

Implementation :
- The implementation of this game is done using a 100x175 matrix . The matrix is filled necessary colors using coloroma and required ASCII values . All cannons , huts , walls and the King are of size 1x1 . 
- The code is implemented using OOPS concepts like inheritance , Polymorphism , Encapsulation , Abstraction .

Spawning points - When keys 1 , 2 , 3 are pressed , barbarians are spawned at 3 differeent places .
Cannons :
They have a damage of 20 and attack the troops at range of 6
Every building has certain hitpoints like , 300 for townhall , 200 for cannons , 150 for huts and 100 for walls . 

King will attack a wall when in contact with it . The king's health is displayed using a health bar .

Spells :
Pressing r key invokes rage spell , which lasts for 4 seconds and the background color of the grid changes . 
Pressing h invokes heel spell .

Game ends once all the troops and King dies or when all the Buildings are destroyed .