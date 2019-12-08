from array import *
from copy import copy, deepcopy

DEFINE_CELLS_IN_ROW = 9
DEFINE_CUBES_BLOCK = 3

class PuzzleSudoku:
    
    def check_cube_val_zero(self, table):
        for i in range(len(table)):
            for j in range(len(table[0])):
                if table[i][j] == 0:
                    return (i,j)
        return None            
 
    def pretty_print_in_2D(self, sudoku):

        for i in range(len(sudoku)):
            if i%3 == 0 and i != 0:
                print ''
            for j in range(len(sudoku[0])):
                if j%3 == 0  and j != 0:
                    print '|',
                if j == DEFINE_CELLS_IN_ROW-1:
                    print sudoku[i][j]
                else:
                    print (sudoku[i][j] ),

    def authenticate_each_cell_input(self, table, num, sector_block):
        sector_row = sector_block[1] // DEFINE_CUBES_BLOCK
        sector_col = sector_block[0] // DEFINE_CUBES_BLOCK

        #check row
        for i in range(len(table[0])):
            if table[sector_block[0]][i] == num and sector_block[1] != i:
                return False
        #check col
        for i in range(len(table)):
            if table[i][sector_block[1]] == num and sector_block[0] != i:
                return False

        for i in range(sector_col*DEFINE_CUBES_BLOCK, sector_col*DEFINE_CUBES_BLOCK +DEFINE_CUBES_BLOCK):
            for j in range(sector_row*DEFINE_CUBES_BLOCK, sector_row*DEFINE_CUBES_BLOCK +DEFINE_CUBES_BLOCK):
                #print (i,j)
                if table[i][j] == num and (i,j) != sector_block:
                    return False
        return True

    def do_action(self, sudoku_table):
        sector_block = self.check_cube_val_zero(sudoku_table)
        if not sector_block:
            return True
        for i in range(1,10):
            if self.authenticate_each_cell_input(sudoku_table, i, sector_block):
                row, col = sector_block
                sudoku_table[row][col] = i
                if self.do_action(sudoku_table):
                    return True
                sudoku_table[row][col] = 0
        return False

    def get_working_table(self, sudoku_table):
        tmp_table = deepcopy(sudoku_table)
        self.do_action(sudoku_table)
        if tmp_table == sudoku_table:
            return False
        else:
            return True


 
bss =[
        [7,8,0,4,0,0,1,2,0],
        [6,0,0,0,7,5,0,0,9],
        [0,0,0,6,0,1,0,7,8],
        [0,0,7,0,4,0,2,6,0],
        [0,0,1,0,5,0,9,3,0],
        [9,0,4,0,6,0,0,0,5],
        [0,7,0,3,0,0,0,1,2],
        [1,2,0,0,0,7,4,0,0],
        [0,4,9,2,0,6,0,0,7]
]
