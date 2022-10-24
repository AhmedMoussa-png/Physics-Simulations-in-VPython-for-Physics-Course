from vpython import *
#Web VPython 3.2
oofpez = 9e9
muzofp = 1e-7 
B_scale = 6e6 


sources = []
sources.append( cylinder(pos=vector(-0.5,0,0.5), radius=0.05, axis=vector(0,0,-1.0), 
                color=color.green, current=1.0, opacity=0.5 ))
#sources.append( cylinder(pos=vector(0.5,0,-0.5), radius=0.05, axis=vector(0,0,1.0), 
                #color=color.green, current=1.0, opacity=0.5 ))
#sources.append( cylinder(pos=vector(-0.5,0,-0.5), radius=0.05, axis=vector(1.0,0,0), 
                #color=color.green, current=1.0, opacity=0.5 ))
#sources.append( cylinder(pos=vector(0.5,0,0.5), radius=0.05, axis=vector(-1.0,0,0), 
                #color=color.green, current=1.0, opacity=0.5 ))


current_arrows = []
current_scale = 0.25
for source in sources:
    current_arrows.append(arrow(pos=source.pos+0.5*source.axis, axis=source.axis*source.current*current_scale,
                        color=color.white))


magnetic_field_points = []

sources_center = vector(0,0,0)
sources_width = 0
for source in sources:
    sources_center = sources_center + (source.pos+source.axis/2)/len(sources)
    sources_width = max(sources_width,source.length)


R = 1.5*sources_width
dtheta = pi/12
for theta in range(0,2*pi,dtheta):
    locn = sources_center + vector(R*cos(theta),R*sin(theta),0)
    magnetic_field_points.append(arrow( pos=locn,
                                axis=vector(0,0,0), color=color.blue ))
R = 1.2*sources_width
dtheta = pi/12
for theta in range(0,2*pi,dtheta):
    locn = sources_center + vector(R*cos(theta),R*sin(theta),0)
    magnetic_field_points.append(arrow( pos=locn,
                                axis=vector(0,0,0), color=color.blue ))
R = 1.8*sources_width
dtheta = pi/12
for theta in range(0,2*pi,dtheta):
    locn = sources_center + vector(R*cos(theta),R*sin(theta),0)
    magnetic_field_points.append(arrow( pos=locn,
                                axis=vector(0,0,0), color=color.blue ))
#R = 1.00*sources_width
#dtheta = pi/12
#for theta in range(0,2*pi,dtheta):
#    locn = sources_center + vector(R*cos(theta),R*sin(theta),0)
#    magnetic_field_points.append(arrow( pos=locn,
#                                axis=vector(0,0,0), color=color.blue ))


t = 0
dt = 0.01
period = 1.0
while (True):
    rate(100)
    t = t + dt
    

#    curr = 1.0*cos(2*pi*t/period)
#    for i in range(0,len(sources)):
#        sources[i].current = curr
#        current_arrows[i].axis = sources[i].axis*sources[i].current*current_scale


    for point in magnetic_field_points:
        point.axis = vector(0,0,0)
        for source in sources:
            r = point.pos-(source.pos+0.5*source.axis)
            point.axis = point.axis + muzofp*source.current*cross(source.axis,r.hat)/mag(r)**2*B_scale

