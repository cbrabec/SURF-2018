# -*- coding: utf-8 -*-
import clr

try:
    clr.AddReference('Cornerstone')
except:
    if clr.FindAssembly('Cornerstone') is None:
        print('Could not find Cornerstone.dll')
    else:
        print('Found Cornerstone.dll at {}'.format(clr.FindAssembly('Cornerstone')))
        print('Try right-clicking the .dll, selecting "Properties", and then clicking "Unblock"')
        
        
import CornerstoneDll as cDll

class TLS:
    def __init__(self, connect):
        self.TLSInstrument = cDll.Cornerstone(connect)
        
    def setWavelength(self, units, wavelength):
        self.TLSInstrument.setWavelength(units)
        self.TLSInstrument.setWavelength(wavelength)
test = TLS(False)
test.setWavelength(1)