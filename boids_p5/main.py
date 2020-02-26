from p5 import *
import numpy as np
from boid import Boid

# Define the size of the window
width = 1000 
height = 1000

number_of_boids = 30

# Create an array of 30 boids with random x and y positions
flock = [Boid(*np.random.rand(2)*1000, width, height) for _ in range(number_of_boids)]

# If you are familiar with Processing, then p5 will look very similar.
# The main functions are setup() and draw()
# setup() runs once, draw() runs every frame
# If you don't know processing, but know Unity, then think of them as Start() and Update()
#Additionally, the main file needs to end with run() in order to execute.

def setup():

    size(width, height)

def draw():
    # draw the background every frame
    background(30, 30, 47)

    for boid in flock:
        # display the boids  
        boid.show()
        # apply flocking behaviour
        boid.apply_behaviour(flock)
        # move the boids
        boid.update()
        # wrap position if they move off-screen
        boid.edges()

# Run the sketch
# frame_rate is an optional parameter
# This code is poorly optimized, and runs like garbage on my personal hardware
# It might be somewhat smoother on a computer with a bit more life remaining.
run()   