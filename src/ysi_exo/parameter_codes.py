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
COND_U = 5
SPCOND_U = 7
SAL = 12
TURBIDITY_FNU = 223
TSS_M = 190
PH_M = 17
PH = 18
ORP = 19
TDS_M = 110
PRESS_PSIA = 20
DEPTH_M = 22
CHLOROPHYLL_U = 193
CHLOROPHYLL_RFU = 194
ODO_PERC_SAT = 211
ODO_PERC_LOCAL = 214
ODO_MG = 212
BGAPE_U = 226
FDOM_RFU = 227
TEMP_F = 2
TDS_G = 10
BATTERY = 28
NH3 = 47
NH4 = 48
CL_MG = 112
BGAPC_RFU = 216
NLFCOND_U = 238
CABLE = 230
POSITION_M = 240

DATE_FORMAT = {DATE_DD: "%d%m%y", DATE_MM: "%m%d%y", DATE_YY: "%y%m%d"}
TIME_FORMAT = "%H%M%S"
TIME_FORMAT_YSI = "%H:%M:%S"

PARAM_STRINGS = {\
    u'Date (MM/DD/YYYY)' : DATE_MM,
    u'Date (DD/MM/YYYY)' : DATE_DD,
    u'Date (YYYY/MM/DD)' : DATE_YY,
    u'Time (HH:mm:ss)' : TIME,
    #u'Time (Fract. Sec)' : , 
    #u'Site Name' : ,
    u'Chlorophyll RFU' : CHLOROPHYLL_RFU, 
    u'Cond \xb5S/cm' : COND_U,
    u'Depth m' : DEPTH_M, 
    u'nLF Cond \xb5S/cm' : NLFCOND_U, 
    u'ODO % sat' : ODO_PERC_SAT, 
    u'ODO % local' : ODO_PERC_LOCAL, 
    u'ODO mg/L' : ODO_MG, 
    u'Pressure psi a' : PRESS_PSIA,
    u'Sal psu' : SAL, 
    u'SpCond \xb5S/cm' : SPCOND_U, 
    u'TAL PC RFU' : BGAPC_RFU,
    u'TDS mg/L' : TDS_M, 
    u'Turbidity FNU' : TURBIDITY_FNU, 
    u'TSS mg/L' : TSS_M,
    u'pH' : PH,
    u'pH mV' : PH_M, 
    u'Temp \xb0C' : TEMP_C, 
    u'Vertical Position m' : POSITION_M, 
    u'Battery V' : BATTERY, 
    u'Cable Pwr V' : CABLE
}
