from github.calintat.art.racetrack import draw_triangle
from github.lordvile018.art.racetrack import handle_keydown, handle_keyup
from tealight.utils import github_load
project_globals = github_load("a-l-williams", "art", "project-globals")
key_handlers = github_load("lordvile018", "art", "racetrack")

y = project_globals.Globals()
print y.get_connection_string()


current_direction = 0
current_acceleration = 0



def handle_keydown(key):
  current_direction = key_handlers.direction_handle_keydown(key, current_direction)

def handle_frame():
  
  draw_triangle(50,50,currentDirection,20,"red")


#print test_polygon(100, 100, [(100,200), (50, 50), (200,100), (150,250)])