# -*- coding: utf-8 -*-
from time import sleep
import numpy as np
import qcodes as qc
from qcodes.instrument_drivers.stanford_research.SR830 import SR830
from LockinInit import initLockins
from qcodes.dataset.measurements import Measurement
from qcodes.dataset.plotting import plot_by_id

loc_provider = qc.data.location.FormatLocation(fmt='data/{date}/#{counter}_{name}_{time}')
qc.data.data_set.DataSet.location_provider=loc_provider

lockin1 = SR830('lockin1', 'GPIB0::6::INSTR')
lockin2 = SR830('lockin2', 'GPIB0::7::INSTR')
lockin3 = SR830('lockin3', 'GPIB0::8::INSTR')

initLockins(lockin1, lockin2, lockin3)

station = qc.Station(lockin1, lockin2, lockin3)
qc.new_experiment(name='Temperature Sweep', sample_name='test_sample')


temps = np.linspace[300, 0, 600]
tempSweep = qc.loop(temps[0, 599], delay = 5).each(lockin1.ch1, lockin2.ch1, lockin3.ch1)
data = tempSweep.get_data_set(name='tempsweep')
