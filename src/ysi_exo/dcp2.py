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
    COMMAND_PARA = "para"
    COMMAND_DATA = "data"
    COMMAND_SETECHO = "setecho" # possible parameters 0 (disable echo) or 1
    COMMAND_TIME = "time"
    RETURN_CHAR = "\r"

    # Returns by the DCP2 Serial.
    RETURN_OK = "OK"
    RETURN_Unknown = "?Command"

    INITIALIZATION_DELAY = 0.1
    READING_DELAY = 0.3 # delay after writing for reading (s).

    def __init__(self, serial_port=SERIAL_PORT, baudrate=BAUDRATE):
        """Initialization of the serial port and parameters."""

        # Initialization of the serial port.
        self.serial = serial.Serial(serial_port, baudrate,
            timeout=SERIAL_TIMEOUT)
        time.sleep(self.INITIALIZATION_DELAY)

        # Clearing buffer if any.
        self.serial.read(self.serial.inWaiting())
        time.sleep(self.INITIALIZATION_DELAY)

        # Disabling echo.
        while not self._disable_echo():
            time.sleep(self.INITIALIZATION_DELAY)

        # Read the parameters
        self._initialize_read()

    def read_parameters(self):
        """Read parameters that are returned when reading data (echo off)."""

        raw_line = self._sonde_read(self.COMMAND_PARA)
        self.parameters = map(int, raw_line.split())

    def read_data(self):
        """Read data (echo off)."""

        data = self._sonde_read(self.COMMAND_DATA)
        self.data = map(float, data.split())

    def _sonde_read(self, command):
        """Read sonde response after request defined by command."""

        self.serial.write(command + self.RETURN_CHAR)
        time.sleep(self.READING_DELAY)

        data = self.serial.read(self.serial.inWaiting())

        return data

    def _disable_echo(self):
        self.serial.write(self.COMMAND_SETECHO + " " + "0" + self.RETURN_CHAR)
        time.sleep(self.READING_DELAY)
        raw_line = self.serial.read(self.serial.inWaiting())
        return self.RETURN_OK in raw_line

    def set_time(self, epoch_time):
        current_time_ysi_format = convert_epoch_to_date(epoch_time)
        self.serial.write(self.COMMAND_TIME + " " + 
            current_time_ysi_format + self.RETURN_CHAR)
        time.sleep(self.INITIALIZATION_DELAY)
        raw_line = self.serial.read(self.serial.inWaiting())
        return self.RETURN_OK in raw_line
