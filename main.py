from ursina.prefabs.dropdown_menu import DropdownMenu, DropdownMenuButton
from ursina import Ursina, Entity, Sky

app = Ursina()

DropdownMenu('File', buttons=(
    DropdownMenuButton('New'),
    DropdownMenuButton('Open'),
    DropdownMenuButton('Save'))
)

class Star(Entity):
     def __init__(self, **kwargs):
        super().__init__()
        self.model = "sphere",
        self.texture = 'sun_texture.jpg'
        self.luminocity = 0
        self.radius = 0
        self.surface_area = 0
        self.lifetime = 0
    def get_missing(varibels):
        

#earth = Star()
Sky(color="#000000")

app.run()

# screen = pygame.display.set_mode((500,500))
# length_held = 0 
# old_pos = (0,0)
# direction = 0
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#     if pygame.mouse.get_pressed()[0]:
#         if old_pos == pygame.mouse.get_pos():
#             print(length_held)
#             if (length_held < 10) and (direction == 1):
#                 direction = -1
#             if (length_held < 0) and (direction == -1):
#                 direction = 1
#             length_held += (0.01*direction)
#         else: 
#             length_held = 0 
#             old_pos = pygame.mouse.get_pos()
#         pygame.draw.circle(screen, (125,125,125), pygame.mouse.get_pos(), length_held)
#     pygame.display.flip()

# class star()