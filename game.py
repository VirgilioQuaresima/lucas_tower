class Game:

    Header = "\n\
******************\n\
** LUCA'S TOWER **\n\
******************\n\
          by Virgi"

    disks_number = 3

    def __init__(self) -> None:
        self.gameover = False
        self.columns = [[], [], []]
        self.moves = 0

    def define_columns(self, n):
        for j in range(3):
            if j == 0:
                for i in range(1, n+1):
                    self.columns[j].append(i)
            else:
                for i in range(1, n+1):
                    self.columns[j].append(0)

    def select_disks(self, start_col: int, end_col: int) -> None:
        lista = self.columns[start_col]
        start_disk = 0
        index_start_disk = 0
        for i, el in enumerate(lista):
            if el != 0:
                start_disk = el
                index_start_disk = i
                break

        lista = self.columns[end_col]
        base_disk = 0
        index_base_disk = 0

        for i, el in enumerate(lista):
            if el != 0:
                base_disk = el
                index_base_disk = i
                break

        if base_disk == 0 or base_disk > start_disk:

            self.columns[start_col][index_start_disk] = 0
            if index_base_disk == 0:
                self.columns[end_col][len(
                    self.columns[end_col])-1] = start_disk
            else:
                self.columns[end_col][index_base_disk-1] = start_disk

    def insert_column(self) -> tuple:
        start_col = int(input('insert start column: '))-1
        end_col = int(input('insert end column: '))-1

        if start_col < 0 or start_col > 2 or end_col < 0 or end_col > 2:
            return None, None

        if start_col == end_col:
            return None, None

        if self.columns[start_col][len(self.columns[end_col])-1] == 0:
            return None, None
        return start_col, end_col

    def check_gameover(self) -> None:
        big_boy = [i for i in range(1, len(self.columns[2])+1)]
        if self.columns[2] == big_boy or self.columns[1] == big_boy:
            self.gameover = True
            self.print_towers()
            print()
            print('***************')
            print('congratulations')
            print('***************')
            print()
            print(f'your number of moves: {self.moves+1}')
            print(f'minimal number of moves: {(2**self.disks_number)-1}')

    def print_towers(self):
        tower_1 = self.columns[0]
        tower_2 = self.columns[1]
        tower_3 = self.columns[2]
        triplets = [(tower_1[i], tower_2[i], tower_3[i])
                    for i in range(len(self.columns[0]))]
        print(f'moves: {self.moves}')
        print()
        for el in triplets:
            print(
                f"{el[0] if el[0] != 0 else '|'} {el[1] if el[1] != 0 else '|'} {el[2] if el[2] != 0 else '|'}")
        print()

    def select_difficoulty(self):
        dif = {'1': 3, '2': 4, '3': 5}
        diff_name = input('\n\
Select the difficoulty of the game:\n\
\nEasy: 1,\n\
Middle: 2,\n\
Hard: 3\n')
        return dif[diff_name]

    def run(self):
        print(self.Header)
        difficoulty = self.select_difficoulty()
        self.define_columns(difficoulty)
        
        while (self.gameover == False):
            print()
            self.print_towers()
            s, e = self.insert_column()
            if s != None:
                self.select_disks(s, e)
            self.check_gameover()
            self.moves += 1


if __name__ == '__main__':
    g = Game()
    g.run()
