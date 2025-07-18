import pygame 

pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.set_caption("Expermental Image Draw Test")
    dispObj = pygame.Rect((200,150),(400,300))
    screen.fill("purple", dispObj)
    pygame.display.flip()
    clock.tick(60.0)

print(pygame.display.get_caption())
pygame.quit()