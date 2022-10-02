from math import pi

SUN_RADIUS = 6.957 * (10**8)
SUN_MASS = 1.989 * 10**30
SUN_LUM = 3.828 * 10**26
SB = 5.670367 * 10**-8
SUN_LIFE = 10**10
SUN_TEMP = 5778

star_radius = 6.957 * (10**8)
star_temp = 5778
star_mass = 2 * 10**30
star_life = 5 * 10**9
 
def find_abs_lum(radius, temp):
   surface_area = 4 * pi * (radius**2)
   return SB * surface_area * (temp**4)
 
def find_rel_lum(radius, temp):
   return (((radius / SUN_RADIUS)**2) * ((temp / SUN_TEMP)**4) )
 
def find_mass(radius, temp):
   return 8.852 * (10**20) * (radius **0.571) * (temp ** 1.142)
 
def find_lifetime(mass):
   return SUN_LIFE * (mass / SUN_MASS)**2.5
 
def mass_from_reminaing_lifetime(lifetime):
   return (lifetime / SUN_LIFE)**(1/2.5) * SUN_MASS
 
def find_radius_from_lifetime(lifetime, temp):
   return (mass_from_reminaing_lifetime(lifetime) / (8.852 * 10**20 * (temp ** 1.142)) ) **(1/0.571)
 
print(find_mass(star_radius, star_temp))
print(find_lifetime(star_mass))
print(mass_from_reminaing_lifetime(star_life))
print(find_radius_from_lifetime(10**10, star_temp))