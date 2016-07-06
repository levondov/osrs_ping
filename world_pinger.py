import subprocess
import numpy as np
import time

worlds = np.linspace(1,94,94)
exceptions = np.array([7, 15, 23, 24, 31, 32, 39, 40, 47, 48, 55, 
    56, 63, 64, 71, 72, 79, 80, 87, 88, 89, 90, 91, 92])
worlds = np.delete(worlds, exceptions-1)

def ping_world(world):
    # pings a world and returns a string of min/avg/max/mdev pings
    world = str(world)
    if world[-2:] == '.0':
	world = world[0:len(world)-2]
    address = "oldschool" + world + ".runescape.com"
    ping_resp = subprocess.Popen(["/bin/ping", "-c1", "-w100", address], stdout=subprocess.PIPE)
    return ping_resp.communicate()[0].split('\n')[5][4:]

def main():
    pings = np.zeros(len(worlds))
    f = open('test.txt', 'w')
    # grab pings and write to file
    for world,ping in zip(worlds, pings):
        ping = ping_world(int(world))
        temp = "World " + str(world)[0:-2] + ": " + ping + " <br> "
        f.write(temp)
    f.close()

while True:
    print 'checking pings....'
    main()
    for i in range(0,16):
	print 'time till next check: ' + str(15-i)
	time.sleep(1)
        
