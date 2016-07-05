import subprocess
import numpy as np
import matplotlib.pyplot as plt

worlds = np.linspace(1,94,94)
exceptions = np.array([7, 15, 23, 24, 31, 32, 39, 40, 47, 48, 55, 
    56, 63, 64, 71, 72, 79, 80, 87, 88, 89, 90, 91, 92])
worlds = np.delete(worlds, exceptions-1)

def ping_world(world):
    address = "oldschool" + str(world) + ".runescape.com"
    ping_resp = subprocess.Popen(["/bin/ping", "-c1", "-w100", address], stdout=subprocess.PIPE).stdout.read()
    return ping_resp