"""
Author: Christopher Eromosele Inegbedion
Project name: Tic-Tac-Toe
Project description: A game of tic-tac-toe that can be played between 2 people

"""
top_positions = ["-", "-", "-"]
middle_positions = ["-", "-", "-"]
bottom_positions = ["-", "-", "-"]

player_turn = "X"


def init():
    print("================")
    print("||Instructions||")
    print("================")
    print("To move a position, set the vertical position (from 1 to 3) and the horizontal position (from 1 to 3)\n")
    print("X starts the game")

    print("\n===================")
    print("   (1) | (2) | (3)")
    print("    ↓     ↓     ↓ ")
    print("||  {}  |  {}  |  {}   ← (1)".format(top_positions[0], top_positions[1], top_positions[2]))
    print("|| ----|-----|----- ")
    print("||  {}  |  {}  |  {}   ← (2)".format(middle_positions[0], middle_positions[1], middle_positions[2]))
    print("|| ----|-----|----- ")
    print("||  {}  |  {}  |  {}   ← (3)".format(bottom_positions[0], bottom_positions[1], bottom_positions[2]))
    print("===================")
    update_game()


def update_game():
    global player_turn
    if player_turn == "X":

        print("It's X's turn")
        v_move = input("Vertical position: ")
        h_move = input("Horizontal position: ")

        if move(int(v_move), int(h_move)):
            print("\nGame Over!")
            print("===============")
            print("||'X' has won||")
            print("===============")
            return True
        draw()
        player_turn = "O"
        update_game()

    else:
        print("It's O's turn")
        v_move = input("Vertical position: ")
        h_move = input("Horizontal position: ")

        if move(int(v_move), int(h_move)):
            print("\nGame Over!")
            print("===============")
            print("||'O' has won||")
            print("===============")
            return True
        draw()
        player_turn = "X"
        update_game()


def move(v_position, h_position):
    """
    This method moves an X or O item to the user's desired location if it is valid.

    :param v_position: This is the vertical position to be played at
    :param h_position: This is the horizontal position to be played at
    :return: Return true if the user has won, false if not
    """
    if is_move_valid(v_position, h_position):
        set_position(v_position, h_position)
        return has_player_won(v_position, h_position)
    else:
        print("\nThat move is not valid")
        update_game()


def set_position(v_position, h_position):
    """
    Set an X or O at the position selected

    :param v_position: This is the vertical position to be played at
    :param h_position: This is the horizontal position to be played at
    :return: None
    """
    if v_position == 1:
        top_positions[h_position-1] = player_turn
    if v_position == 2:
        middle_positions[h_position - 1] = player_turn
    if v_position == 3:
        bottom_positions[h_position - 1] = player_turn


def is_move_valid(v_position, h_position):
    """
    Validate whether or not a move is valid

    :param v_position: This is the vertical position to be played at
    :param h_position: This is the horizontal position to be played at
    :return: Return True if the move is valid, False it not
    """
    if v_position == 1:
        if 1 <= h_position <= 3:
            position = top_positions[h_position-1]
            if position == "-":
                return True
    if v_position == 2:
        if 1 <= h_position <= 3:
            position = middle_positions[h_position-1]
            if position == "-":
                return True
    if v_position == 3:
        if 1 <= h_position <= 3:
            position = bottom_positions[h_position-1]
            if position == "-":
                return True

    return False


def has_player_won(v_position, h_position):
    """
    Get all the neighbours at a position, and return True if there is a winning group

    :param v_position: This is the vertical position of the user
    :param h_position: This is the horizontal position of the user
    :return: Return True if one of the neighbouring groups results in a win, False if no winning group
    """
    all_neighbours = get_neighbours(v_position, h_position)
    # print(all_neighbours)
    for group in all_neighbours:
        if is_group_a_winner(group):
            return True

    return False


def get_neighbours(v_position, h_position):
    """
    Get all the neighbours at a position

    :param v_position: This is the vertical position being checked
    :param h_position:  This is the horizontal position being checked
    :return: Return all the neighbours
    """
    top_straight_lr = [top_positions[0], top_positions[1], top_positions[2]]
    middle_straight_lr = [middle_positions[0], middle_positions[1], middle_positions[2]]
    bottom_straight_lr = [bottom_positions[0], bottom_positions[1], bottom_positions[2]]

    top_bottom_diagonal = [top_positions[0], middle_positions[1], bottom_positions[2]]
    bottom_top_diagonal = [bottom_positions[0], middle_positions[1], top_positions[2]]

    top_start_bottom_up_down = [top_positions[0], middle_positions[0], bottom_positions[0]]
    top_middle_bottom_up_down = [top_positions[1], middle_positions[1], bottom_positions[1]]
    top_end_bottom_up_down = [top_positions[2], middle_positions[2], bottom_positions[2]]

    if v_position == 1:
        if h_position == 1:
            return [
                top_bottom_diagonal,
                top_straight_lr,
                top_start_bottom_up_down
            ]
        if h_position == 2:
            return [
                top_middle_bottom_up_down,
                top_straight_lr
            ]
        if h_position == 3:
            return [
                bottom_top_diagonal,
                top_straight_lr,
                top_end_bottom_up_down
            ]
    elif v_position == 2:
        if h_position == 1:
            return [
                middle_straight_lr,
                top_start_bottom_up_down
            ]
        if h_position == 2:
            return [
                bottom_top_diagonal,
                top_bottom_diagonal,
                top_middle_bottom_up_down,
                middle_straight_lr
            ]
        if h_position == 3:
            return [
                top_end_bottom_up_down,
                middle_straight_lr
            ]
    elif v_position == 3:
        if h_position == 1:
            return [
                top_start_bottom_up_down,
                bottom_straight_lr,
                bottom_top_diagonal
            ]
        if h_position == 2:
            return [
                top_middle_bottom_up_down,
                bottom_straight_lr
            ]
        if h_position == 3:
            return [
                top_end_bottom_up_down,
                bottom_straight_lr,
                top_bottom_diagonal
            ]


def is_group_a_winner(group):
    """
    Check if all the elements in the group are identical, return True if so, else False

    :param group: A list with a group of X's and O's
    :return: Return true if the group is a winner, False if not
    """
    start = ""
    for i in range(len(group)):
        if i == 0:
            if group[i] == "-":
                return False
            else:
                start = group[i]
        else:
            if group[i] == "-":
                return False
            else:
                if group[i] != start:
                    return False

    return True


def draw():
    """
    Draw the Tic-Tac-Toe board

    :return: None
    """
    print("\n=======================")
    print("||   {}  |  {}  |  {}   ||".format(top_positions[0], top_positions[1], top_positions[2]))
    print("|| -----|-----|----- ||")
    print("||   {}  |  {}  |  {}   ||".format(middle_positions[0], middle_positions[1], middle_positions[2]))
    print("|| -----|-----|----- ||")
    print("||   {}  |  {}  |  {}   ||".format(bottom_positions[0], bottom_positions[1], bottom_positions[2]))
    print("=======================")


init()
