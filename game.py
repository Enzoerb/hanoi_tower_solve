from random import randint, sample


class HanoiTower:

    def __init__(self, number_disks=randint(3, 15)):
        self.rods = [[], [], []]
        self.number_disks = number_disks
        self.moves = 0

    def inicialize_game(self):
        self.rods[0] = list(range(self.number_disks-1, -1, -1))
        self.rods[1] = []
        self.rods[2] = []

    def change(self, rod_from, rod_to):
        try:
            if len(self.rods[rod_to]) > 0:
                if(self.rods[rod_from][-1] > self.rods[rod_to][-1]):
                    return False
            number = self.rods[rod_from][-1]
            self.rods[rod_to].append(number)
            self.rods[rod_from].pop()
            self.moves += 1
            return True
        except IndexError:
            return False

    def check_rod(self, rod):
        correct = list(range(self.number_disks-1, -1, -1))
        if self.rods[rod] == correct:
            return True
        return False

    def check_win(self):
        state = self.check_rod(1) or self.check_rod(2)
        return state

    def __str__(self):
        string = ''

        def treat_number(lst, index):
            try:
                number = str(lst[index])
                return number + ' '*(len(str(self.number_disks))+3-len(number))
            except IndexError:
                return '|' + ' '*(len(str(self.number_disks))+2)

        for index in range(max([len(rod) for rod in self.rods])-1, -1, -1):
            for i in range(3):
                string += treat_number(self.rods[i], index)
            string += str('\n')

        return string


if __name__ == '__main__':
    Game = HanoiTower(15)
    Game.inicialize_game()
    print(str(Game))
    if len(Game.rods[0]) > 0:
        Game.change(0, 1)
    print(str(Game))
    print(Game.check_win())
    Game.rods[1] = list(range(Game.number_disks-1, -1, -1))
    print(Game.rods[1])
    print(Game.check_win())
