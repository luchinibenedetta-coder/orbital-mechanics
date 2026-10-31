import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import map_coordinates
from matplotlib.animation import FuncAnimation, PillowWriter

# Orbital Mechanics Simulation

# Physical constants
G = 6.67430e-11       # gravitational constant [m^3 kg^-1 s^-2]
M_earth = 5.972e24    # mass of Earth [kg]
earth_radius = 6.371e6    # radius of Earth [m]

# Initial conditions
x = 7.0e6             # initial x position [m]
y = 0.0               # initial y position [m]
vx = 0.0              # initial x velocity [m/s]
vy = 7546.0           # initial y velocity [m/s]
initial_r = (x**2 + y**2)**0.5

# Simulation settings
dt = 1.0          # time step [s]
total_time = 5840  # total simulation time [s]

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
orbital_period = 2*3.14159*(initial_r**3 / (G*M_earth))**0.5

print("Orbital_period:", orbital_period, "s")
print("Orbital_period:", orbital_period / 60, "min")
final_r = (x**2 + y**2)**0.5
specific_energy = (speed**2 / 2) - (G * M_earth / final_r)

print("Specific mechanical energy:", specific_energy, "J/kg")
theoretical_speed = (G * M_earth / initial_r)**0.5
print("Theoretical circular speed:", theoretical_speed, "m/s")
difference = speed - theoretical_speed
print("Speed difference:", difference, "m/s")

# Calculate final altitude
earth_radius = 6.371e6 # Earth radius [m]
altitude = final_r - earth_radius

print("Final altitude:",altitude / 1000, "km")

# Animate the prbit
plt.style.use("dark_background")

# Earth texture: NASA Blue Marble (equirectangular map, longitude -180...180, latitude 90...-90)
texture=plt.imread("earth.jpg")/255.0
tex_h,tex_w,_=texture.shape

# Part of the Earth facing the viewer: the point at the center of the disk
centre_lat=np.radians(25) # latitude of the center [deg -> rad]
center_lon=np.radians(-15) # longitude of the center [deg -> rad]

# Build an image of Earth seen from the side
R = earth_radius / 1000      # Earth radius [km]
n = 400                      # image resolution [pixels]
lim = 1.15 * R               # half-size of the image (leaves room for the atmosphere)
gx, gy = np.meshgrid(np.linspace(-lim, lim, n), np.linspace(-lim, lim, n))
px, py = gx / R, gy / R      # pixel position in Earth radii
rho = np.sqrt(px**2 + py**2)
z = np.sqrt(np.clip(1 - rho**2, 0, 1))   # height of the sphere toward the viewer

# For each pixel of the disk, find the latitude and longitude of the point on the sphere
lat=np.arcsin(np.clip(z*np.sin(center_lat)+py*np.cos(center_lat),-1,1))
lon = center_lon + np.arctan2(px, z * np.cos(center_lat) - py * np.sin(center_lat))
lon = (lon + np.pi) % (2 * np.pi) - np.pi
 
# Look up the texture color for each pixel (bilinear interpolation)
u = (lon + np.pi) / (2 * np.pi) * (tex_w - 1)
v = (np.pi / 2 - lat) / np.pi * (tex_h - 1)
colors = np.dstack([map_coordinates(texture[..., c], [v, u], order=1) for c in range(3)])
 
# Simple shading: sunlight from the upper left, darker toward the edge
light = np.clip(-0.4 * px + 0.3 * py + 0.8 * z, 0, 1)
earth_img = np.zeros((n, n, 4))
earth_img[..., :3] = colors * (0.45 + 0.55 * light)[..., None]
earth_img[..., 3] = rho <= 1
 
# Thin blue atmosphere around the Earth
glow = np.exp(-(rho - 1) / 0.03) * (rho > 1) * 0.6
earth_img[rho > 1, :3] = [0.35, 0.6, 1.0]
earth_img[rho > 1, 3] = glow[rho > 1]
 
fig, ax = plt.subplots(figsize=(5, 5))
ax.imshow(earth_img, extent=[-lim, lim, -lim, lim], origin="lower")
 
# Satellite trajectory (grows as the satellite moves) and satellite
trail, = ax.plot([], [], color="white", alpha=0.6, linewidth=1)
satellite, = ax.plot([], [], "o", color="#ffd84d", markersize=5)
 
ax.set_xlim(-8500, 8500)
ax.set_ylim(-8500, 8500)
ax.set_aspect("equal")
ax.set_xlabel("x position [km]")
ax.set_ylabel("y position [km]")
ax.set_title("Satellite Orbit")
fig.tight_layout()
 
step = 40  # use one position every 40 s of simulated time
 
def update(frame):
    i = frame * step
    trail.set_data([x/1000 for x in x_positions[:i+1]],
                   [y/1000 for y in y_positions[:i+1]])
    satellite.set_data([x_positions[i]/1000], [y_positions[i]/1000])
    return trail, satellite
 
ani = FuncAnimation(fig, update, frames=len(x_positions)//step, interval=30)
 
# Save the animation as a GIF
ani.save("orbit.gif", writer=PillowWriter(fps=25), dpi=80)
