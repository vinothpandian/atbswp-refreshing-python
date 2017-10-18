#! python

import time, sys, subprocess, os

# FOLDER_NAME = "P2C15"
# os.makedirs(FOLDER_NAME, exist_ok=True)
# os.chdir("P2C15")

if len(sys.argv) == 2:
    timer = int(sys.argv[1])
else:
    print("Run the program as P2C15Ex3-simpleCountDown.py [Time in Seconds]")
    sys.exit()

startTime = time.time()

while timer > 0:
    print("%s sec left.." % timer)
    timer -= 1
    time.sleep(1)

# Only for windows
subprocess.Popen(["start", ".\\P2C15\\alarm.wav"], shell=True)
