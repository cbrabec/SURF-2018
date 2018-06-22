# -*- coding: utf-8 -*-
"""
Created on Tue May 15 14:52:37 2018

@author: Lab User
"""
import qcodes as qc
from qcodes.instrument_drivers.stanford_research.SR830 import SR830

def initLockins(lockin1, lockin2, lockin3):
    lockin1 = SR830('lockin1', 'GPIB0::6::INSTR')
    lockin1.phase(0)
    lockin1.reference_source('internal') #Internal source
    lockin1.frequency(7.311)
    lockin1.amplitude(3)
    lockin1.ext_trigger('sine')
    lockin1.input_config('a-b')
    lockin1.input_shield('float')
    lockin1.input_coupling('AC')
    lockin1.notch_filter('off')
    lockin1.sensitivity(0.001)
    lockin1.reserve('low noise')
    lockin1.time_constant(1)
    lockin1.filter_slope(24)
    lockin1.sync_filter('on')
    
    lockin2 = SR830('lockin2', 'GPIB0::7::INSTR')
    lockin2.phase(0)
    lockin2.reference_source('external') 
    lockin2.frequency(7.311)
    lockin2.amplitude(1.000)
    lockin2.ext_trigger('TTL rising')
    lockin2.input_config('a-b')
    lockin2.input_shield('float')
    lockin2.input_coupling('AC')
    lockin2.notch_filter('off')
    lockin2.sensitivity(0.5)
    lockin2.reserve('low noise')
    lockin2.time_constant(1)
    lockin2.filter_slope(24)
    lockin2.sync_filter('on')
    
    lockin3 = SR830('lockin3', 'GPIB0::8::INSTR')
    lockin3.phase(0)
    lockin3.reference_source('external') 
    lockin3.frequency(7.311)
    lockin3.amplitude(1.092)
    lockin3.ext_trigger('TTL rising')
    lockin3.input_config('a-b')
    lockin3.input_shield('float')
    lockin3.input_coupling('AC')
    lockin3.notch_filter('off')
    lockin3.sensitivity(0.05)
    lockin3.reserve('low noise')
    lockin3.time_constant(1)
    lockin3.filter_slope(24)
    lockin3.sync_filter('on')


    