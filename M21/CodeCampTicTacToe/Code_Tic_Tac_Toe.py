import math
def check_horizontal(game, n):
    winner = ""
    for line in game:
        if n == line.count(line[0]):
            winner = line[0]
    if winner == ".":
        return None
    return winner

def check_vertical(game, n):
    winner = ""
    for i in range(n):
        lst = [line[i] for line in game]
        if n == lst.count(lst[0]):
            winner = lst[0]
            break
    if winner == ".":
        return None
    return winner

def check_diagonal(game, n, direction):
    winner = ""
    lst = [v[abs(direction -i)] for i, v in enumerate(game)]
    if n == lst.count(lst[0]):
        winner = lst[0]
    if winner == ".":
        return None
    return winner

def get_winner(game, n):
    x = check_horizontal(game, n)
    if x != "":
        return x
    x = check_vertical(game, n)
    if x != "":
        return x
    x = check_diagonal(game, n, 0)
    if x != "":
        return x
    x = check_diagonal(game, n, n-1)
    if x != "":
        return x
    return "draw"

def count_marks(game, n):
    x_cnt = 0
    o_cnt = 0
    for line in game:
        x_cnt += line.count('x')
        o_cnt += line.count('o')
    return x_cnt, o_cnt

def is_valid_game(game, n):
    counts = count_marks(game, n)
    print(counts)
    if abs(counts[0] - counts[1]) == 1:
        return True
    return False
    

def is_valid_input(game, n):
    for i in range(n):
        for j in game[i]:
            if j not in ['x', 'o', '.']:
                return False
    return True

def read_input(n):
    game = []
    for _ in range(n):
        game.append([j for j in input().split(" ")])
    return game

def main():
    n = 3
    game = read_input(n)
    if is_valid_input(game, n):
        valid_game = is_valid_game(game, n)
        # print(valid_game)
        winner = get_winner(game, n)
        print(winner)
    else:
        print("invalid game")


if __name__ == '__main__':
    main()
