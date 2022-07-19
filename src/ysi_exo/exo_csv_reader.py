# -*- coding: utf-8 -*-
"""Reader of the CSV log from the EXO multiparameter sonde.

Reading values from the CSV log file export from Kor EXO.
An example file (with header) is in the test folder.

More details at:
.. EXO manual (page 62):
   https://www.ysi.com/File%20Library/Documents/Manuals/EXO-User-Manual-Web.pdf

"""

import io
import enum
import time

from ysi_exo.converter import Converter
from ysi_exo.parameter_codes import *
from ysi_exo.default_values import *


class ExoCsvReader(Converter):
    """Interface to read the log file.

    Attributes:
        parameters (list): Order of how parameters are interpreted.
        data (list): array with data.
    """
    FIRST_LINE_SEP_INDEX = -2 #"sep="
    ENCODING = 'utf_16_le'
    SKIP_NUM_LINES = 8
    TIME_SEP = ':'
    DATE_SEP = '/'
    DATE_ORDER = {\
            DATE_YY : [0, 1, 2],
            DATE_MM : [2, 0, 1],
            DATE_DD : [2, 1, 0]
    }

    def __init__(self, csv_file_path):
        """Initialization of the CSV reader.

        Implementation assumes header.
        
        """
        self.csv_file = io.open(csv_file_path, "r", encoding=self.ENCODING)

        self.sep = self.csv_file.readline()[self.FIRST_LINE_SEP_INDEX]
        self._skip_lines(self.SKIP_NUM_LINES)
        self.parameters_line = self.csv_file.readline().split(self.sep)

        # Initialization of the relevant entries.
        self._initialize_read()

    def read_parameters(self):
        """Read parameters that are in the log file."""

        self.parameters = []
        self.parameters_indices = []
        for i, parameter_type in enumerate(self.parameters_line):
            try:
                self.parameters.append(PARAM_STRINGS[parameter_type])
                self.parameters_indices.append(i)
            except KeyError:
                continue

        self.data = [None] * len(self.parameters)

    def read_data(self):
        """Read data."""

        if self.parameters:
            raw_data_list = self.csv_file.readline().split(self.sep)
            if not raw_data_list[0]:
                # If end of the line.
                raise RuntimeWarning
                return
            for i in xrange(len(self.parameters)):
                raw_data = raw_data_list[self.parameters_indices[i]]
                if self.parameters[i] == TIME:
                    self.data[i] = float(''.join(raw_data.split(self.TIME_SEP)))
                elif DATE_DD <= self.parameters[i] <= DATE_YY:
                    date_list = raw_data.split(self.DATE_SEP)
                    self.data[i] = self._date_to_float(date_list, self.parameters[i])
                else:
                    self.data[i] = float(raw_data)

    def _skip_lines(self, num_lines):
        """Skip lines."""

        for i in xrange(num_lines):
            self.csv_file.next()

    def _date_to_float(self, date_list, date_format):
        """Transform date from string to float."""
        order = self.DATE_ORDER[date_format]
        new_date_list = [None] * 3
        new_date_list[order[0]] = date_list[order[0]][-2:] # Year.
        new_date_list[order[1]] = date_list[order[1]].zfill(2) # Month.
        new_date_list[order[2]] = date_list[order[2]].zfill(2) # Day.
        

        return float(''.join(new_date_list))

    def _determine_encoding(self, first_line):
        """Determine encoding based on the first line (in bytes)."""
        import magic
        m = magic.open(magic.MAGIC_MIME_ENCODING)
        m.load()
        encoding = m.buffer(first_line)
        bom= codecs.BOM_UTF16_LE
        first_line = first_line[len(bom):]

