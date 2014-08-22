from github.calintat.art.racetrack import *
from tealight.utils import github_load, now, sleep
project_globals = github_load("a-l-williams", "art", "project-globals")
key_handlers = github_load("lordvile018", "art", "racetrack")
network_client = github_load("lordvile018", "art", "racetrackclient")

y = project_globals.Globals()
print y.get_connection_string()

draw_track()
current_direction = 0
last_sent = now()
previous_direction = 0
current_acceleration = 0
rotating = 0 # 0 for not, 1 for left, 2 for right
accelerating = 0 # 0 for not, 1 for forward, 2 for back
current_x = 77
current_y = 412
current_velocity = 0
current_size = 10
score = 0

def lose():
  global score
  text(5,20,"You lose!")

  network_client.authenticated_send({"state": "lose"}, "server", "status")
  score = 0
  draw_track()
def handle_keydown(key):
  global rotating, current_velocity, accelerating
  previous_direction = current_direction
  data = key_handlers.direction_handle_keydown(key, current_direction)
  if data is not None and "key" in data:
    if data['key'] == "left":
      rotating = 1
    elif data['key'] == "right":
      rotating = 2
  if key == "up":
    accelerating = 1
  elif key == "space":
    accelerating = 2
      
def handle_keyup(key):
  global rotating, accelerating
  data = key_handlers.direction_handle_keyup(key, current_direction)
  if "key" in data:
    if data['key'] == "left" or data['key'] == "right":
      rotating = 0
    elif data['key'] == "down" or data['key'] == "up":
      accelerating = 0
      
def handle_frame():
  
  global last_sent, score, current_direction, previous_direction, current_x, current_y, current_velocity, accelerating, rotating
  if rotating == 1:
    current_direction -= 5
  elif rotating == 2:
    current_direction += 5
  draw_track()
  color("white")
  text(5,5,"Score: " + str(score))
  movement_data = movement(current_x, current_y, current_velocity, current_direction, current_size)
  
  if check_finish(current_x, current_y) == True:
    color("white")
    text(5,20,"You win!")
    network_client.authenticated_send({"state": "win"}, "server", "status")
    current_x = 77
    current_y = 412
    current_velocity = -900
    
  if "losing" in movement_data:
    current_x = 77
    current_y = 412
    current_velocity = 0
    current_direction = 0
    accelerating = 0
    rotating = 0
    lose()
  else:
    if accelerating == 0:
      if current_velocity <= 0.1:
        current_velocity = 0
      else:
        current_velocity *= 0.95    
    elif current_velocity > 0 and current_velocity <= 0.1:
      current_velocity = 0
    elif current_velocity < 0:
      current_velocity += 0.1
    current_x = movement_data['x']
    current_y = movement_data['y']
    if accelerating == 1:
      data = movement_handle_keydown("up", current_velocity)
      if data is not None:
        current_velocity = data['speed']
    draw_triangle(current_x,current_y,current_direction,current_size,"red")
    previous_direction = current_direction
  if accelerating > 0 and now()- last_sent > 0.5:
    last_sent = now()
    score += 1
  if now() - last_sent > 2:
    network_client.client_handle_frame()
    last_sent = now()



#print test_polygon(100, 100, [(100,200), (50, 50), (200,100), (150,250)])