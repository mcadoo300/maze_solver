from graphics import MazeWindow, WelcomeWindow
from maze import Maze
import sys

def main():
    win = WelcomeWindow()
    win, data = win.GenNewMaze()
    pad=25
    maze_test = Maze(x1=pad,y1=pad,num_rows=data[0],num_cols=data[1],cell_size_x=30,cell_size_y=30,window=win)

    maze_test.start()
    maze_test._break_entrance_and_exit()
    maze_test._break_walls_r(0,0)
    maze_test.reset_visited()
    
    maze_test.solveBFS()
    win.waitForClose()
    

if __name__ == "__main__":
    main()