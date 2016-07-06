import subprocess
import numpy as np
import time

worlds = np.linspace(1,94,94)
exceptions = np.array([7, 15, 23, 24, 31, 32, 39, 40, 47, 48, 55, 
    56, 63, 64, 71, 72, 79, 80, 87, 88, 89, 90, 91, 92])
worlds = np.delete(worlds, exceptions-1)
world_types = (1,2,2,2,2,2,1,2,2,2,2,3,2,1,3,2,2,2,3,2,4,1,2,2,2,2,2,2,1,2,4,2,2,2,2, 
    2,3,2,2,2,2,2,2,2,3,2,2,3,2,2,2,2,2,2,2,2,2,3,2,3,2,3,1,1,1,1,1,2,1,1)

def ping_world(world):
    # pings a world and returns a string of min/avg/max/mdev pings
    world = str(world)
    if world[-2:] == '.0':
	world = world[0:len(world)-2]
    address = "oldschool" + world + ".runescape.com"
    ping_resp = subprocess.Popen(["/bin/ping", "-c1", "-w100", address], stdout=subprocess.PIPE)
    return float(ping_resp.communicate()[0].split('\n')[5][4:].split('/')[4])

def main():
    pings = ['None']*len(worlds)
    world_icon = ['None']*len(worlds)
    world_best = ['None']*len(worlds)
    total = ['None']*len(worlds)

    # setup html code for world icons
    for i,world in enumerate(worlds):
        # grab appropriate icons for each world
        if world_types[i] == 1:
            world_icon[i] = "<img src=""images/f2p_icon.png""> "
        elif world_types[i] == 2:
            world_icon[i] = "<img src=""images/p2p_icon.png""> "
        elif world_types[i] == 3:
            world_icon[i] = "<img src=""images/p2p_icon.png""> (DMM) "
        else: # = 4
            world_icon[i] = "<img src=""images/p2p_icon.png""> (PVP) "
        
    # grab pings for each world
    for i,world in enumerate(worlds):
        pings[i] = ping_world(int(world))
        
    # find best worlds, best = green, next 9 best = yellow, rest = red
    temp = np.argsort(pings)
    for i,world in enumerate(worlds):
        if i < 10:
            world_best[temp[i]] = "<font color=""green"">" + str(pings[temp[i]]) + "</font>"
        else:
            world_best[temp[i]] = "<font color=""red"">" + str(pings[temp[i]]) + "</font>"
    
    # finally put it all together
    for i,world in enumerate(worlds):
        total[i] = world_icon[i] + "World " + str(world)[0:-2] + ": " + world_best[i] + " ms <br>"

    # write to text file
    f = open('test.txt', 'w')
    for each_world in total:
	f.write(each_world)
    f.close()

while True:
    print 'checking pings....'
    start_time = time.time()
    main()
    print 'finished in ' + str(time.time() - start_time)[0:3] + ' seconds '
        
