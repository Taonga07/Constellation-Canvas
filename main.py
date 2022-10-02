from ursina.prefabs.dropdown_menu import DropdownMenu, DropdownMenuButton
from ursina import Ursina, Entity, Sky, EditorCamera, Slider

app = Ursina()


class Star(Entity):
     def __init__(self, **kwargs):
        super().__init__(model = "sphere", texture = 'sun_texture.jpg', scale=Slider())

cam = EditorCamera()
cam.target_z -= cam.zoom_speed * (abs(cam.target_z)*20)


earth = Star()
Sky(color="#000000")

app.run()
