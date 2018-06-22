from time import sleep, time
import numpy as np
import qcodes as qc
from qcodes import (Instrument, VisaInstrument,
                    ManualParameter, MultiParameter,
                    validators as vals)
from qcodes.instrument.channel import InstrumentChannel

class SR830(qc.VisaInstrument):
    def __init__(self, name, address, **kwargs):
        super().__init__(name, address, terminator = '\r', **kwargs)
        
        self.add_parameter('Phase Shift', 
                           unit = 'degrees',
                           label = 'Phase Shift',
                           set_cmd = 'PHAS {:03.2f}',
                           get_cmd = 'PHAS?',
                           get_parser = float)
        self.add_parameter('reference',
                           docstring = 'Selects Reference Source',
                           val_mapping = {'internal': 1, 'external': 0},
                           set_cmd = 'FMOD {0:d}',
                           get_cmd = 'FMOD?',
                           get_parser = int)
        self.add_parameter('frequency',
                           unit = 'Hz',
                           label = 'Reference Frequency',
                           set_cmd = 'FREQ {0:.5f}',
                           get_cmd = 'FREQ?',
                           get_parser = float)
        self.add_parameter('trigger',
                           docstring = 'Reference trigger mode',
                           val_mappint = {'zero' : 0, 'rising edge' : 1, 'falling edge' : 2},
                           set_cmd = 'RSLP {0:d}',
                           get_cmd = 'RSLP?',
                           get_parser = int)
        self.add_parameter('harmonic',
                           unit = 'harmonic',
                           lable = 'Detection Harmonic',
                           set_cmd = 'HARM {0:d}',
                           get_cmd = 'HARM?',
                           get_parser = int)
        self.add_parameter('sin amplitude',
                           unit = 'V',
                           label = 'Sine Output Amplitude',
                           set_cmd = 'SLVL {0:1.3f}',
                           get_cmd = 'SLVL?',
                           get_parser = float)
        self.add_parameter('input config',
                           docstring = 'Input Configuration',
                           val_mapping = {'A': 0, 'A-B': 1, 'I(10 MOhm)': 2, 'I(100MOhm)': 3},
                           set_cmd = 'ISRC {0:d}',
                           get_cmd = 'ISRC?',
                           get_parser = int)
        self.add_parameter('grounding',
                           docstring = 'Input Shield Grounding',
                           val_mapping = {'Float' : 0, 'Ground' : 1},
                           set_cmd = 'IGND {0:d}',
                           get_cmd = 'IGND?',
                           get_parser = int)
        self.add_parameter('coupling',
                           docstring = 'Input Coupling',
                           val_mapping = {'AC' : 0, 'DC' : 1},
                           set_cmd = 'ICPL {0:d}',
                           get_cmd = 'ICPL?',
                           get_parser = int)
        self.add_parameter('filter status',
                           docstring = 'Input Line Filter Status',
                           val_mapping = {'Out/No Filters' : 0, 'Line Notch In' : 1, 
                                          '2xLine Notch In' : 2, 'Both Notch Filters In' : 3},
                            set_cmd = 'ILIN {0:d}',
                            get_cmd = 'ILIN?',
                            get_parser = int)
        self.add_parameter('sensitivity',
                           docstring = 'Sensitivity Level',
                           set_cmd = 'SENS {0:d}',
                           get_cmd = 'SENS',
                           get_parser = int)
        self.add_parameter('reserve mode',
                           docstring = 'Reserve Mode',
                           val_mapping = {'High Reserve' : 0, ' Normal' : 1, 'Low Noise' : 2},
                           set_cmd = 'RMOD {0:d}',
                           get_cmd = 'RMOD?',
                           get_parser = int)
        self.add_parameter('time constant',
                           docstring = 'Time Constant Setting',
                           set_cmd = 'OFLT {0:d}',
                           get_cmd = 'OFLT',
                           get_parser = int)
        self.add_parameter('filter slope',
                           docstring = 'Low Pass Filter Slope',
                           val_mapping = {'6 dB' : 0, '12 dB' : 1, '18 dB' : 2, '24 dB' : 3},
                           set_cmd = 'OFSL {0:d}',
                           get_cmd = 'OFSL?',
                           get_parser = int)
        self.add_parameter('sync filter',
                           docstring = 'Sync Filtering Setting',
                           val_mapping = {'Off' : 0, 'On' : 1},
                           set_cmd = 'SYNC {0:d}',
                           get_cmd = 'SYNC?',
                           get_parser = int)
        
        self.add_parameter('display',
                           docstring = 'Display Settings',
                           set_cmd = 'DDEF {}, {}, {}'.format({'0:d'},{'0:d'},{'0:d'}),
                           get_cmd = 'DDEF?',
                           )