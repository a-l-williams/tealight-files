from github.calintat.art.racetrack import draw_triangle
from github.lordvile018.art.racetrack import handle_keydown, handle_keyup
from tealight.utils import github_load
x = github_load("a-l-williams", "art", "project-globals")
y = x.Globals()
print y.get_connection_string()


currentDirection = 0

def handle_frame():
  global currentDirection
  draw_triangle(50,50,currentDirection,20,"red")


#print test_polygon(100, 100, [(100,200), (50, 50), (200,100), (150,250)])