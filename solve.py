from game import HanoiTower
from sys import setrecursionlimit


class SolveHanoiTower:

    def __init__(self, Game=HanoiTower(), inicialized=False):
        self.Game = Game
        self.higher = 0
        self.lower = 2
        self.order = [(0, 1), (0, 2), (1, 2)]
        self.actual_change = 0
        if not inicialized:
            self.Game.inicialize_game()

    def lower_higher(self):
        rod_1 = self.order[self.actual_change][0]
        rod_2 = self.order[self.actual_change][1]
        if len(self.Game.rods[rod_1]) > 0 and len(self.Game.rods[rod_2]) > 0:
            self.lower, self.higher = (
                rod_2, rod_1) if self.Game.rods[rod_2][-1] < self.Game.rods[rod_1][-1] else (rod_1, rod_2)
            if(self.Game.rods[self.higher][-1] < self.Game.rods[self.lower][-1]):
                return False
        elif len(self.Game.rods[rod_1]) > 0:
            self.lower, self.higher = (rod_1, rod_2)
        elif len(self.Game.rods[rod_2]) > 0:
            self.lower, self.higher = (rod_2, rod_1)
        return True

    def recursion_solve(self):
        if not (Game.check_win() or Game.moves == (2 ** Game.number_disks) - 1):
            self.lower_higher()
            Game.change(self.lower, self.higher)
            self.actual_change = 0 if self.actual_change >= 2 else self.actual_change + 1
            self.recursion_solve()

    def non_recursion_solve(self):
        while not(self.Game.check_win() or self.Game.moves > (2 ** self.Game.number_disks)):
            self.lower_higher()
            self.Game.change(self.lower, self.higher)
            self.actual_change = 0 if self.actual_change >= 2 else self.actual_change + 1


if __name__ == '__main__':
    Game = HanoiTower(14)
    setrecursionlimit(2*(2**Game.number_disks))
    Solve = SolveHanoiTower(Game)
    print(str(Game))
    Solve.recursion_solve()
    print('End')
    print(str(Game))
    print(Game.check_win())
    print(Game.number_disks, Game.moves)

    Game = HanoiTower(20)
    Solve = SolveHanoiTower(Game)
    print(str(Game))
    Solve.non_recursion_solve()
    print('End')
    print(str(Game))
    print(Game.check_win())
    print(Game.number_disks, Game.moves)
