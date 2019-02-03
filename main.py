from sys import argv
import math

script, units, dist = argv

# Earth's radius (km)
rad = 6371.0

units = units.upper()

# Convert distance to a floating point number
dist = float(dist)

if units == "MI":
    # Convert Earth's radius to miles
    rad = rad / 1.609
elif units != "KM":
    print "ERROR: invalid parameter"

# Calculate circumference
circ = 2.0 * float(math.pi) * rad

# Calculate degrees per km/mi
a = 360.0 / circ

e = a * dist

# Convert degrees to radians
j = e * (math.pi / 180)

# Calculate curvature
curv = rad * (1.0 - math.cos(j))

# Limit decimal places
if curv > 1000:
    rnd = 2
elif curv > 100:
    rnd = 3
elif curv > 10:
    rnd = 4
else:
    rnd = 5

curv = round(curv, rnd)

# Print output
if units == "MI":
    print """
    Distance: %r mi
    Curvature: %f mi
    """ % (dist, curv)
else:
    print """
    Distance: %r km
    Curvature: %f km
    """ % (dist, curv)


