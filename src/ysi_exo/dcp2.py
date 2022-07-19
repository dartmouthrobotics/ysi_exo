# -*- coding: utf-8 -*-
"""RS232 Driver for the DCP2 by YSI to interface with EXO multiparameter sonde.

Reading values using a DCP2.

More details at:
.. DCP2 guide:
   https://www.ysi.com/Product/id-599820/EXO-DCP-Signal-Output-Adapter-2-0

"""

import serial
import time

from ysi_exo.converter import Converter
from ysi_exo.parameter_codes import *
from ysi_exo.default_values import *


class Dcp2(Converter):
    """Interface with the DCP2 through serial.

    Attributes:
        serial (serial.Serial): serial port object.
        parameters (list): Order of how parameters are interpreted.
        data (list): array with data.
    """

    # Commands.
    COMMAND_PARA = "Para"
    COMMAND_DATA = "Data"
    RETURN_CHAR = "\r"

    READING_DELAY = 0.3 # delay after writing for reading (s).

    def __init__(self, serial_port=SERIAL_PORT, baudrate=BAUDRATE):
        """Initialization of the serial port and parameters."""

        # Initialization of the serial port.
        self.serial = serial.Serial(serial_port, baudrate,
            timeout=SERIAL_TIMEOUT)
        time.sleep(1)

        # Clearing buffer if any.
        self.serial.read(self.serial.inWaiting())
        time.sleep(1)

        # Read the parameters
        self._initialize_read()

    def read_parameters(self):
        """Read parameters that are returned when reading data."""

        raw_line = ""
        while not any(char.isdigit() for char in raw_line):
            raw_line = self._sonde_read(self.COMMAND_PARA)

        # 1 and -1, necessary to skip the command and the final #.
        self.parameters = map(int, raw_line.split()[1:-1])

    def read_data(self):
        """Read data."""

        data = self._sonde_read(self.COMMAND_DATA)
        self.data = map(float, data.split()[1:-1])

    def _sonde_read(self, command):
        """Read sonde response after request defined by command."""

        self.serial.write(command + self.RETURN_CHAR)
        time.sleep(self.READING_DELAY)

        return self.serial.read(self.serial.inWaiting())
