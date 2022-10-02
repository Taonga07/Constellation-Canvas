from ursina import Ursina, Entity, EditorCamera, Sky, Slider, Text
from math import pi

SUN_RADIUS = 6.957 * (10**8)
SUN_MASS = 1.989 * 10**30
SUN_LUM = 3.828 * 10**26
SB = 5.670367 * 10**-8
SUN_LIFE = 10**10
SUN_TEMP = 5778

length_held = 0 
old_pos = (0,0)

class Star(Entity):
    def __init__(self, radius, temperture) -> None:
        super().__init__(model = "sphere", texture = 'sun_texture.jpg', scale = 100)
        self.inital_lifetime = SUN_LIFE * ((8.852 * (10**20) * (radius **0.571) * ((temperture) ** 1.142)) / SUN_MASS) ** 2.5
        self.radius, self.temperture, self.lifetime = radius, temperture, self.inital_lifetime
        self.luminenecence = lambda: SB * (4 * pi * (self.radius**2)) * (self.temperture**4)
        self.mass = lambda: (self.lifetime / SUN_LIFE)**(1/2.5) * SUN_MASS

    def update(self) -> None:
        self.radius = (((self.lifetime / SUN_LIFE) ** (1/2.5) * SUN_MASS) / (8.852 * 10**20 * (self.temperture ** 1.142)) ) ** (1/0.571)
        self.temperture = (((self.lifetime / SUN_LIFE) ** (1/2.5) * SUN_MASS) / (8.852 * 10**20 * (self.radius ** 0.571)) ) ** (1/1.142)
        colours=["#0000FF","#dbe9f4","#FFFFFF","#ffffd4","#FFFF00","#FFA500","#FF0000"]
        if self.temperture >= 30000: self.color =  colours[0]
        if 30000 > self.temperture >= 20000: self.color =  colours[1]
        if 20000 > self.temperture >= 10000: self.color =  colours[2]
        if 10000 > self.temperture >= 7000: self.color =  colours[3]
        if 7000 > self.temperture >= 6000: self.color =  colours[4]
        if 5000 > self.temperture >= 3000: self.color =  colours[5]
        self.scale = self.radius*2 / 10**8

def update():
    #a.lifetime = s.value*a.inital_lifetime
    a.update()
    a.color = "#0046bd"
    print(a.lifetime, a.temperture)

if __name__ == '__main__':
    app = Ursina()
    a = Star((6.957 * (10**8)), 5778)
    s = Slider(min=0, max=1, step=0.1, vertical=False)
    s.label.origin = (0,-1)
    Sky(color="#000000")
    camera = EditorCamera()
    app.run()