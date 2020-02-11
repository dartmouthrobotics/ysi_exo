# -*- coding: utf-8 -*-
"""RS232 Driver for the DCP by YSI to interface with EXO multiparameter sonde.

Reading values using a DCP Modbus.

More details at:
.. DCP guide:
   https://www.ysi.com/Product/id-599825/EXO-Modbus-Signal-Output-Adapter

"""

from utilities import timestamp_available


class Converter(object):
    """Base class for converter from YSI proprietary signal to another signal.
    """

    def __init__(self):
        """Initialize the converter object to talk to the sonde."""
        raise NotImplementedError

    def _initialize_read(self):
        """Common method to initialize data structures for parameters."""
        # Read the parameters
        self.read_parameters()
        self.date_index, self.time_index = timestamp_available(self.parameters)

    def read_parameters(self):
        """Read parameters that are returned when reading data."""
        raise NotImplementedError

    def read_data(self):
        """Read data."""
        raise NotImplementedError
