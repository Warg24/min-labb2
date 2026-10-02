import math
from tkinter import *

# Task (2/12): Define a class Vec


class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x},{self.y})"

    def __rmul__(self, factor):
        return Vec(factor * self.x, factor * self.y)

    def __add__(self, other):
         return Vec(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)

    def norm(self):
        return math.hypot(self.x, self.y)

    def get_coords(self):
        return (self.x, self.y)

    

        
        


    

# Task (3/12): Additionally define a function dot(u, v)
def dot(u,v):
    return u.x * v.x + u.y * v.y
# Task (4/12): Create a class Particle

class Particle:
    def __init__(self, mass, position, velocity, radius):
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.radius = radius
# Task (5/12): In the Particle class, implement a method inertial_move(self, dt).
    def inertial_move(self, dt):
        self.position = dt * self.velocity + self.position
# Task (6/12): In the Particle class, implement a method apply_force(self, dt, f)

    def apply_force(self, dt, f):
        self.velocity = self.velocity + (dt / self.mass) * f


##########################################
### NB. Tasks 7–8 are done in view.py. ###
##########################################


# Task (9/12): In the Particle class, add a method bounding_box(self)






###########################################
### When you're done with all 12 tasks: ###
### forces/other features in this file! ###
###########################################
