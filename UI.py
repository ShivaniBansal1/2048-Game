from tkinter import Frame, Label, CENTER

from logicsGame import Logics
from constants import Constants as c

class Game2048(Frame):
    def __init__(self):

        #creates a frame/ initialises the frame
        Frame.__init__(self)

        #visualises frame as grid
        self.grid()

        #giving title to frame
        self.master.title("2048")

        #binding with event 'key press' just like event listner
        self.master.bind("<key>", self.key_down)

        #creating dictionary for commands
        self.commands = {c.key_up : Logics.move_up, c.key_down:Logics.move_down, c.key_left : Logics.move_left, c.key_right:Logics.move_right}
        
        #creating cells which are empty (actually it is matrix UI)
        self.grid_cells = []

        #intialising cells with 0 and assigning required colour and bg color
        self.init_grid()

        #starts the game and inserts random 2's
        self.init_matrix()

        #update cells according to numbers(0,2,4,8)
        self.update_grid_cells()

        #runs the actual program
        self.mainloop()

    def init_grid(self):
        background = Frame(self, bg=c.background_colour_game, width = c.size, height = c.size)
        background.grid()
        for i in range(c.grid_length):
            grid_row = []
            for j in range(c.grid_length):
                cell = Frame(background, bg=c.background_colour_cell_empty, width = c.size/c.grid_length, height = c.size/c.grid_length)
                cell.grid(row=i, column=j, padx=c.grid_padding, pady = c.grid_padding)
                t = Label(master = cell, text="", bg=c.background_colour_cell_empty, justify = CENTER, font = c.FONT, width=5, height=2)

                t.grid()
                grid_row.append(t)

            self.grid_cells.append(grid_row)

    # def init_matrix(Self):
    #     for i in range(c.grid_length):
    #         for j in range(c.grid_length):
    #             new_number = self.matrix[i][j]
    #             if new_number == 0:
    #                 self.grid_cells[i][j].configure(
    #                     text="", bg=c.background_colour_cell_empty
    #                 )
    #             else:
    #                 self.grid_cells[i][j].configure(text=str(
    #                     new_number
    #                 ), )

    #initialises a matrix with 2's at two positions(here we are maintianing our own matrix)
    def init_matrix(self):

        #here self.matrix is our own Matrix(logical)
        self.matrix = Logics.start_game()
        Logics.insert_random_2(self.matrix)

    #this function reflects the own created matrix in the UI
    def update_grid_cells(self):
        for i in range(c.grid_length):
            for j in range(c.grid_length):
                new_number = self.matrix[i][j]
                if new_number == 0:
                    self.grid_cells[i][j].configure(
                        text='', bg=c.background_colour_cell_empty
                    )
                else:
                    self.grid_cells[i][j].configure(text=str(
                        new_number
                    ), bg = c.background_colour_dict[new_number], fg=c.cell_colour_dict[new_number])
        self.update_idletasks()

    def key_down(self, event):
        key = repr(event.char)
        if key in self.commands:
            self.matrix, changed = self.commands[repr(event.char)](self.matrix)
            if changed:
                Logics.insert_random_2(self.matrix)
                self.update_grid_cells()
                changed = False
                if  Logics.current_state(self.matrix) == "WON":
                    self.grid_cells[1][1].configure(
                        text="You", bg=c.background_colour_cell_empty
                    )
                    self.grid_cells[1][2].configure(
                        text="Win!", bg=c.background_colour_cell_empty
                    )
                if Logics.current_state(Self.matrix)=="LOST":
                    self.grid_cells[1][1].configure(
                        text="You", bg=c.background_colour_cell_empty
                    )
                    self.grid_cells[1][2].configure(
                        text="Lose!", bg=c.background_colour_cell_empty
                    )

gameGrid = Game2048()