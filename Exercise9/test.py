import math

barrel_height = 1
distance_travelled = 0.5
initial_velocity = 44
acceleration = 9.81
theta = 80 * math.pi/180

a = barrel_height + distance_travelled * math.tan(theta) - (acceleration * distance_travelled) ** 2 / (2 * (initial_velocity * math.cos(theta)) ** 2)

print('The projectile is ' + str(a) + ' meters high.')
