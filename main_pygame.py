from math import pi
import pygame

SUN_RADIUS = 6.957 * (10**8)
SUN_MASS = 1.989 * 10**30
SUN_LUM = 3.828 * 10**26
SB = 5.670367 * 10**-8
SUN_LIFE = 10**10
SUN_TEMP = 5778


pygame.init()
screen = pygame.display.set_mode((500,500))
length_held = 0 
old_pos = (0,0)



class Star():
    def __init__(self, radius, temperture) -> None:
        self.lifetime = SUN_LIFE * ((8.852 * (10**20) * (radius **0.571) * ((temperture) ** 1.142)) / SUN_MASS) ** 2.5
        self.temperture = (((self.lifetime / SUN_LIFE) ** (1/2.5) * SUN_MASS) / (8.852 * 10**20 * (self.radius ** 0.571)) ) ** (1/1.142)
        self.radius = (((self.lifetime / SUN_LIFE) ** (1/2.5) * SUN_MASS) / (8.852 * 10**20 * (self.temperture ** 1.142)) ) ** (1/0.571)
        self.luminenecence = lambda: SB * (4 * pi * (self.radius**2)) * (self.temperture**4)
        self.mass = lambda: (self.lifetime / SUN_LIFE)**(1/2.5) * SUN_MASS
    
    def colour(self) -> str:
        colours=["#0000FF","#dbe9f4","#FFFFFF","#ffffd4","#FFFF00","#FFA500","#FF0000"]
        if self.temperture >= 30000: return colours[0]
        if 30000 > self.temperture >= 20000: return colours[1]
        if 20000 > self.temperture >= 10000: return colours[2]
        if 10000 > self.temperture >= 7000: return colours[3]
        if 7000 > self.temperture >= 6000: return colours[4]
        if 5000 > self.temperture >= 3000: return colours[5]


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    if pygame.mouse.get_pressed()[0]:
        if old_pos == pygame.mouse.get_pos():
            length_held += (0.01)
        else: 
            length_held = 0 
            old_pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen, (125,125,125), pygame.mouse.get_pos(), length_held)
    pygame.display.flip()

