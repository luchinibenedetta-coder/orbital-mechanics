# Orbital Mechanics Simulation
A numerical simulation of satellite orbital motion around Earth using Python.

## Objective
The objective of this project is to simulate the motion of a satellite orbiting Earth under the influence of gravity and to compare the numerical results with theoretical predictions.

## Physical Model
The satellite's mass is assumed negligible compared to Earth's mass, so its effect on Earth's gravitational field is neglected. The gravitational acceleration is calculated from Newton's law of universal gravitation:
a = −GM r/r³
where G is the gravitational constant, M is the mass of Earth, and r is the distance between the satellite and the center of Earth.

## Numerical Method
The equations of motion are integrated numerically using the Euler method with a fixed time step of 1 second. At each time step, the gravitational acceleration is calculated from the satellite's current position. The velocity is then updated, followed by the position.

## Initial Conditions
| Parameter | Value |
|---|---:|
| Initial distance from Earth's center | 7000 km |
| Initial velocity | 7546 m/s (tangential) |
| Time step | 1 s |
| Simulation time | 5400 s |

## Results
The simulation produces a nearly circular orbit with the following values:
| Quantity | Result |
|---|---:|
| Final speed | 7544.18 m/s |
| Theoretical circular speed | 7545.95 m/s |
| Speed difference | -1.77 m/s |
| Theoretical orbital period | 97.14 min |
| Final altitude | 630.69 km |
| Specific mechanical energy | -2.85 × 10⁷ J/kg |
The simulated final speed differs from the theoretical circular speed by only about 1.77 m/s, indicating that the numerical simulation remains very close to the expected circular orbit. The negative specific mechanical energy confirms that the satellite remains gravitationally bound to Earth throughout the simulated orbit.

## Limitations
- The simulation assumes a two-body system consisting of Earth and the satellite.
- Earth's gravitational field is modeled as spherically symmetric, with constant mass and radius.
- Atmospheric drag, Earth's rotation, and other perturbing forces are not included.
- The numerical integration uses a fixed time step of 1 second.

## Visualization
The plot below shows the simulated satellite trajectory, together with the initial and final satellite positions and the Earth.

![Satellite's orbit](orbit.png)

## Future Improvements
- Improve the numerical integration method.
- Simulate different types of orbits, including elliptical and escape trajectories.
- Compare numerical results with analytical predictions.
- Investigate numerical errors and their dependence on the time step.