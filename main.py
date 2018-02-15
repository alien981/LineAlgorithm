from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
c1 = [255, 255, 255]
c2 = [255, 0, 0]
c3 = [0, 0, 255]

draw_line(200, 100, 200, 200, screen, color) 
draw_line(0, 100, 100, 100, screen, color) 
draw_line(0, 0, 500, 100, screen, c3)
draw_line(0, 0, 100, 500, screen, c2)

display(screen)
save_extension(screen, 'img.png')
