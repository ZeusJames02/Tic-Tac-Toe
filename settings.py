import os
# Screen's size
size = width, height = 640, 480

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
LIGHTBLUE = (0, 155, 155)
LIGHTYELLOW = (155, 155, 0)
GRAY = (155, 155, 155)

# Frames per second
FPS = 120

# Line division
LINES = {(width/3, 0):(width/3, height),
         (2*(width/3), 0):(2*(width/3), height),
         (0, height/3):(width, height/3),
         (0, 2*height/3):(width, 2*height/3)}

# Points to be placed
POINTS = [(width/6, height/6),
          (width/2, height/6),
          (2*width/3 + width/6, height/6),
          (width/6, height/3 + height/6),
          (width/2, height/2),
          (2*width/3 + width/6, height/3 + height/6),
          (width/6, 2*height/3 + height/6),
          (width/2, 2*height/3 + height/6),
          (2*width/3 + width/6, 2*height/3 + height/6)]
X_img = os.path.expanduser("X.png")
O_img = os.path.expanduser("Y.png")
