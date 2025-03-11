import pygame
pygame.init()

screen=pygame.display.set_mode([300,300])
pygame.display.set_caption("Lumemees")
screen.fill([0, 0, 0])
pygame.draw.circle(screen, [255,255,255], [150,50])

pygame.display.update()
running = True
while running:

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()