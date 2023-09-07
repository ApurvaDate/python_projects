from tkinter import Button
import random 
import settings

class Cell:
    all = []
    def __init__(self, x, y, is_mine = False):
        self.is_mine = is_mine 
        self.cell_btn_object = None #None at first
        self.x = x
        self.y = y
        #Append the object to cell.all list
        Cell.all.append(self)
        #we will create a instance  method that will create this button for us and assign it to self.cell_btn_object

    def create_btn_object(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
            text=f"({self.x},{self.y})"
        )     #we are just instantiating an instance of Button class
        #locate the element using location 
        #if we receive the parameter location, thn we should pass it , whenever we call it, we refer to actual center_frame 
        #which will be from minesweeper.py
        btn.bind('<Button-1>', self.left_click_actions) 
        btn.bind('<Button-3>', self.right_click_actions) 
        self.cell_btn_object = btn
        #Button-1 = left click and Button - 3 = right click
        #here we are not calling the method, just passig the reference of that method.
        
    
    def left_click_actions(self, event ):
        # print(event) 
        # #we need more parameter to assign an event
        # print("I am left clicked")
        if self.is_mine:
            self.show_mine() 
        else:
            self.show_cell()
    def show_mine(self):
        #a logic to interrupt the game and display a message that player lost!
        #converting a background of that cell into a red background shoul be enough to highlight the mine
        self.cell_btn_object.configure(bg ="red")

    def get_cell_by_axis(self,x,y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return x,y
        #return a cel object based on the value of x & y
        #iterate over all list
    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y -1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1)
        ]

        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1

        return counter
        
    def show_cell(self):
        return self.surrounded_cells_mines_length

    
    def right_click_actions(self, event ):
        print(event) #we need more parameter to assign an event
        print("I am right clicked")

    
    @staticmethod
    def randomize_mines():  #it takes couple of cells and turns them into mine
        picked_cells = random.sample(Cell.all,settings.MINES_COUNT) #it includes all the instances 
        print(picked_cells)
        for picked_cell in picked_cells:
            picked_cell.is_mine = True


    def __repr__(self):
        return f"Cell({self.x},{self.y})"

