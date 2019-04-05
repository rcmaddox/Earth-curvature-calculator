# Copyright (C) 2019 Cole Maddox

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

# Contact the author at: colemaddox@protonmail.com

# test

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
    print("ERROR: invalid parameter")

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
    print("Distance: %r mi" % (dist))
    print("Curvature %f mi" % (curv))
else:
    print("Distance: %r km" % (dist))
    print("Curvature: %f km" % (curv))
