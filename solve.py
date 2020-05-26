from game import HanoiTower


class SolveHanoiTower:

    def __init__(self, Game=HanoiTower(), inicialized=False):
        self.Game = Game
        self.higher = 0
        self.lower = 2
        if not inicialized:
            self.Game.inicialize_game()

    def higher_lower(self):
        if len(self.Game.rods[0]) > 0 and len(self.Game.rods[2]) > 0:
            self.lower, self.higher = (
                2, 0) if self.Game.rods[0][-1] > self.Game.rods[2][-1] else (0, 2)
        elif len(self.Game.rods[0]) > 0:
            self.lower, self.higher = (2, 0)
        elif len(self.Game.rods[2]) > 0:
            self.lower, self.higher = (0, 2)

    def clear_midrow(self):
        for _ in range(len(self.Game.rods[1])):
            self.Game.change(1, 0)

    def higher_to_midrow(self):
        if len(self.Game.rods[1]) > 0:
            if self.Game.rods[1][-1] < self.Game.rods[self.higher][-1]:
                self.Game.change(1, self.lower)
                self.higher_to_midrow()
                self.Game.change(self.lower, 1)
            else:
                self.Game.change(self.higher, 1)
        else:
            self.Game.change(self.higher, 1)

    def solve(self):
        tries = 0
        self.clear_midrow()
        while not self.Game.check_win():
            self.higher_lower()
            self.higher_to_midrow()
            if tries > 2*self.Game.number_disks:
                break
            tries += 1


if __name__ == '__main__':
    Game = HanoiTower()
    Solve = SolveHanoiTower(Game)
    Solve.solve()
    print(str(Game))
    print(Game.check_win())
    print(Game.number_disks, Game.moves)
