# -*- coding: utf-8 -*-
"""Parameter codes used within YSI EXO multiparameter sonde.

Constants to be used to interpret the parameters from a YSI EXO.

More details at:
.. DCP guide:
   https://www.ysi.com/File%20Library/Documents/Guides/599825_Modbus-Quickstart-Guide.pdf

"""

DATE_DD = 51
DATE_MM = 52
DATE_YY = 53
TIME = 54
ODO_PERCSAT = 211
ODO_M = 212
TEMP_C = 1
SPCOND_U = 7
SAL = 12
TURBIDITY_FNU = 223
TSS_M = 190
PH = 18
ORP = 19
PRESS_PSIA = 20
DEPTH_M = 22
CHLOROPHYLL_U = 193
BGAPE_U = 226
FDOM_RFU = 227
TEMP_F = 2
TDS_G = 10
BATTERY = 28
NH3 = 47
NH4 = 48
CL_MG = 112
BGAPC = 216
NLFCOND_U = 238

DATE_FORMAT = {DATE_DD: "%d%m%y", DATE_MM: "%m%d%y", DATE_YY: "%y%m%d"}
TIME_FORMAT = "%H%M%S"
