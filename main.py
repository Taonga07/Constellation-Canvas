import pygame 

pygame.init()

screen = pygame.display.set_mode((500,500))
length_held = 0 
old_pos = (0,0)
direction = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    if pygame.mouse.get_pressed()[0]:
        if old_pos == pygame.mouse.get_pos():
            print(length_held)
            if (length_held < 10) and (direction == 1):
                direction = -1
            if (length_held < 0) and (direction == -1):
                direction = 1
            length_held += (0.01*direction)
        else: 
            length_held = 0 
            old_pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen, (125,125,125), pygame.mouse.get_pos(), length_held)
    pygame.display.flip()