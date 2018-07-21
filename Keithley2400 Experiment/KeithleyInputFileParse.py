# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 14:39:40 2018

@author: Cole
"""
def keithleyInputParse(fileName):
    commands = []
    inputFile = open(fileName,'r')
    for line in inputFile:
        commands.append(line)
    
    for i, cmd in enumerate(commands):
        commands[i] = list(map(float, cmd.rsplit(sep = ' ')))
    
    inputFile.close()
    return commands
