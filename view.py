############################################################
### NB. This module is partially implemented for DAT425. ###
############################################################
import time
from model import *
import tkinter as tk


# Task (7/12): Draw on canvas
root = tk.Tk()

height = 600 # Change if you want a larger or smaller canvas
width = 800
canvas = tk.Canvas(root, width=width, height=height)
canvas.pack()
canvas.create_oval(80, 30, 140, 150, fill="blue")
canvas.update_idletasks()



# Test that it works: draw something on the canvas!


# Task (8/12): Define a new function to_canvas_coords(canvas, u)
def mirror_y(u):
    """Takes a vector `u`, of class Vec that you have defined in model.py. 
    Returns a new vector where the y coordinate is mirrored.
    """
    (x,y) = u.get_coords()
    return Vec(x,-y)

def to_canvas_coords(canvas,u):
    """Takes a vector `u` in simulation coordinates, 
    and returns a new vector in canvas coordinates.
    """
    h = canvas.winfo_reqheight()
    w = canvas.winfo_reqwidth()
    return Vec(w/2, h/2) + (h/20) * mirror_y(u)

#######################################
### NB. Task 9 is done in model.py. ###
#######################################

# Task (10/12): Define a new function move_oval_to(o, u1, u2)
def move_oval_to(canvas,o,u1,u2):
    """Moves the oval `o` to a specific bounding box, 
    given by two vectors `u1` and `u2`.
    """
    (x1,y1) = to_canvas_coords(canvas,u1).get_coords()
    (x2,y2) = to_canvas_coords(canvas,u2).get_coords()
    canvas.coords(o, x1, y1, x2, y2)


# Task (11/12): Define a new function create_oval(canvas, particle)
def create_oval(canvas, particle):
    """Creates an oval from a particle."""
    o = canvas.create_oval(0, 0, 0, 0)
    u1, u2 = particle.bounding_box()
    move_oval_to(canvas, o, u1, u2) 
    return o



# Task (12/12): Define a function simulation_loop(f, timestep, particles)
def simulation_loop(f, timestep, particles):

    multiple_ovals = []

    for p in particles:
        oval = create_oval(canvas, p)
        multiple_ovals.append(oval)
        last_update = time.time()

    while True:

        f(timestep, particles)

        for p in particles:
            p.inertial_move(timestep)

        now = time.time()

        if now - last_update > 1/30:
            for i in range(len(particles)):
                u, w = particles[i].bounding_box()
                move_oval_to(canvas, multiple_ovals[i], u, w)
            canvas.update()
            last_update = now
            print(particles[0].position)

