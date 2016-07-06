import subprocess
import numpy as np

worlds = np.linspace(1,94,94)
exceptions = np.array([7, 15, 23, 24, 31, 32, 39, 40, 47, 48, 55, 
    56, 63, 64, 71, 72, 79, 80, 87, 88, 89, 90, 91, 92])
worlds = np.delete(worlds, exceptions-1)
pings = np.zeros(len(worlds))

def ping_world(world):
    # pings a world and returns a string of min/avg/max/mdev pings
    address = "oldschool" + str(world) + ".runescape.com"
    ping_resp = subprocess.Popen(["/bin/ping", "-c1", "-w100", address], stdout=subprocess.PIPE)
    return ping_resp.communicate()[0].split('\n')[5][4:]

def main():
    # grab pings
    #for world,ping in zip(worlds, pings):
    #    ping = str(ping_world(world))
    
    # write to text file
    f = open('test.txt', 'w')
    for world,ping in zip(worlds,pings):
        temp = "World " + str(world)[0:2] + ": " + str(ping) + " \n "
        f.write(temp)
        print temp
    f.close()
    
main()
        