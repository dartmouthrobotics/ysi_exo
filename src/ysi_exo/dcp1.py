# -*- coding: utf-8 -*-
"""RS232 Driver for the DCP by YSI to interface with EXO multiparameter sonde.

Reading values using a DCP Modbus.

More details at:
.. DCP guide:
   https://www.ysi.com/Product/id-599825/EXO-Modbus-Signal-Output-Adapter

"""

import enum
import minimalmodbus
import time

from ysi_exo.converter import Converter
from ysi_exo.parameter_codes import *
from ysi_exo.default_values import *


class Dcp1(Converter):
    """Interface with the DCP through serial.

    Attributes:
        serial (minimalmodbus.Instrument): serial port object.
        parameters (list): Order of how parameters are interpreted.
        data (list): array with data.
        parameter_status (list): array with data status.
    """

    # REGISTERS (LENGTH 1).
    REGISTER_SAMPLE_PERIOD = 0
    REGISTER_FORCE_SAMPLE = 1
    REGISTER_FORCE_WIPE = 2

    REGISTER_PARAMETER_TYPE = range(128, 160)

    REGISTER_PARAMETER_STATUS = range(256, 288)

    class ParameterStatus(enum.Enum):
        """Enumerate of the parameter status."""
        AVAILABLE = 0
        NOT_SET = 1
        NOT_AVAILABLE = 2


    REGISTER_FLOAT_DATA = range(384, 448, 2)

    ADDRESS = 1

    BYTE_ORDER = minimalmodbus.BYTEORDER_LITTLE_SWAP
    NUMBER_OF_DECIMALS = 0

    def __init__(self, serial_port=SERIAL_PORT, baudrate=BAUDRATE,
            address=ADDRESS):
        """Initialization of the serial port and parameters."""

        # Initialization of the serial port.
        self.serial = minimalmodbus.Instrument(serial_port, address)
        time.sleep(1)
        self.serial.serial.baudrate = baudrate
        time.sleep(1)

        self._initialize_read()

    def read_parameters(self):
        """Read parameters that are returned when reading data.

        Read parameters from the registers. When the value is 0
        it means that no other values are stored.
        """

        self.parameters = []
        for register_parameter_type in self.REGISTER_PARAMETER_TYPE:
            parameter = self.serial.read_register(register_parameter_type,
                number_of_decimals=self.NUMBER_OF_DECIMALS)
            if parameter != 0:
                self.parameters.append(parameter)
            else:
                break

        self.data = [None] * len(self.parameters)
        self.parameter_status = [None] * len(self.parameters)

    def read_data(self):
        """Read data."""

        if self.parameters:
            for i in range(len(self.parameters)):
                data_value = self.serial.read_float(self.REGISTER_FLOAT_DATA[i], 
                    byteorder=self.BYTE_ORDER)
                self.data[i] = data_value

    def read_parameter_status(self):
        """Read parameter status."""

        if self.parameters:
            for i in xrange(len(self.parameters)):
                parameter_value = self.serial.read_register(self.REGISTER_PARAMETER_STATUS[i], 
                    number_of_decimals=self.NUMBER_OF_DECIMALS)
                self.parameter_status[i] = parameter_value
