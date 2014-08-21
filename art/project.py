from github.calintat.art.racetrack import draw_triangle
from github.lordvile018.art.racetrack import handle_keydown, handle_keyup

currentDirection = 0

def handle_frame():
  draw_triangle(50,50,currentDirection,20,"red")


#print test_polygon(100, 100, [(100,200), (50, 50), (200,100), (150,250)])