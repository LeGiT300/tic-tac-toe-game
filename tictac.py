import tkinter as tk
import random


def next_turn(row, column):
    global player

    if buttons[row][column]['text'] == '' and check_winner() is False:

        if player == players[0]:
            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1] + " turn"))

            elif check_winner() is True:
                label.config(text=(players[0] + " wins"))

            elif check_winner() == 'Draw':
                label.config(text="Draw")

        else:
            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0] + " turn"))

            elif check_winner() is True:
                label.config(text=(players[1] + " wins"))

            elif check_winner() == 'Draw':
                label.config(text="Draw")


def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg='yellow')
            buttons[row][1].config(bg='yellow')
            buttons[row][2].config(bg='yellow')
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg='yellow')
            buttons[1][column].config(bg='yellow')
            buttons[2][column].config(bg='yellow')
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '':
        buttons[0][0].config(bg='yellow')
        buttons[1][1].config(bg='yellow')
        buttons[2][2].config(bg='yellow')
        return True

    elif buttons[0][1]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != '':
        buttons[0][2].config(bg='yellow')
        buttons[1][1].config(bg='yellow')
        buttons[2][0].config(bg='yellow')
        return True
    elif check_empty() is False:

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg='pink')
        return 'Draw'
    else:
        return False


def check_empty():
    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != '':
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True


def new_game():
    global player

    player = random.choice(players)

    label.config(text= player + " turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg='#F0F0F0')


window = tk.Tk()
window.title('Tic Tac Toe')
players = ['X', 'O']

player = random.choice(players)
buttons = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

label = tk.Label(text=player + ' turn', font=('consolas', 40))
label.pack(side='top')

reset_button = tk.Button(text='restart', font=('consolas', 15), command=new_game)
reset_button.pack(side='top')

frame = tk.Frame(window)
frame.pack()

for row in range(3):
    for columns in range(3):
        buttons[row][columns] = tk.Button(frame, text='', font=('consolas', 40), width=5, height=2,
                                          command=lambda row=row, column=columns: next_turn(row, column))

        buttons[row][columns].grid(row=row, column=columns)

window.mainloop()
