import matplotlib.pyplot as plt

# Orbital Mechanics Simulation

# Physical constants
G = 6.67430e-11       # gravitational constant [m^3 kg^-1 s^-2]
M_earth = 5.972e24    # mass of Earth [kg]

# Initial conditions
x = 7.0e6             # initial x position [m]
y = 0.0               # initial y position [m]
vx = 0.0              # initial x velocity [m/s]
vy = 7546.0           # initial y velocity [m/s]

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

    # Store current position
    x_positions.append(x)
    y_positions.append(y)

print("Final position:", x, y, "m")
print("Final velocity:", vx, vy, "m/s")

# Calculate final speed
speed = (vx**2 + vy**2)**0.5

print("Final speed:", speed, "m/s")
print("Final speed:", speed / 1000, "km/s")
orbital_period = 2*3.14159*(7000000**3 / (G*M_earth))**0.5

print("Orbital_period:", orbital_period, "s")
print("Orbital_period:", orbital_period / 60, "min")
final_r = (x**2 + y**2)**0.5
specific_energy = (speed**2 / 2) - (G * M_earth / final_r)

print("Specific mechanical energy:", specific_energy, "J/kg")
initial_r = 7.0e6
theoretical_speed = (G * M_earth / initial_r)**0.5
print("Theoretical circular speed:", theoretical_speed, "m/s")
difference = speed - theoretical_speed
print("Speed difference:", difference, "m/s")

# Calculate final attitude
earth_radius = 6.371e6 # Earth radius [m]
altitude = final_r - earth_radius

print("Final altitude:",altitude / 1000, "km")

# Plot the orbit
plt.plot(
    [x/1000 for x in x_positions],
    [y/1000 for y in y_positions],
    label="Satellite trajectory"
)

plt.scatter(
    x_positions[0]/1000,
    y_positions[0]/1000,
    s=50,
    label="Starting position"
)

# Draw satellite
plt.scatter(
    x_positions[-1]/1000,
    y_positions[-1]/1000,
    s=50,
    label="Satellite"
)

# Draw Earth
earth = plt.Circle((0, 0), 6371, alpha=0.5)
plt.gca().add_patch(earth)

plt.xlabel("x position [km]")
plt.ylabel("y position [km]")
plt.title("Satellite Orbit")
plt.axis("equal")
plt.legend()
plt.show()