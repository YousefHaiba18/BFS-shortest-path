# Yousef Haiba
# 05/06/2022
# BFS shortest path

import queue
import time   
import curses
from curses import wrapper




maze = [
    ["X", "S", "X", " ", "X", "X", "X", "X", "X"],
    ["X", " ", " ", " ", " ", " ", " ", " ", "X"],
    ["X", " ", "X", "X", " ", "X", "X", "X", "X"],
    ["X", "X", "X", " ", " ", " ", "X", " ", "X"],
    ["X", " ", "X", " ", "X", "X", " ", " ", "X"],
    ["X", " ", "X", " ", "X", " ", "X", " ", "X"],
    ["X", " ", "X", " ", "X", " ", "X", "X", "X"],
    ["X", " ", " ", " ", " ", " ", " ", "X", "X"],
    ["X", "X", "X", "X", "X", "X", " ", " ", "X"],
    ["X", " ", "X", " ", "X", " ", "X", " ", "X"],
    ["X", "X", " ", " ", " ", " ", " ", " ", "X"],
    ["X", "X", "X", " ", "X", "X", " ", " ", "X"],
    ["X", " ", "X", " ", " ", " ", "X", "X", "X"],
    ["X", " ", " ", " ", " ", " ", " ", " ", "X"],
    ["X", "X", "X", " ", "X", "X", "X", "E", "X"]

]

def StartFinder(maze, start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j

    return None




def print_maze(maze, stdscr, path=[]):
    white = curses.color_pair(1)
    red = curses.color_pair(2)

    for i, row in enumerate(maze):       
        for j, value in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i, j*3, "O", red) #represents path taken
            else:
                stdscr.addstr(i, j*3, value, white) #represents border/barriers



def PathFinder(maze, stdscr):
    start = "S"
    end = "E"
    start_pos = StartFinder(maze, start)

    q = queue.Queue()
    q.put((start_pos, [start_pos]))

    visited = set()

    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos

        stdscr.clear()
        print_maze(maze, stdscr, path)
        time.sleep(0.35)  # delay drawing graph to see the path taken step by step
        stdscr.refresh()

        if maze[row][col] == end:
            return path

        adjacent = FindAdjacent(maze, row, col)
        for next in adjacent:
            if next in visited:
                continue

            r, c = next
            if maze[r][c] == "X":
                continue

            NewPath = path + [next]
            q.put((next, NewPath))
            visited.add(next)




def FindAdjacent(maze, row, col):  #finding adjacent spaces
    adjacent = []

    if row > 0:  
        adjacent.append((row - 1, col))
      
    if row + 1 < len(maze):  
        adjacent.append((row + 1, col))
      
    if col > 0:  
        adjacent.append((row, col - 1))
      
    if col + 1 < len(maze[0]): 
        adjacent.append((row, col + 1))

    return adjacent


def main(stdscr):
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    PathFinder(maze, stdscr)
    stdscr.getch()


wrapper(main)