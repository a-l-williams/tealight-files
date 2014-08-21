from github.calintat.art.racetrack import *
from tealight.utils import github_load
project_globals = github_load("a-l-williams", "art", "project-globals")
key_handlers = github_load("lordvile018", "art", "racetrack")
y = project_globals.Globals()
print y.get_connection_string()

draw_track()
current_direction = 0
previous_direction = 0
current_acceleration = 0
rotating = 0 # 0 for not, 1 for left, 2 for right
current_x = 77
current_y = 412


def handle_keydown(key):
  global rotating
  previous_direction = current_direction
  data = key_handlers.direction_handle_keydown(key, current_direction)
  if data is not None and "key" in data:
    if data['key'] == "left":
      rotating = 1
      print rotating
    elif data['key'] == "right":
      rotating = 2
      print rotating
      
def handle_keyup(key):
  global rotating
  data = key_handlers.direction_handle_keyup(key, current_direction)
  if "key" in data:
    if data['key'] == "left" or data['key'] == "right":
      rotating = 0
      
def handle_frame():
  global current_direction, previous_direction
  #print "Previous direction is", previous_direction
  if rotating == 1:
    current_direction -= 5
  elif rotating == 2:
    current_direction += 5
  #print "Current direction is", current_direction
  draw_track()
  #draw_triangle(100,80,previous_direction,20,"white")
  draw_triangle(current_x,current_y,current_direction,10,"red")
  
  previous_direction = current_direction


#print test_polygon(100, 100, [(100,200), (50, 50), (200,100), (150,250)])