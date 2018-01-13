from labgraph.utils.serial import *



ports = list_ports()

print(str(ports))

s = Serial(ports[1],9600)
s.open()

while True:

    l =None
    while l == None:
        l = s.read_line()

    print(l)