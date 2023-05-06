import math
import matplotlib.pyplot as plt

class Vector:
    
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        
    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"
    
    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"
    
    def __getitem__(self, item):
        if item == 0:
            return self.x
        elif item == 1:
            return self.y
        elif item == 2:
            return self.z
        else:
            raise IndexError("There are only three elements in the vector")
            
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        
    def __mul__(self, other):
        if isinstance(other, Vector):
            return (self.x * other.x + self.y * other.y + self.z * other.z)
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other, self.z * other)
        else:
            raise TypeError("operand must be Vector, int, or float")
            
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x / other, self.y / other, self.z / other)
        else:
            raise TypeError("operand must be int or float")
            
    def get_magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
    
    def normalize(self):
        magnitude = self.get_magnitude()
        return Vector(
            self.x / magnitude,
            self.y / magnitude,
            self.z / magnitude,
        )

class SolarSystem:

    def __init__(self, size, projection2d = False):
        self.size = size
        self.projection2d = projection2d
        self.bodies = []
        self.fig, self.ax = plt.subplots(
            1,
            1,
            subplot_kw={"projection": "3d"},
            figsize=(self.size / 50, self.size / 50),
        )
        self.fig.tight_layout()
        self.ax.set_facecolor((0.9, 0.9, 0.9))
        if not self.projection2d:
            self.ax.view_init(10, 5)
        else:
            self.ax.view_init(0, 0)


    def add_body(self, body):
        self.bodies.append(body)

    def update_all(self):
        self.bodies.sort(key=lambda item: item.position[0])
        for body in self.bodies:
            body.move()
            self.check_if_fusion()
            body.draw()

    def draw_all(self):
        self.ax.set_xlim((-self.size / 2, self.size / 2))
        self.ax.set_ylim((-self.size / 2, self.size / 2))
        self.ax.set_zlim((-self.size / 2, self.size / 2))
        if not self.projection2d:
            self.ax.xaxis.set_ticklabels([])
            self.ax.yaxis.set_ticklabels([])
            self.ax.zaxis.set_ticklabels([])
        else:
            self.ax.axis(False)
        plt.pause(0.001)
        self.ax.clear()

    def calculate_all_body_interactions(self):
        bodies_copy = self.bodies.copy()
        for idx, first in enumerate(bodies_copy):
            for second in bodies_copy[idx + 1:]:
                first.accelerate_due_to_gravity(second)
                
    def check_if_fusion(self):
        for body in self.bodies:
            for otherBody in self.bodies:
                if body != otherBody:
                    distance = math.sqrt((body.position[0] - otherBody.position[0]) ** 2 + (body.position[1] - otherBody.position[1]) ** 2 + (body.position[2] - otherBody.position[2]) ** 2)
                    distanceNeeded = (body.display_size + otherBody.display_size) / 2

                    if distance < distanceNeeded:
                        if body.mass > otherBody.mass:

                            red = ((body.color[0] * body.mass) + (otherBody.color[0] * otherBody.mass)) / (body.mass + otherBody.mass)
                            green = ((body.color[1] * body.mass) + (otherBody.color[1] * otherBody.mass)) / (body.mass + otherBody.mass)
                            blue = ((body.color[2] * body.mass) + (otherBody.color[2] * otherBody.mass)) / (body.mass + otherBody.mass)
                            body.color = (red, green, blue)

                            body.mass += otherBody.mass
                            otherBody.mass = 0.1
                            x = ((body.position[0] * body.mass) + (otherBody.position[0] * otherBody.mass)) / (body.mass + otherBody.mass)
                            y = ((body.position[1] * body.mass) + (otherBody.position[1] * otherBody.mass)) / (body.mass + otherBody.mass)
                            z = ((body.position[2] * body.mass) + (otherBody.position[2] * otherBody.mass)) / (body.mass + otherBody.mass)

                            body.position = (x, y, z)

                            #xVel = (body.velocity.__getitem__(0) + otherBody.velocity.__getitem__(0)) / 2
                            #yVel = (body.velocity.__getitem__(1) + otherBody.velocity.__getitem__(1)) / 2
                            #zVel = (body.velocity.__getitem__(2) + otherBody.velocity.__getitem__(2)) / 2
                            #body.velocity = Vector(xVel, yVel, zVel)
                            body.velocity = Vector(0, 0, 0)

class SolarSystemBody:
    
    #min_display_size = 10
    #display_log_base = 1.3
    display_size_default = 15000000

    def __init__(self, solar_system, mass, position = (0, 0, 0), velocity = (0, 0, 0), color = (0, 0, 0), radius = 1000, display_size = 1):
        self.solar_system = solar_system
        self.mass = mass
        self.position = position
        self.velocity = Vector(*velocity)
        self.color = color
        self.radius = radius
        self.display_size = self.radius * display_size / self.display_size_default
        self.solar_system.add_body(self)

    def move(self):
        self.position = (self.position[0] + self.velocity[0], self.position[1] + self.velocity[1], self.position[2] + self.velocity[2])

    def draw(self):
        if self.mass != 0.1:
            self.solar_system.ax.plot([list(self.position)[0]], [list(self.position)[1]], [list(self.position)[2]], marker = "o", markersize = self.display_size + self.position[0] / 30, color = self.color)
        if not self.solar_system.projection2d:
            if self.mass != 0.1:
                self.solar_system.ax.plot([list(self.position)[0]], [list(self.position)[1]], - self.solar_system.size / 2, marker = "o", markersize = self.display_size / 2, color = (.5, .5, .5))

    def accelerate_due_to_gravity(self, other):
        distance = Vector(*other.position) - Vector(*self.position)
        distance_mag = distance.get_magnitude()
        force_mag = self.mass * other.mass / (distance_mag ** 2)
        force = distance.normalize() * force_mag
        reverse = 1
        for body in self, other:
            acceleration = force / body.mass
            body.velocity += acceleration * reverse
            reverse = -1

solar_system = SolarSystem(size = 400, projection2d = False)


bodies = (SolarSystemBody(solar_system, 300, position = (150, 0, 0), velocity = (0, 0, 0), color = (1, 0, 0), radius = 696340, display_size = 400), SolarSystemBody(solar_system, 300, position = (-150, 0, 0), velocity = (0, 0, 0), color = (0, 0, 1), radius = 696340, display_size = 400))

while True:
    solar_system.calculate_all_body_interactions()
    solar_system.update_all()
    solar_system.check_if_fusion()
    solar_system.draw_all()
    print("1 " + str(bodies[0].velocity) + " - 2 " + str(bodies[1].velocity))