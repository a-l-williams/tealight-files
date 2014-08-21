from github.calintat.art.racetrack import draw_triangle
from tealight.utils import github_load
project_globals = github_load("a-l-williams", "art", "project-globals")
key_handlers = github_load("lordvile018", "art", "racetrack")

y = project_globals.Globals()
print y.get_connection_string()


current_direction = 0
previous_direction = 0
current_acceleration = 0



def handle_keydown(key):
  global current_direction, previous_direction
  previous_direction = current_direction
  current_direction = key_handlers.direction_handle_keydown(key, current_direction)

def handle_frame():
  global current_direction, previous_direction
  print "Previous direction is", previous_direction
  print "Current direction is", current_direction
  draw_triangle(50,50,previous_direction,20,"white")
  draw_triangle(50,50,current_direction,20,"red")


#print test_polygon(100, 100, [(100,200), (50, 50), (200,100), (150,250)])