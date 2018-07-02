###############################################################################
#
#                               PPMS Experiment
#                                Yeh Lab
#                               Author : Cole Brabec
#                           06/27/2018
#
###############################################################################
#Operational Description:
#   This program enables automated experiments utilizing the Quantum design
#   Dynacool PPMS, and 3 Stanford Research SR830 Lock-In Amplifiers. The
#   program interfaces with the PPMS using the application extension provided
#   provided by Quantum design. The connection with the PPMS is made through
#   QDInstrument_Server.exe and Multivu. Both Multivue and QD_instrument
#   must be running on the ppms computer before this script is run. 
#   The script takes the input experiment parameters, and runs through
#   each experiment, outputting the data in a comma-seperated-value (CSV)
#   format. The user is able to specify whether they desire a temperatureSweep
#   or Magnetic field sweep.
#   
#User Interface:
#   When the script is run, the user is prompted for the name of the input file
#   The input file must be organized in a csv format: each line contains 8
#   values seperated by a comma and space, with the line terminating in a 
#   newline character. 
#   The lines must contain the following values:
#   1). String - either 'temperatureSweep' or 'magneticFieldSweep'
#   2). A string that is the name of the output file for the sweep
#   
#
#   Remaining arguments for temperature sweep:
#   3). The starting temperature in Kelvin
#   4). The end temperature in Kelvin
#   5). The temperature interval between each data point in Kelvin
#   6). The rate to move between each temperature point in Kelvin/minute
#   7). Magnetic field strength in Oe
#   8). Magnetic field ramping rate in Oe/sec
#
#   Remaing arguments for magnetic field sweep:
#   3). The starting Magntic Field in Oe
#   4). The end Magnetic Field in Oe
#   5). The Magnetic field interval between each data point in Oe
#   6). The rate to move between each field point in Oe/second
#   7). Temperature in Kelvin
#   8). Temperature ramping rate in Kelvin/minute
#
#   The output file contains 12 values in CSV format - values are seperated by
#   a space and a comma, with each line terminated in a newline character.
#   1). Date and Time
#   2). PPMS Temperature
#   3). PPMS Magnetic Field
#
#   4). Lockin1 X
#   5). Lockin1 Y
#   6). Lockin1 R
#
#   7). Lockin2 X
#   8). Lockin2 Y
#   9). Lockin2 R
#
#   10). Lockin3 X
#   11). Lockin3 Y
#   12). Lockin3 R
#
#Input:
#   1) Input from a file outlining experiments
#   2) Console input indicating name of input file
#   3) Magnetic field and Temperature from ppms
#   3) X, Y, and R from SR830's
#
#Output:
#   1) Commands to ppms
#   2) Commands to SR830's
#   3) Output File
#
#Global Variables:
#   None
#
#Limitations:
#   1). SR830 config settings must be changed by editing code
#   2). IP address must be changed by editing code
#   3). A nested for loop for temp and magnetic field sweep is currently not
#       supported for a single experiment. Instead each experiment must be one
#       of the loop.
#
#Known Bugs with fixes:
#   1). Bug: Error connecting to ppms
#       fixes: Ensure Multivue is open on PPMS computer
#              Ensure QDInstrument_Server.exe is running
#              Ensure ppms in initialized with correct address
#   2). Bug: Error connecting to SR830
#       fixes: Ensure SR830's are on
#              Ensure SR830's usb's are connected
#              Ensure SR830 addresses are set correctly
#
#
#
#Usage instructions:
#1: Set up input file
#2: Open Multivue on PPMS computer
#3. Run QDInstrument_Server.exe on PPMS computer
#4. Turn on SR830 Amplifiers
#5. Set SR830 amplifiers to correct address
#6. Run script, input name if input file
#7. Let the experiment run
#
#For any bugs or questions contact Cole Brabec:
#Phone #: (913)609 - 3846
#Email: cbrabec@caltech.edu
#
#Revision History:
#   06/27/2018 Cole Brabec - Inital Revision
#                            Added SR830 Interface
#                            Added PPMS Interface
#                            Implemented Temp and Mag sweeps
#
from qcodes.instrument_drivers.stanford_research.SR830 import SR830
#from LockinInit import initLockins
from sweep import temperatureSweep
from sweep import magFieldSweep
from ppms import Dynacool
from fileParser import lineParse

#This ip address is the ip4 address of the ppms computer
ppms = Dynacool('131.215.107.158')
print('connected')

#These are the addresses the SR830's must be set to
lockin1 = SR830('lockin1', 'GPIB0::6::INSTR')
lockin2 = SR830('lockin2', 'GPIB0::7::INSTR')
lockin3 = SR830('lockin3', 'GPIB0::8::INSTR')

#This function sets the lockin config settings
#initLockins(lockin1, lockin2, lockin3)

#prompt the user for console input
inputFile = input("Input name of input File: ")
f = open(inputFile, 'r')
sleepTime = lockin1.time_constant.get() * 10
time = 0
for line in f:
    sweepArgs = lineParse(line)
    npoints = (sweepArgs[3] - sweepArgs[2])/sweepArgs[4]
    if sweepArgs[0] == 'temperatureSweep':
        time += (sleepTime + (sweepArgs[4]/sweepArgs[5]) /60) * npoints
    else:
        time += (sleepTime + (sweepArgs[4]/sweepArgs[5])) * npoints
time = time / 3600
print("Estimeated time for experiment in hours: %d" % time)
inputCommand = input("Would you like to perform experiment (y/n)?: ")

f.close()

f = open(inputFile, 'r')
if inputCommand == 'y' or inputCommand == 'Y':
    for line in inputFile:
        sweepArgs = lineParse(line)
        if sweepArgs[0] == 'temperatureSweep':
            temperatureSweep(ppms, lockin1, lockin2, lockin3, *sweepArgs[1:], sleepTime)
        else:
            magFieldSweep(ppms, lockin1, lockin2, lockin3, *sweepArgs[1:], sleepTime)

