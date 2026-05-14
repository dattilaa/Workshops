import random


class NavalBattle:

    playing_field = None

    def __init__(self, player_symbol):
        self.player_symbol = player_symbol
        self.hits = []


    @classmethod
    def new_game(cls):
        cls.playing_field = [[0 for _ in range(10)] for _ in range(10)]

        ships = [(4, 1), (3, 2), (2, 3), (1, 4)]

        for ship_length, count in ships:
            for _ in range(count):
                placed = False
                attempts = 0
                while not placed and attempts < 1000:
                    orientation = random.choice([0, 1])

                    if orientation == 0:
                        x = random.randint(0, 9)
                        y = random.randint(0, 9 - ship_length + 1)
                    else:
                        x = random.randint(0, 9 - ship_length + 1)
                        y = random.randint(0, 9)

                    if cls._can_place_ship(x, y, ship_length, orientation):
                        cls._place_ship(x, y, ship_length, orientation)
                        placed = True

                    attempts += 1

                if not placed:
                    return cls.new_game()


    @classmethod
    def _can_place_ship(cls, x, y, length, orientation):
        start_x = max(0, x - 1)
        start_y = max(0, y - 1)

        if orientation == 0:
            end_x = min(9, x + 1)
            end_y = min(9, y + length)
        else:
            end_x = min(9, x + length)
            end_y = min(9, y + 1)

        for i in range(start_x, end_x + 1):
            for j in range(start_y, end_y + 1):
                if cls.playing_field[i][j] != 0:
                    return False

        if orientation == 0:
            for j in range(y, y + length):
                if cls.playing_field[x][j] != 0:
                    return False
        else:
            for i in range(x, x + length):
                if cls.playing_field[i][y] != 0:
                    return False

        return True

    @classmethod
    def _place_ship(cls, x, y, length, orientation):
        if orientation == 0:
            for j in range(y, y + length):
                cls.playing_field[x][j] = 1
        else:
            for i in range(x, x + length):
                cls.playing_field[i][y] = 1


    @staticmethod
    def show():
        if NavalBattle.playing_field is None:
            print('Игровое поле не создано. Используйте NavalBattle.new_game()')
            return

        print('   ' + ' '.join(f'{i:2}' for i in range(1, 11)))
        print('   ' + '-' * 30)

        for i in range(10):
            row_display = []
            for j in range(10):
                cell = NavalBattle.playing_field[i][j]
                if cell == 0:
                    row_display.append(' ~')
                elif cell == 'o':
                    row_display.append(' o')
                elif isinstance(cell, str):
                    row_display.append(f' {cell}')
                elif cell == 1:
                    row_display.append(' ~')
                else:
                    row_display.append(' ?')

            print(f'{i + 1:2} |' + ''.join(row_display))

    def shot(self, x, y):
        if NavalBattle.playing_field is None:
            print('игровое поле не заполнено')
            return 'игровое поле не заполнено'

        if not (1 <= x <= 10 and 1 <= y <= 10):
            print('ошибка: некорректные координаты')
            return 'ошибка'

        i, j = y - 1, x - 1

        cell = NavalBattle.playing_field[i][j]

        if cell == 'o' or isinstance(cell, str):
            print('ошибка')
            return 'ошибка'

        if cell == 1:
            NavalBattle.playing_field[i][j] = self.player_symbol
            self.hits.append((x, y))
            print('попал')

            if self._is_ship_destroyed(x, y):
                print('Корабль уничтожен!')

            return 'попал'
        elif cell == 0:
            NavalBattle.playing_field[i][j] = 'o'
            print('мимо')
            return 'мимо'
        else:
            return 'ошибка'

    def _is_ship_destroyed(self, x, y):
        i, j = y - 1, x - 1

        ship_cells = [(i, j)]

        for k in range(i - 1, -1, -1):
            if NavalBattle.playing_field[k][j] == self.player_symbol:
                ship_cells.append((k, j))
            elif NavalBattle.playing_field[k][j] == 1:
                ship_cells.append((k, j))
            else:
                break

        for k in range(i + 1, 10):
            if NavalBattle.playing_field[k][j] == self.player_symbol:
                ship_cells.append((k, j))
            elif NavalBattle.playing_field[k][j] == 1:
                ship_cells.append((k, j))
            else:
                break

        for k in range(j - 1, -1, -1):
            if NavalBattle.playing_field[i][k] == self.player_symbol:
                ship_cells.append((i, k))
            elif NavalBattle.playing_field[i][k] == 1:
                ship_cells.append((i, k))
            else:
                break

        for k in range(j + 1, 10):
            if NavalBattle.playing_field[i][k] == self.player_symbol:
                ship_cells.append((i, k))
            elif NavalBattle.playing_field[i][k] == 1:
                ship_cells.append((i, k))
            else:
                break

        for ci, cj in ship_cells:
            if NavalBattle.playing_field[ci][cj] == 1:
                return False

        return True