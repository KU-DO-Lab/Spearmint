from Drivers.daq_driver import Daq
from qcodes.instrument_drivers.Lakeshore.Model_372 import Model_372
from qcodes.instrument_drivers.american_magnetics.AMI430 import AMI430
from qcodes.instrument_drivers.stanford_research.SR860 import SR860
from qcodes.instrument_drivers.stanford_research.SR830 import SR830
from qcodes.instrument_drivers.tektronix.Keithley_2450 import Keithley2450
from qcodes.instrument_drivers.Lakeshore import LakeshoreModel336
from Drivers.M4G import M4G
# To add an instrument, import the driver then add it to our instrument
# dictionary with the name as the key, and the class as the value
import pyvisa


LOCAL_INSTRUMENTS = {'NI DAQ': Daq,
                     'Model_372': Model_372,
                     'AMI430': AMI430,
                     'SR860': SR860,
                     'SR830': SR830,
                     'Keithley2450': Keithley2450,
                     'Lakeshore336': LakeshoreModel336,
                     'Model 4G': M4G,
                     }
