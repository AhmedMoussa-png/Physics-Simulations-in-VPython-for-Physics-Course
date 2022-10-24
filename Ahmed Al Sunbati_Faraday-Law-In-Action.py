from vpython import *
#Web VPython 3.2
MagnetAxis = vector(1,0,0) # Orientation of the magnet, in (x,y,z) components.

def B(time):
  Bx = cos(time)
  By = 0
  Bz = 0

  return vector(Bx,By,Bz) 



ObservationPoints = [] 
R = 1 
for theta in range(0,2*pi,0.5):
  ObservationPoints.append(R*vector(0,cos(theta),sin(theta)))
  

  # ObservationPoints.append(R*vector(0.1,cos(theta),sin(theta)))
  # ObservationPoints.append(0.75*R*vector(0.2,cos(theta),sin(theta)))
  # ObservationPoints.append(2*R*vector(-0.1,cos(theta),sin(theta)))
  # ObservationPoints.append(R*vector(-0.2,cos(theta),sin(theta)))



MagneticField = arrow( pos=vector(0,0,0), axis=B(0), visible=True )

ElectricFieldVectors = [] 
for Point in ObservationPoints:
  ElectricFieldVectors.append(arrow(pos=Point,axis=vector(0,0,0),color=color.yellow))


dt = 0.01 
time = 0 
ScaleFactor = 1.2e-1

print('white  = magnetic field')
print('yellow = electric field')

def PlayPause(b):
  global dt, remember_dt
  if b.text == 'Pause':
    remember_dt = dt
    dt = 0
    b.text = 'Play'
  else:
    dt = remember_dt
    b.text = 'Pause'
  return

PauseButton = button(text='Pause', bind=PlayPause)

while (True): 
  rate(0.5/dt) 
  if PauseButton.text == 'Pause':
    MagneticField.axis = B(time)
    # Update electric field vectors.
    BDeriv = (B(time+dt)-B(time-dt))/(2*dt)
    for FieldHere in ElectricFieldVectors:
      rhat = hat(FieldHere.pos)
      Ehat = rhat.cross(hat(BDeriv))
      # FieldHere.axis = ScaleFactor*mag(BDeriv) * (Magnet.size.y/2)**2 * 2 / mag(FieldHere.pos) * Ehat
      FieldHere.axis = ScaleFactor*mag(BDeriv) * 2 / mag(FieldHere.pos) * Ehat
    time = time + dt 
