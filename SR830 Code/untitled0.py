# -*- coding: utf-8 -*-
import qcodes as qc
from qcodes.instrument_drivers.stanford_research.SR830 import SR830
from qcodes.tests.instrument_mocks import DummyInstrument

lockin1 = SR830('lockin1', 'GPIB0::6::INSTR')
lockin2 = SR830('lockin2', 'GPIB0::7::INSTR')
lockin3 = SR830('lockin3', 'GPIB0::8::INSTR')

PPMS    = DummyInstrument(name = 'PPMS', gates = ['temp', 'magnetic field'])

station = qc.Station(lockin1, lockin2, lockin3, PPMS)