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
accelerating = 0 # 0 for not, 1 for forward, 2 for back
current_x = 77
current_y = 412
current_velocity = 0

def handle_keydown(key):
  global rotating, current_velocity, accelerating
  previous_direction = current_direction
  data = key_handlers.direction_handle_keydown(key, current_direction)
  if data is not None and "key" in data:
    if data['key'] == "left":
      rotating = 1
      print rotating
    elif data['key'] == "right":
      rotating = 2
      print rotating

  if key == "up":
    accelerating = 1
    print "Key down up!"
  else:
    accelerating = 2
      
def handle_keyup(key):
  global rotating
  data = key_handlers.direction_handle_keyup(key, current_direction)
  if "key" in data:
    if data['key'] == "left" or data['key'] == "right":
      rotating = 0
    elif data['key'] == "down" or data['key'] == "up":
      accelerating = 0
      
def handle_frame():
  global current_direction, previous_direction, current_x, current_y, current_velocity
  #print "Previous direction is", previous_direction
  if rotating == 1:
    current_direction -= 5
  elif rotating == 2:
    current_direction += 5
  #print "Current direction is", current_direction
  draw_track()
  #draw_triangle(100,80,previous_direction,20,"white")
  movement_data = movement(current_x, current_y, current_velocity, current_direction)
  if current_velocity > 0.1:
    current_velocity -= 0.1
  elif current_velocity > 0 and current_velocity <= 0.1:
    current_velocity = 0
  elif current_velocity < 0:
    current_velocity += 0.1
  current_x = movement_data['x']
  current_y = movement_data['y']
  if accelerating == 1:
    data = movement_handle_keydown("up", current_velocity)
    current_velocity = data['speed']
  draw_triangle(current_x,current_y,current_direction,10,"red")
  #print current_velocity
  previous_direction = current_direction


#print test_polygon(100, 100, [(100,200), (50, 50), (200,100), (150,250)])