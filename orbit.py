print(# Orbital Mechanics Simulation

# Physical constants
G = 6.67430e-11       # gravitational constant [m^3 kg^-1 s^-2]
M_earth = 5.972e24    # mass of Earth [kg]

# Initial conditions
x = 7.0e6             # initial x position [m]
y = 0.0               # initial y position [m]
vx = 0.0              # initial x velocity [m/s]
vy = 7546.0           # initial y velocity [m/s]

# Distance from Earth's center
r = (x**2 + y**2)**0.5

# Gravitational acceleration
ax = -G * M_earth * x / r**3
ay = -G * M_earth * y / r**3

# Simulation settings
dt = 1.0          # time step [s]
total_time = 5400  # total simulation time [s]

# Store the trajectory
x_positions = []
y_positions = []

# Simulation loop
for t in range(total_time):

    # Distance from Earth's center
    r = (x**2 + y**2)**0.5

    # Gravitational acceleration
    ax = -G * M_earth * x / r**3
    ay = -G * M_earth * y / r**3

    # Update velocity
    vx = vx + ax * dt
    vy = vy + ay * dt

    # Update position
    x = x + vx * dt
    y = y + vy * dt

#Store corrente position
x_positions.appendi(x)
y_position.apendi(y)

print("Final position:", x, y, "m")
print("Final velocity:", vx, vy, "m/s")

print("Gravitational acceleration:", ax, ay, "m/s^2")
print("Orbital mechanics simulation")
print("Initial position:", x, y, "m")
print("Initial velocity:", vx, vy, "m/s"))