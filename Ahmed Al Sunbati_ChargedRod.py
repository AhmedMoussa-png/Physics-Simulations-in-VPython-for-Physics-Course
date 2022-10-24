from vpython import *
#Web VPython 3.2
sf = 0.002 # Scale factor for electric field arrow.
oofpez = 9e9 # Electric constant.
Qtot = 1e-9 # Total charge.
L = 1.0 # Length of rod.
N = 10.0 # Number of slices the rod will be made of.
dy = L/N # Length of a slice.

# Create a list of slices as point charges.
slices = [] # An empty list.
i = 0
y0 = -L/2 + dy/2 # Center of bottom slice.
while i < N:
    # Create a single point charge.
    a = sphere(pos=vector(0,y0+i*dy,0), radius=dy/2.0, color=color.red, q=Qtot/N)
    # Add point charge to list of slices.
    slices.append(a)
    i = i + 1 # Move to the next slice.
    
    
# Create a list of observation locations.
observations = [] # An empty list.

yobs_list = [-0.75,-0.5,-0.25,0.0,0.25,0.5,0.75] # Height of observation locations.
for yobs in yobs_list:
    
    R = 0.15 # Radius of circle of observations.
    dtheta = pi/6.0 # Angle between observation locations.
    theta = 0
    while (theta < 2.0*pi):
        a = vector(R*cos(theta), yobs, R*sin(theta))
        observations.append(a)
        theta = theta + dtheta

# You can add to the list of observation locations here!



# Loop over ALL observation locations to calculate E at each location.

for r_obs in observations:
    # Calculate E from each slice.
    E_net = vector(0,0,0)
    for s in slices:
        r = r_obs - s.pos # Relative position vector.
        rhat = r/mag(r) # Unit vector.
        E = (oofpez * s.q / mag(r)**2) * rhat # Calculate E for this slice.
        E_net = E_net + E # Add this E to the total E.
        
    arrow(pos=r_obs, axis=sf*E_net)
    
# Print the most recent electric field vector for reference.
print(E_net)