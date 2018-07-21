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
        self.TLSInstrument = cDll.Cornerstone.GetCornerstone(connect)
        
    def setWavelength(self, wavelength, units = cDll.WAVELENGTH_UNITS.NM):
        self.TLSInstrument.setUnits(units)
        self.TLSInstrument.setWavelength(wavelength)
    def getWavelength(self):
        return self.TLSInstrument.getWavelength()
    def setBandpass(self, bandpass):
        self.TLSInstrument.setBandpass(bandpass)
    def getBandpass(self):
        return self.TLSInstrument.getBandpass()
    def setFilter(self, filter):
        self.TLSInstrument.SetFilter(filter)
    def getFilter(self):
        return self.TLSInstrument.getFilter()
    def connect(self):
        return self.TLSInstrument.connect()
        
Mono = TLS(False)
if not Mono.connect():
    print('Please connect device')
else:
    print('Device Connected!')
    print(Mono.getFilter())
    Mono.setWavelength(500)