
import sys

course_gpx = sys.argv[1]
route_name = sys.argv[2]

output = [
    f"var {route_name}_lat = [",
    f"var {route_name}_lon = [",
]

fin = open(course_gpx)
for line in fin:
   if "trkpt lat" in line:
       _, lat, lon = line.split()
       output[0] += lat[5:-1] + ", "
       output[1] += lon[5:-2] + ", "
fin.close()

fout = open(f"routes/{route_name}.js", 'w')
fout.write(output[0][:-2] + "];\n")
fout.write(output[1][:-2] + "];\n")
fout.close()

