from fileParser import lineParse


inputFile = input("Input name of input File: ")
inputFile = open(inputFile, 'r')
sleepTime = 10
time = 0
for line in inputFile:
    sweepArgs = lineParse(line)
    print(sweepArgs)
    npoints = (sweepArgs[3] - sweepArgs[2])/sweepArgs[4]
    print(npoints)
    if sweepArgs[0] == 'temperatureSweep':
        time += (sleepTime + (sweepArgs[4]/sweepArgs[5]) /60) * npoints
    else:
        time += (sleepTime + (sweepArgs[4]/sweepArgs[5])) * npoints
print(time)
time = time / 3600
print("Estimeated time for experiment in hours: %d" % time)
inputCommand = input("Would you like to perform experiment (y/n)?: ")