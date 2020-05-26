from random import randint
from game import HanoiTower

Game = HanoiTower()
Game.inicialize_game()

print(str(Game))
for _ in range(len(Game.rods[1])):
    Game.change(1, 0)
print(str(Game))

tries = 0
while not Game.check_win():

    if len(Game.rods[1]) == 0:
        if len(Game.rods[0]) > 0:
            if len(Game.rods[2]) > 0:
                if Game.rods[0][-1] > Game.rods[2][-1]:
                    Game.change(0, 1)
                else:
                    Game.change(2, 1)
            else:
                Game.change(0, 1)
        elif len(Game.rods[2]) > 0:
            Game.change(2, 1)
    else:
        if len(Game.rods[0]) > 0 and len(Game.rods[2]) > 0:
            if Game.rods[1][-1] > Game.rods[0][-1] and Game.rods[1][-1] > Game.rods[2][-1]:
                if Game.rods[0][-1] > Game.rods[2][-1]:
                    Game.change(0, 1)
                else:
                    Game.change(2, 1)
            else:
                if Game.rods[0][-1] > Game.rods[2][-1]:
                    centered_disks = len(Game.rods[1])
                    for _ in range(centered_disks):
                        Game.change(1, 2)
                    for actual_disk in range(centered_disks):
                        if Game.rods[0][-1] > Game.rods[2][-1]:
                            Game.change(0, 1)
                            for _ in range(centered_disks-actual_disk):
                                Game.change(2, 1)
                            break
                        else:
                            Game.change(2, 1)
                else:
                    centered_disks = len(Game.rods[1])
                    for _ in range(centered_disks):
                        Game.change(1, 0)
                    for actual_disk in range(centered_disks):
                        if Game.rods[2][-1] > Game.rods[0][-1]:
                            Game.change(2, 1)
                            for _ in range(centered_disks-actual_disk):
                                Game.change(0, 1)
                            break
                        else:
                            Game.change(0, 1)

        elif len(Game.rods[0]) > 0:
            if Game.rods[1][-1] > Game.rods[0][-1]:
                Game.change(0, 1)
            else:
                centered_disks = len(Game.rods[1])
                for _ in range(centered_disks):
                    Game.change(1, 2)
                for actual_disk in range(centered_disks):
                    if Game.rods[0][-1] > Game.rods[2][-1]:
                        Game.change(0, 1)
                        for _ in range(centered_disks-actual_disk):
                            Game.change(2, 1)
                        break
                    else:
                        Game.change(2, 1)

        elif len(Game.rods[2]) > 0:
            if Game.rods[1][-1] > Game.rods[2][-1]:
                Game.change(2, 1)
            else:
                centered_disks = len(Game.rods[1])
                for _ in range(centered_disks):
                    Game.change(1, 0)
                for actual_disk in range(centered_disks):
                    if Game.rods[2][-1] > Game.rods[0][-1]:
                        Game.change(2, 1)
                        for _ in range(centered_disks-actual_disk):
                            Game.change(0, 1)
                        break
                    else:
                        Game.change(0, 1)

        else:
            break

    print(str(Game))
    tries += 1
    print(tries)
    if tries > 2*Game.number_disks:
        break

print(Game.rods[1])
print(Game.check_win())
