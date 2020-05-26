from random import randint, sample


class HanoiTower:

    def __init__(self, number_disks=randint(3, 15)):
        self.rods = list()
        self.number_disks = number_disks
        self.moves = 0

    def inicialize_game(self):
        disks = range(self.number_disks)
        disks = sample(disks, len(disks))

        first_patition = [None, randint(0, len(disks))]
        self.rods.append(disks[:first_patition[1]])

        second_partition = [len(self.rods[0]), randint(0, len(disks) - len(self.rods[0]))]
        self.rods.append(disks[second_partition[0]:sum(second_partition)])

        third_partition = [len(self.rods[0])+len(self.rods[1]), None]
        self.rods.append(disks[third_partition[0]:])

    def change(self, rod_from, rod_to):
        try:
            number = self.rods[rod_from][-1]
            self.rods[rod_to].append(number)
            self.rods[rod_from].pop()
            self.moves += 1
        except IndexError as err:
            try:
                self.rods[rod_from]
                self.rods[rod_to]
            except IndexError:
                raise IndexError('rod does not exist')
            try:
                self.rods[rod_from][-1]
            except IndexError:
                raise IndexError('rod is empty')
            raise err

    def check_rod(self, rod):
        correct = list(range(self.number_disks-1, -1, -1))
        if self.rods[rod] == correct:
            return True
        return False

    def check_win(self):
        state = self.check_rod(0) or self.check_rod(1) or self.check_rod(2)
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
