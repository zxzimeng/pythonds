from pickle import FALSE
import turtle
from typing import List
from time import sleep

maze = [
    list(row) for row in '''
+++++E++++++++++++++++
+   +   ++ ++     +  +
+ +   +       +++ + ++
+ + +  ++  ++++   + ++
+++ ++++++    +++ +  +
+          ++  ++    +
+++++ ++++++   +++++ +
+     +   +++++++  + +
+ +++++++        +   +
+                + +++
++++++++++++++++++S+++'''.splitlines(False) if len(row) > 0
]
maze.reverse()


def printMaze(maze):
  for i in reversed(maze):
    print(i)


COLOR_MAP = {
    '+': 'dim gray',  # wall
    'E': 'lime',  # exit 
    'S': 'slate blue',  # start
    ' ': 'white',  # blank
    '*': 'teal',  # current pos
    'p': 'spring green',  # visited|pending
    'a': 'deep sky blue',  # visited|accomplished
    'f': 'red',  # visited|failure
}


class MazeView():

  def __init__(self) -> None:
    self.w = turtle.Screen()
    self.t = turtle.Turtle()
    self.t.speed(0)
    self.w.delay(0)
    self.w.tracer(0)

  def drawMaze(self, mStr: List[List[str]]):
    self.t.goto(0, 0)
    self.t.clear()
    self.drawSquare(len(mStr) * 20)
    for i in range(len(mStr)):
      for j in range(len(mStr[i])):
        self.t.fillcolor(COLOR_MAP[mStr[i][j]])
        self.t.begin_fill()
        self.drawCell(i, j)
        self.t.end_fill()
    self.w.update()

  def drawSquare(self, s):

    # t.fillcolor("blue")
    # t.begin_fill()
    self.t.forward(s)  # Forward turtle by s units
    self.t.left(90)  # Turn turtle by 90 degree

    # drawing second side
    self.t.forward(s)  # Forward turtle by s units
    self.t.left(90)  # Turn turtle by 90 degree

    # drawing third side
    self.t.forward(s)  # Forward turtle by s units
    self.t.left(90)  # Turn turtle by 90 degree

    # drawing fourth side
    self.t.forward(s)  # Forward turtle by s units
    self.t.left(90)  # Turn turtle by 90 degree
    # t.end_fill()

  def exitOnClick(self):
    self.w.exitonclick()

  def drawCell(self, r, c):
    self.t.penup()
    self.t.goto(c * 20, r * 20)
    self.t.pendown()
    self.drawSquare(20)


mv = MazeView()


def runMaze():
  mv.drawMaze(maze)
  currentPos = [0, 0]
  for i in range(len(maze)):
    for x in range(len(maze[0])):
      if maze[i][x] == 'S':
        currentPos = [i, x]
  print(currentPos)
  nextStep(maze, currentPos)
  mv.drawMaze(maze)
  printMaze(maze)
  mv.exitOnClick()


def cellAt(maze: List, pos: List):
  if pos[0] < 0 or pos[1] < 0:
    return '+'
  if pos[0] >= len(maze) or pos[1] >= len(maze[0]):
    return '+'
  return maze[pos[0]][pos[1]]


def setCell(maze, pos, value):
  if pos[0] < 0 or pos[1] < 0:
    return
  if pos[0] >= len(maze) or pos[1] >= len(maze[0]):
    return
  maze[pos[0]][pos[1]] = value


def nextStep(maze: List, curP: List):
  printMaze(maze)
  # sleep(0.1)
  print(f'cur={curP}')
  mv.drawMaze(maze)
  if cellAt(maze, curP) == 'E':
    print('')
    return True
  positions = [
      [curP[0] + 1, curP[1]],
      [curP[0] - 1, curP[1]],
      [curP[0], curP[1] + 1],
      [curP[0], curP[1] - 1],
  ]
  setCell(maze, curP, 'p')
  for p in positions:
    cell = cellAt(maze, p)
    if cell in [' ', 'E']:
      if cell == ' ':
        setCell(maze, p, '*')
      accomplished = nextStep(maze, p)
      if accomplished:
        setCell(maze, curP, 'a')
        return True
      else:
        setCell(maze, p, 'f')
  return False


runMaze()