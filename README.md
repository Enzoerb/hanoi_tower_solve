# hanoi_tower_solve

## game.py
python script with HanoiTower class that initializes the game and has all it mechanisms

### HanoiTower

<hr/>

#### magic methods

<hr/>

##### \__init__
to initializew the function you can give the number of disks, otherwise it will be a random number from 3 to 15

HanoiTower class has 3 instance variables

<b>self.rods</b> := list with 3 lists inside it, where each one of the 3 lists are a rod of the game

<b>self.number_disks</b> := the number of disks in the game

<b>self.moves</b> := number of moves executed until the exact moment (starts as 0)

##### \__str__
returns the state of the Game

ex:

<pre>
>>> from game import HanoiTower
>>> Game = HanoiTower(10)
>>> Game.inicialize_game()
>>> print(str(Game))
0    |    |    
1    |    |    
2    |    |    
3    |    |    
4    |    |    
5    |    |    
6    |    |    
7    |    |    
8    |    |    
9    |    |  

>>> Game.change(0, 1)
>>> print(str(Game))
1    |    |    
2    |    |    
3    |    |    
4    |    |    
5    |    |    
6    |    |    
7    |    |    
8    |    |    
9    0    |  

</pre>
obs: each of the numbers are one disk(higher the number => higher the disk)

<hr/>

#### instance methods

<hr/>

##### initialize_game
initializes the game seting self.moves = 0, cleaning rods 1 and 2, and inserting all numbers in inverse order at rod 0

ex:

<pre>
>>> from game import HanoiTower
>>> Game = HanoiTower(10)
>>> Game.inicialize_game()
>>> Game.moves
0
>>> Game.rods
[[9, 8, 7, 6, 5, 4, 3, 2, 1, 0], [], []]
>>> Game.number_disks
10
</pre>

##### change
tranfer disk from first parameter to disk in second parameter

if disk does not exist or disk 1 > disk 2 returns False

ex:

<pre>
>>> from game import HanoiTower
>>> Game = HanoiTower(10)
>>> Game.inicialize_game()
>>> print(str(Game))
0    |    |    
1    |    |    
2    |    |    
3    |    |    
4    |    |    
5    |    |    
6    |    |    
7    |    |    
8    |    |    
9    |    |  

>>> Game.change(0, 1)
True
>>> Game.moves
1
>>> print(str(Game))
1    |    |    
2    |    |    
3    |    |    
4    |    |    
5    |    |    
6    |    |    
7    |    |    
8    |    |    
9    0    |  

>>> Game.change(0, 1)
False
>>> Game.moves
1
>>> print(str(Game))
1    |    |    
2    |    |    
3    |    |    
4    |    |    
5    |    |    
6    |    |    
7    |    |    
8    |    |    
9    0    |

</pre>

##### check_rod
checks if the order of a rod is right and with all disks in it

ex:

<pre>
>>> from game import HanoiTower
>>> Game = HanoiTower(10)
>>> Game.rods[0] = list(range(10))
>>> Game.check_rod(0)
False
>>> Game.rods[1] = list(range(9, -1, -1))
>>> Game.check_rod(1)
True
</pre>

##### check_win
check if you won the Game

win format 1:

<pre>
|    0    |    
|    1    |    
|    2    |    
|    3    |   
|    4    |    
|    5    |    
|    6    |    
|    7    |    
|    8    |    
|    9    |  
</pre>

win format 2:

<pre>
|    |    0   
|    |    1   
|    |    2   
|    |    3   
|    |    4   
|    |    5   
|    |    6   
|    |    7   
|    |    8   
|    |    9 
</pre>
