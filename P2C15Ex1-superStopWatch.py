#! python

import time

print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')

input()
print("Timer started....")
startTime = time.time()
lastTime = startTime

lapCount = 1

try:
    while True:
        input()
        currentTime = time.time()
        lapTime = round(currentTime - lastTime, 2)
        totalTime = round(currentTime - startTime, 2)
        print("Lap %s: Total time - %s, Lap time - %s" % (lapCount, totalTime, lapTime))
        lastTime = currentTime
        lapCount += 1
except KeyboardInterrupt:
    totalTime = round(time.time() - startTime, 2)
    print("\n\nTotal Laps: %s and Total time (till quit): %s" % (lapCount, totalTime))
    print("Done")
