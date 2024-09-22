import tkinter   # (GUI library).

#===============================================================================================================================

def set_title(row,column):
    global curr_player

    if(game_over):
        return

    if board[row][column]["text"] != "":
        return
    
    board[row][column]["text"] = curr_player  #mark board

    if(curr_player == playerO):
        curr_player = playerX
    else:
        curr_player = playerO

    lable["text"] = curr_player+"'s turn" 

    check_winner()

#===============================================================================================================================

def check_winner():
    global turns, game_over
    turns+=1   

    # Horizontal check
    for row in range(3):
        if(board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"] and board[row][0]["text"] != ""):
            lable.config(text=board[row][0]["text"]+" is the winner !", foreground="green")
            for column in range(3):
                board[row][column].config(background=grey, foreground="green")
            game_over = True
            return
        
    # Vertical check
    for column in range(3):
        if(board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"] and board[0][column]["text"] != ""):
            lable.config(text=board[0][column]["text"]+" is the winner !", foreground="green")
            for row in range(3):
                board[row][column].config(background=light_grey, foreground='green')
            game_over = True
            return

    # Diagionally    
    if(board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] and board[0][0]["text"] != ""):
            lable.config(text=board[0][0]["text"]+" is the winner !", foreground="green")
            for i in range(3):
                board[i][i].config(background=light_grey, foreground='green')
            game_over = True
            return

    # Anti-diagionally
    if(board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] and board[0][2]["text"] != ""):
        lable.config(text=board[0][2]["text"]+" is the winner !", foreground="green")
        board[0][2].config(foreground="green", background=light_grey)
        board[1][1].config(foreground="green", background=light_grey)
        board[2][0].config(foreground="green", background=light_grey)
        game_over = True
        return
    
    if(turns == 9):
        lable.config(text="~ TIE ! ~", foreground=yellow)
        game_over = True
        return
    
#===============================================================================================================================

def new_game():
    global turns, game_over

    turns = 0
    game_over = False

    lable.config(text=curr_player+"'s turn", foreground='white')

    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground=blue, background=black)

#===============================================================================================================================

def place():
    window.update()
    w_width=window.winfo_width()
    w_height=window.winfo_height()
    s_width=window.winfo_screenwidth()
    s_height=window.winfo_screenheight()

    window_x = int((s_width/2)-(w_width/2))
    window_y = int((s_height/2)-(w_height/2))

    window.geometry(f"{w_width}x{w_height}+{window_x}+{window_y}")

#===============================================================================================================================
# Player values

playerX = "X"
playerO = "O"
curr_player = playerX
turns = 0
game_over = False

#===============================================================================================================================
# 2D borrd.

board = [[0,0,0], 
         [0,0,0],
         [0,0,0]]

#===============================================================================================================================
# Colours !

blue        =   '#0000FF'
yellow      =   '#FFFF00'
grey        =   '#696969'
light_grey  =   '#A9A9A9'
white       =   '#FFFFFF'
light_green =   '#90EE90'
black       =   '#333333'

#===============================================================================================================================
# setup.

window = tkinter.Tk()  #Create the game window.
window.title("Tic Tac Toe")
window.resizable(False,False)

frame = tkinter.Frame(window)
lable = tkinter.Label(frame, text=curr_player+"'s Turn", font=("consolas",20),
                       background=light_grey, foreground=white)

lable.grid(row=0, column=0,columnspan=3, sticky="we") # we is west to east.

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text ="", font=("consolas", 50, "bold"),
                                            background=black, foreground=blue, width=4, height=1,
                                            command=lambda row=row, column=column: set_title(row, column))
        board[row][column].grid(row=row+1, column=column)

button = tkinter.Button(frame, text="restart", font=("consolas",20),background=light_grey,
                        foreground=white, command=new_game)
button.grid(row=4, column=0,columnspan=3,sticky="we")

frame.pack()
place()
window.mainloop()

#===============================================================================================================================

print("Exit sucessful")

#===============================================================================================================================