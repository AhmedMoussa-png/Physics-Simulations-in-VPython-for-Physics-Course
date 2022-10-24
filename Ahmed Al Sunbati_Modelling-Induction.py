from vpython import *
#Web VPython 3.2

oofpez = 9e9
muzofp = 1e-7 # *exactly*

def GetFluxThrough(point1,point2,point3,sources):

    dx = 0.01
    

    xhat = point2-point1
    yhat = point3-point1
    xhat = xhat.hat
    yhat = yhat.hat
    

    nhat = cross(xhat,yhat)
    

    center = (point2+point3)/2
    

    if (dot(nhat,center) < 0):
        nhat = -nhat
    
    flux = 0
    
    point = point1
    start_point = point1
    while (dot(point-point1,xhat) <= mag(point2-point1)):
        point = start_point
        while (dot(point-point1,yhat) <= mag(point3-point1)):
            for source in sources:
                r = point-(source.pos+0.5*source.axis)
                B = muzofp*source.current*cross(source.axis,r.hat)/mag(r)**2
                flux = flux + dot(B,nhat)*dx**2
            point = point + dx*yhat
        start_point = start_point + dx*xhat
    
    return flux


primary = []
primary.append( cylinder(pos=vector(-3,0,-0.5), radius=0.05, axis=vector(1.0,0,0), 
                color=color.blue, current=1.0, opacity=0.5 ))
primary.append( cylinder(pos=vector(-2,0,0.5), radius=0.05, axis=vector(-1.0,0,0), 
                color=color.blue, current=1.0, opacity=0.5 ))
primary.append( cylinder(pos=vector(-3,0,0.5), radius=0.05, axis=vector(0,0,-1.0), 
                color=color.blue, current=1.0, opacity=0.5 ))
primary.append( cylinder(pos=vector(-2,0,-0.5), radius=0.05, axis=vector(0,0,1.0), 
                color=color.blue, current=1.0, opacity=0.5 ))

primary_arrows = []
current_scale = 0.25
for source in primary:
    primary_arrows.append(arrow(pos=source.pos+0.5*source.axis, axis=source.axis*source.current*current_scale,
                        color=color.white))


RightFront = vector(1,0,1)
LeftFront = vector(-1,0,1)
RightBack = vector(1,0,-1)
LeftBack = LeftFront + (RightBack-RightFront)
secondary = curve( pos=(RightFront, LeftFront, LeftBack, RightBack, RightFront), 
                  color=color.white)

secondary_arrows = []
efield_scale = 5e7
for i in range(0,secondary.npoints-1):
    my_pos = (secondary.point(i).pos+secondary.point(i+1).pos)/2
    my_axis = secondary.point(i).pos-secondary.point(i+1).pos
    secondary_arrows.append(arrow(pos=my_pos, axis=my_axis*0*efield_scale,
                        color=color.red))


prev_flux = GetFluxThrough(RightBack, LeftFront, RightFront, primary)


flux_display = gdisplay()
flux_graph = gcurve(color=color.red, label="magnetic flux" )
efield_display = gdisplay()
efield_graph = gcurve(color=color.red, label="induced electric field")


magnetic_field_points = []

primary_center = vector(0,0,0)
for source in primary:
    primary_center = primary_center + source.pos/len(primary)
label(pos=primary_center, text='primary coil', box=False, opacity=0)

secondary_center = 0.5*(LeftBack+RightFront)
label(pos=secondary_center, text='secondary coil', box=False, opacity=0)

field_center = 0.5*(primary_center+secondary_center)
R = mag(primary_center-secondary_center)*0.5
B_scale = 6e7
dtheta = pi/12
for theta in range(-pi/4,pi/4,dtheta): # Adjust this angle range as necessary.
    locn = field_center + vector(R*cos(theta),R*sin(theta),0)
    magnetic_field_points.append(arrow( pos=locn,
                                axis=vector(0,0,0), color=color.blue ))


t = 0
dt = 0.01
period = 1.0
while (True):
    rate(100)
    t = t + dt
    

    curr = 1.0*cos(2*pi*t/period)
    for i in range(0,len(primary)):
        primary[i].current = curr
        primary_arrows[i].axis = primary[i].axis*primary[i].current*current_scale


    for point in magnetic_field_points:
        point.axis = vector(0,0,0)
        for source in primary:
            r = point.pos-(source.pos+0.5*source.axis)
            point.axis = point.axis + muzofp*source.current*cross(source.axis,r.hat)/mag(r)**2*B_scale


    flux = GetFluxThrough(RightBack, LeftFront, RightFront, primary)
    flux_graph.plot(pos=(t,flux))

    emf = -(flux-prev_flux)/dt

    prev_flux = flux
    secondary_length = 0
    for i in range(0,secondary.npoints-1):
        secondary_length = secondary_length + mag(secondary.point(i).pos-secondary.point(i+1).pos)
    E_mag = emf/secondary_length
    efield_graph.plot(pos=(t,E_mag))
    for i in range(0,secondary.npoints-1):
        secondary_arrows[i].axis = (secondary.point(i).pos-secondary.point(i+1).pos)*E_mag*efield_scale
        print(secondary_arrows[i].axis)
