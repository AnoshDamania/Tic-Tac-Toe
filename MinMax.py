import pygame as pg

possible_moves = []


def ifwin(b):
    if b[0][0] == 1 and b[0][1] == 1 and b[0][2] == 1:
        return 0
    elif b[1][0] == 1 and b[1][1] == 1 and b[1][2] == 1:
        return 0
    elif b[2][0] == 1 and b[2][1] == 1 and b[2][2] == 1:
        return 0
    elif b[0][0] == 1 and b[1][0] == 1 and b[2][0] == 1:
        return 0
    elif b[0][1] == 1 and b[1][1] == 1 and b[2][1] == 1:
        return 0
    elif b[0][2] == 1 and b[1][2] == 1 and b[2][2] == 1:
        return 0
    elif b[0][0] == 1 and b[1][1] == 1 and b[2][2] == 1:
        return 0

    elif b[0][2] == 1 and b[1][1] == 1 and b[2][0] == 1:
        return 0

    elif b[0][0] == 2 and b[0][1] == 2 and b[0][2] == 2:
        return 1
    elif b[1][0] == 2 and b[1][1] == 2 and b[1][2] == 2:
        return 1
    elif b[2][0] == 2 and b[2][1] == 2 and b[2][2] == 2:
        return 1
    elif b[0][0] == 2 and b[1][0] == 2 and b[2][0] == 2:
        return 1
    elif b[0][1] == 2 and b[1][1] == 2 and b[2][1] == 2:
        return 1
    elif b[0][2] == 2 and b[1][2] == 2 and b[2][2] == 2:
        return 1
    elif b[0][0] == 2 and b[1][1] == 2 and b[2][2] == 2:
        return 1
    elif b[0][2] == 2 and b[1][1] == 2 and b[2][0] == 2:
        return 1

    elif b[0][0] != 0 and b[0][1] != 0 and b[0][2] != 0 and b[1][0] != 0 and \
            b[1][1] != 0 and b[1][2] != 0 and b[2][0] != 0 and b[2][1] != 0 and \
            b[2][2] != 0:
        return 2

    return -1


def get_possible_moves(b):
    for i in range(3):
        for j in range(3):
            if b[i][j] == 0:
                return True
    return False


# function that takes in the boardstate and spits out the best possible move.
def MinMax(b, depth, ismax):
    game_score = ifwin(b)
    if game_score == 1:
        return 1
    elif game_score == 0:
        return 0

    elif game_score == 2:
        return 2

    if ismax:
        best = -20

        for i in range(3):
            for j in range(3):

                if b[i][j] == 0:
                    b[i][j] = 1

                    best = max(best, MinMax(b, depth + 1, not ismax))

                    b[i][j] = 0

        return best
    else:
        best = 1000

        for i in range(3):
            for j in range(3):

                if b[i][j] == 0:
                    b[i][j] = 2

                    best = min(best, MinMax(b, depth + 1, not ismax))

                    b[i][j] = 0
        return best


def get_best_move(b):
    bestval = -1000
    bestMove = (-1, -1)

    for i in range(3):
        for j in range(3):

            if b[i][j] == 0:

                b[i][j] = 1
                move = MinMax(b, 0, False)

                b[i][j] = 0

                if (move > bestval):
                    bestMove = (i, j)
                    bestval = move

    return bestMove


pg.init()
win = pg.display.set_mode((1920, 1080))
font = pg.font.SysFont("freesans", 100)
q1 = 0
q2 = 0
q3 = 0
q4 = 0
q5 = 0
q6 = 0
q7 = 0
q8 = 0
q9 = 0

boardstate = [[q1, q2, q3],
              [q4, q5, q6],
              [q7, q8, q9]]

red_count = 0
end = False
loss = False
who_won = 0

while not end:
    pg.time.delay(1)
    pg.mouse.set_visible(True)
    win.fill((20, 20, 20))
    mouse = pg.mouse.get_pos()

    if not loss:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                end = True

            if event.type == pg.MOUSEBUTTONDOWN:
                if q1 == 0:
                    if 10 <= mouse[0] <= 635 and 10 <= mouse[1] <= 360:
                        if red_count % 2 == 0:
                            q1 = 1
                        else:
                            q1 = 2
                        red_count += 1
                if q2 == 0:
                    if 645 <= mouse[0] <= 1270 and 10 <= mouse[1] <= 360:
                        if red_count % 2 == 0:
                            q2 = 1
                        else:
                            q2 = 2
                        red_count += 1
                if q3 == 0:
                    if 1285 <= mouse[0] <= 1910 and 10 <= mouse[1] <= 355:
                        if red_count % 2 == 0:
                            q3 = 1
                        else:
                            q3 = 2
                        red_count += 1
                if q4 == 0:
                    if 10 <= mouse[0] <= 635 and 365 <= mouse[1] <= 720:
                        if red_count % 2 == 0:
                            q4 = 1
                        else:
                            q4 = 2
                        red_count += 1
                if q5 == 0:
                    if 645 <= mouse[0] <= 1270 and 365 <= mouse[1] <= 720:
                        if red_count % 2 == 0:
                            q5 = 1
                        else:
                            q5 = 2
                        red_count += 1
                if q6 == 0:
                    if 1285 <= mouse[0] <= 1910 and 365 <= mouse[1] <= 720:
                        if red_count % 2 == 0:
                            q6 = 1
                        else:
                            q6 = 2
                        red_count += 1
                if q7 == 0:
                    if 10 <= mouse[0] <= 635 and 725 <= mouse[1] <= 1070:
                        if red_count % 2 == 0:
                            q7 = 1
                        else:
                            q7 = 2
                        red_count += 1
                if q8 == 0:
                    if 645 <= mouse[0] <= 1270 and 725 <= mouse[1] <= 1070:
                        if red_count % 2 == 0:
                            q8 = 1
                        else:
                            q8 = 2
                        red_count += 1
                if q9 == 0:
                    if 1285 <= mouse[0] <= 1910 and 725 <= mouse[1] <= 1070:
                        if red_count % 2 == 0:
                            q9 = 1
                        else:
                            q9 = 2
                        red_count += 1
        boardstate = [[q1, q2, q3],
                      [q4, q5, q6],
                      [q7, q8, q9]]

        if red_count % 2 != 0:
            temp = get_best_move(boardstate)
            if temp == (0, 0):
                q1 = 2
            elif temp == (0, 1):
                q2 = 2
            elif temp == (0, 2):
                q3 = 2
            elif temp == (1, 0):
                q4 = 2
            elif temp == (1, 1):
                q5 = 2
            elif temp == (1, 2):
                q6 = 2
            elif temp == (2, 0):
                q7 = 2
            elif temp == (2, 1):
                q8 = 2
            elif temp == (2, 2):
                q9 = 2
            red_count += 1

        pg.draw.rect(win, (255, 255, 255), (0, 0, 10, 1080))
        pg.draw.rect(win, (255, 255, 255), (1910, 0, 10, 1080))
        pg.draw.rect(win, (255, 255, 255), (0, 0, 1920, 10))
        pg.draw.rect(win, (255, 255, 255), (0, 1070, 1920, 10))
        pg.draw.rect(win, (255, 255, 255), (635, 0, 10, 1080))
        pg.draw.rect(win, (255, 255, 255), (1275, 0, 10, 1080))
        pg.draw.rect(win, (255, 255, 255), (0, 355, 1920, 10))
        pg.draw.rect(win, (255, 255, 255), (0, 715, 1920, 10))

        if q1 == 1:
            pg.draw.circle(win, (255, 0, 0), (322.5, 185), 100)
            pg.draw.circle(win, (20, 20, 20), (322.5, 185), 50)
        if q2 == 1:
            pg.draw.circle(win, (255, 0, 0), (960, 185), 100)
            pg.draw.circle(win, (20, 20, 20), (960, 185), 50)
        if q3 == 1:
            pg.draw.circle(win, (255, 0, 0), (1602.5, 185), 100)
            pg.draw.circle(win, (20, 20, 20), (1602.5, 185), 50)
        if q4 == 1:
            pg.draw.circle(win, (255, 0, 0), (322.5, 540), 100)
            pg.draw.circle(win, (20, 20, 20), (322.5, 540), 50)
        if q5 == 1:
            pg.draw.circle(win, (255, 0, 0), (960, 540), 100)
            pg.draw.circle(win, (20, 20, 20), (960, 540), 50)
        if q6 == 1:
            pg.draw.circle(win, (255, 0, 0), (1602.5, 540), 100)
            pg.draw.circle(win, (20, 20, 20), (1602.5, 540), 50)
        if q7 == 1:
            pg.draw.circle(win, (255, 0, 0), (322.5, 897.5), 100)
            pg.draw.circle(win, (20, 20, 20), (322.5, 897.5), 50)
        if q8 == 1:
            pg.draw.circle(win, (255, 0, 0), (960, 897.5), 100)
            pg.draw.circle(win, (20, 20, 20), (960, 897.5), 50)
        if q9 == 1:
            pg.draw.circle(win, (255, 0, 0), (1602.5, 897.5), 100)
            pg.draw.circle(win, (20, 20, 20), (1602.5, 897.5), 50)

        if q1 == 2:
            pg.draw.circle(win, (0, 0, 255), (322.5, 185), 100)
            pg.draw.circle(win, (20, 20, 20), (322.5, 185), 50)
        if q2 == 2:
            pg.draw.circle(win, (0, 0, 255), (960, 185), 100)
            pg.draw.circle(win, (20, 20, 20), (960, 185), 50)
        if q3 == 2:
            pg.draw.circle(win, (0, 0, 255), (1602.5, 185), 100)
            pg.draw.circle(win, (20, 20, 20), (1602.5, 185), 50)
        if q4 == 2:
            pg.draw.circle(win, (0, 0, 255), (322.5, 540), 100)
            pg.draw.circle(win, (20, 20, 20), (322.5, 540), 50)
        if q5 == 2:
            pg.draw.circle(win, (0, 0, 255), (960, 540), 100)
            pg.draw.circle(win, (20, 20, 20), (960, 540), 50)
        if q6 == 2:
            pg.draw.circle(win, (0, 0, 255), (1602.5, 540), 100)
            pg.draw.circle(win, (20, 20, 20), (1602.5, 540), 50)
        if q7 == 2:
            pg.draw.circle(win, (0, 0, 255), (322.5, 897.5), 100)
            pg.draw.circle(win, (20, 20, 20), (322.5, 897.5), 50)
        if q8 == 2:
            pg.draw.circle(win, (0, 0, 255), (960, 897.5), 100)
            pg.draw.circle(win, (20, 20, 20), (960, 897.5), 50)
        if q9 == 2:
            pg.draw.circle(win, (0, 0, 255), (1602.5, 897.5), 100)
            pg.draw.circle(win, (20, 20, 20), (1602.5, 897.5), 50)

        if q1 == 1 and q2 == 1 and q3 == 1:
            loss = True
            who_won = 0
        elif q4 == 1 and q5 == 1 and q6 == 1:
            loss = True
            who_won = 0
        elif q7 == 1 and q8 == 1 and q9 == 1:
            loss = True
            who_won = 0
        elif q1 == 1 and q4 == 1 and q7 == 1:
            loss = True
            who_won = 0
        elif q2 == 1 and q5 == 1 and q8 == 1:
            loss = True
            who_won = 0
        elif q3 == 1 and q6 == 1 and q9 == 1:
            loss = True
            who_won = 0
        elif q1 == 1 and q5 == 1 and q9 == 1:
            loss = True
            who_won = 0

        elif q1 == 2 and q2 == 2 and q3 == 2:
            loss = True
            who_won = 1
        elif q4 == 2 and q5 == 2 and q6 == 2:
            loss = True
            who_won = 1
        elif q7 == 2 and q8 == 2 and q9 == 2:
            loss = True
            who_won = 1
        elif q1 == 2 and q4 == 2 and q7 == 2:
            loss = True
            who_won = 1
        elif q2 == 2 and q5 == 2 and q8 == 2:
            loss = True
            who_won = 1
        elif q3 == 2 and q6 == 2 and q9 == 2:
            loss = True
            who_won = 1
        elif q1 == 2 and q5 == 2 and q9 == 2:
            loss = True
            who_won = 1
        elif q3 == 2 and q5 == 2 and q7 == 2:
            loss = True
            who_won = 1
        elif q3 == 1 and q5 == 1 and q7 == 1:
            loss = True
            who_won = 0

        elif q1 != 0 and q2 != 0 and q3 != 0 and q4 != 0 and q5 != 0 and q6 != 0 and q7 != 0 and q8 != 0 and q9 != 0:
            who_won = 2
            loss = True

    else:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                end = True
            if event.type == pg.MOUSEBUTTONDOWN:
                if 384 <= mouse[0] <= 684 and 720 <= mouse[1] <= 820:
                    end = True
                if 1152 <= mouse[0] <= 1752 and 720 <= mouse[1] <= 820:
                    loss = False
                    q1 = 0
                    q2 = 0
                    q3 = 0
                    q4 = 0
                    q5 = 0
                    q6 = 0
                    q7 = 0
                    q8 = 0
                    q9 = 0

        label = font.render("GAME OVER!!", True, (255, 255, 255))
        win.blit(label, (100, 100))
        if who_won == 1:
            label = font.render("BLUE WON !!", True, (0, 80, 200))

        if who_won == 0:
            label = font.render("RED WON !!", True, (200, 0, 0))

        if who_won == 2:
            label = font.render("DRAW !!", True, (150, 150, 150))

        win.blit(label, (1000, 200))

        pg.draw.rect(win, (255, 255, 255), (0, 0, 10, 1080))
        pg.draw.rect(win, (255, 255, 255), (1910, 0, 10, 1080))
        pg.draw.rect(win, (255, 255, 255), (0, 0, 1920, 10))
        pg.draw.rect(win, (255, 255, 255), (0, 1070, 1920, 10))

        pg.draw.rect(win, (255, 255, 102), (384, 720, 300, 100))
        label = font.render("QUIT", True, (0, 0, 0))
        win.blit(label, (434, 710))

        pg.draw.rect(win, (51, 255, 255), (1152, 720, 600, 100))
        label = font.render("PLAY AGAIN", True, (0, 0, 0))
        win.blit(label, (1212, 710))

        mouse = pg.mouse.get_pos()

    pg.display.update()
