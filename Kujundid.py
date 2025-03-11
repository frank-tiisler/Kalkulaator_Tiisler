import pygame

screen=pygame.display.set_mode([300,300])
pygame.display.set_caption("Lumemees")
screen.fill([0, 0, 0])
pygame.draw.circle(screen, [255,255,255], [150,225], 45, 1)
pygame.draw.circle(screen, [255,255,255], [150,145], 35, 1)
pygame.draw.circle(screen, [255,255,255], [150,85], 25, 1)

pygame.display.flip()
pygame.init()
pygame.quit()