from p5 import *

class Boid():
    def __init__(self, x, y, width, height):
        # position
        self.position = Vector(x, y)

        # references to size of window
        self.width = width
        self.height = height

        # random velocity
        vec = (np.random.rand(2) - 0.5)*10
        self.velocity = Vector(*vec)

        # random acceleration
        vec = (np.random.rand(2) - 0.5)/2
        self.acceleration = Vector(*vec) 
        
        # Behvaiour Parameters
        self.max_speed = 10  
        self.max_force = 1
        self.perception = 100


    def show(self):
        stroke(255)
        circle((self.position.x, self.position.y), radius=10)

    
    def align(self, boids):
        # Boids try to move in the same direction as other nearby boids

        # initialize empty vectors
        steering = Vector(*np.zeros(2))
        total = 0
        avg_vec = Vector(*np.zeros(2))

        for boid in boids:
            # only look locally at nearby boids in the flock
            if np.linalg.norm(boid.position - self.position) < self.perception:
                avg_vec += boid.velocity
                total += 1
        # don't do anything if a boid is alone
        # otherwise, get the average direction of all the boids, and return a vector steering towards it
        if total > 0:
            avg_vec /= total
            avg_vec = Vector(*avg_vec) 
            avg_vec = (avg_vec /np.linalg.norm(avg_vec)) * self.max_speed 
            steering = avg_vec - self.velocity

        return steering


    def cohesion(self, boids):
        # Boids try to stay near the centre of the group of boids

        # initialize empty vectors
        steering = Vector(*np.zeros(2))
        total = 0
        center_of_mass = Vector(*np.zeros(2))

        for boid in boids:
            # Only look at nearby Boids
            if np.linalg.norm(boid.position - self.position) < self.perception:
                center_of_mass += boid.position
                total += 1

        if total > 0:
            # Do nothing if a boid is alone.
            # otherwise, find the centre of mass
            # (since all boids are the same mass, this is just the average position)
            # return a vector to steer towards the CoM, limited by max_speed and max_force
            center_of_mass /= total
            center_of_mass = Vector(*center_of_mass)
            vec_to_com = center_of_mass - self.position
            if np.linalg.norm(vec_to_com) > 0:
                vec_to_com = (vec_to_com / np.linalg.norm(vec_to_com)) * self.max_speed
            steering = vec_to_com - self.velocity
            if np.linalg.norm(steering)> self.max_force:
                steering = (steering /np.linalg.norm(steering)) * self.max_force

        return steering


    def separation(self, boids):
        # Boids move away from closer boids to avoid crashing

        # initialze empty arrays
        steering = Vector(*np.zeros(2))
        total = 0
        avg_vector = Vector(*np.zeros(2))
        for boid in boids:
            distance = np.linalg.norm(boid.position - self.position)
            if self.position != boid.position and distance < self.perception:
                # only look at nearby boids (excluding yourself)
                # in this case, the closer a boid it, the more force it exerts
                # that is, the higher the chance of crashing, the more important it is to move away
                diff = self.position - boid.position
                diff /= distance
                avg_vector += diff
                total += 1
        if total > 0:
            # do nothing if a boid is alone
            # otherwise, steer away from nearby boids
            avg_vector /= total
            avg_vector = Vector(*avg_vector)
            if np.linalg.norm(steering) > 0:
                avg_vector = (avg_vector / np.linalg.norm(steering)) * self.max_speed
            steering = avg_vector - self.velocity
            if np.linalg.norm(steering)> self.max_force:
                steering = (steering /np.linalg.norm(steering)) * self.max_force

        return steering


    def apply_behaviour(self, boids):
        alignment = self.align(boids)
        cohesion = self.cohesion(boids)
        separation = self.separation(boids)

        self.acceleration += alignment
        self.acceleration += cohesion
        self.acceleration += separation
    
    def update(self):
        # simple movement
        self.position += self.velocity
        self.velocity += self.acceleration

        #limit
        if np.linalg.norm(self.velocity) > self.max_speed:
            self.velocity = self.velocity / np.linalg.norm(self.velocity) * self.max_speed

        self.acceleration = Vector(*np.zeros(2))

    def edges(self):
        # wrap position around edges if boids move outside of window
        if self.position.x > self.width:
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = self.width

        if self.position.y > self.height:
            self.position.y = 0
        elif self.position.y < 0:
            self.position.y = self.height

