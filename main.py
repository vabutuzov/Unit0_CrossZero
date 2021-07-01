#   Отрисовка игрового поля
def print_board():
    for S in playboard:
        print(*S)
    return


#   Ход игрока. Ввод координат ячейки, проверка ввода и измениние клетки на поле
def make_turn():
    if player:
        marker = "0"
    else:
        marker = "X"
    while True:
        turn_str = input("Ход игрока " + marker + ": ").split()

        if len(turn_str) == 2 and turn_str[0] in ["1", "2", "3"] and turn_str[1] in ["1", "2", "3"]:
            x = int(turn_str[0])
            y = int(turn_str[1])
            if playboard[x][y] == "-":
                playboard[x][y] = marker
                print_board()
                return
            else:
                print("Клетка занята. Повторите.")
        else:
            print("Ошибка ввода. Повторите.")


def check_winner():
    #   Список значений по горизонталям
    h_list = []
    for s in playboard[1:]:
        h_list.append("".join(s[1:]))

    #   Список значений по вертикли
    v_list = []
    for y in range(1, 4):
        v_str = ""
        for x in range(1, 4):
            v_str = v_str + playboard[x][y]
        v_list.append(v_str)

    # Список значений по диагонали
    d1_str = ""
    d2_str = ""
    for i in range(1, 4):
        d1_str += playboard[i][i]
        d2_str += playboard[i][4 - i]
    d_list = [d1_str, d2_str]

    # Список значений комбинаций клеток для проверки на наличие победителя
    all_list = []
    all_list.extend(h_list)
    all_list.extend(v_list)
    all_list.extend(d_list)

    #   Проверка выйгрышной последовательности
    if "XXX" in all_list:
        print("Победа игрока X")
        return True
    elif "000" in all_list:
        print("Победа игрока 0")
        return True

    #   Проверка заполенения доски
    board_full = True
    for s in playboard[1:]:
        if "-" in s:
            board_full = False
    if board_full:
        print("Ничья")
        return True

    return False


#   Начальное состояние игрового поля
playboard = [
    [" ", "1", "2", "3"],
    ["1", "-", "-", "-"],
    ["2", "-", "-", "-"],
    ["3", "-", "-", "-"]]

player = False  # Текущий игок, False - крестик, True - нолик
gameover = False

print('Игра "Крестики-нолики"')
print("Вводите через пробел номер клетки по горизонтали и по вертикали")
print_board()

while not gameover:
    make_turn()
    player = not player
    gameover = check_winner()
