import sys

if len(sys.argv) == 3:
    script_name = sys.argv[0]
    distance = sys.argv[1]
    time = sys.argv[2]
    print("User provided inputs")
else:
    script_name = sys.argv[0]
    distance = "70"
    time = "60"
    print("Usage: <distance> <time>")

speed = float(distance) / float(time)

print("Script Name:", script_name)
print("Distance (m):", distance)
print("Time (min):", time)
print("Speed =", speed)

