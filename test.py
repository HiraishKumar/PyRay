import pygame
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

pygame.init()
win = pygame.display.set_mode((1000, 600))

slider = Slider(win, 25, 25, 200, 10, min=0, max=99, step=1, initial = 10)
output = TextBox(win, 250, 17, 35, 30, fontSize=15)
output.disable()  # Act as label instead of textbox

run = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            quit()

    win.fill((255, 255, 255))
    output.setText(" "+str(slider.getValue()))

    pygame_widgets.update(events)
    pygame.display.update()