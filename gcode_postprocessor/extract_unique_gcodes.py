import os,sys

filename = sys.argv[1]

commands = set()

with open(filename, 'r') as f:
    for num, line in enumerate(f):
        line = line.strip()
        if line.startswith(";"):
            continue
        if line == '':
            continue
        command = line.split(' ')[0]
        commands.add(command)

for c in sorted(list(commands)):
    print(c)


# commands that klipper is missing:
# M201 - Set Print Max Acceleration -> MANUAL_STEPPER STEPPER=config_name ACCEL=<accel> ??? or M204 I guess
# M203 - Set Max Feedrate -> MANUAL_STEPPER STEPPER=config_name SPEED=<accel> ???
# M205 for setting jerk and minimum extrude rate and travel or something
