import pybryt
from lecture import pybryt_reference
density = 1.2       # units of kg/m^3
ball_radius = 0.11  # units of m
C_D = 0.2           # drag coefficient

v = 50.8            # m/s (fastest recorded speed of football)
pi = 3.1415926

# Uncomment, fix, and complete the following lines.
A = pi*ball_radius**2  # cross sectional area of a sphere
F_d = 0.5*C_D*density*A*v**2
with pybryt.check(pybryt_reference(1, 3)):
    A, F_d

