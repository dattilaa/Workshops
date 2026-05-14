class NavalBattle:

    playing_field = [[0 for i in range(10)] for j in range(10)]

    def __init__(self, player_symbol: str):
        self.symbol = player_symbol
        self.hits = []


    def shot(self, x: int, y: int):
        if not (1 <= x <= 10 and 1 <= x <= 10):
            return 'Некорректные координаты'

        i, j = y - 1, x - 1
        cell = NavalBattle.playing_field[i][j]

        match cell:
            case 1:
                NavalBattle.playing_field[i][j] = self.symbol
                self.hits.append((x, y))
                return 'Попал'

            case 0:
                NavalBattle.playing_field[i][j] = 'o'
                return 'Мимо'


            case _:
                return 'ошибка'


    @staticmethod
    def show():
        print("   " + " ".join(f"{i:2}" for i in range(1, 11)))
        print("   " + "-" * 30)

        for i in range(10):
            row_display = []
            for j in range(10):
                cell = NavalBattle.playing_field[i][j]
                if cell == 0:
                    row_display.append(" ~")
                elif cell == "o":
                    row_display.append(" o")
                elif isinstance(cell, str):
                    row_display.append(f" {cell}")
                elif cell == 1:
                    row_display.append(" ~")
                else:
                    row_display.append(" ?")

            print(f"{i + 1:2} |" + "".join(row_display))

NavalBattle.playing_field = [[0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
[1, 1, 1, 0, 0, 1, 0, 0, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 1, 1, 0, 0, 1, 0, 0]]
player1 = NavalBattle('#')
player2 = NavalBattle('*')
NavalBattle.show()
player1.shot(6, 2)
player1.shot(6, 1)
player2.shot(6, 3)
player2.shot(6, 4)
player2.shot(6, 5)
player2.shot(3, 3)
player2.show()
player1.shot(1, 1)
NavalBattle.show()

