import qcodes as qc
from time import sleep
from qcodes.instrument_drivers.stanford_research.SR830 import SR830


sr = SR830('lockin', 'GPIB0::8::INSTR')
