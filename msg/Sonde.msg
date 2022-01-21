# Please see the EXO User manual #603789REF Rev E pag. 77
# for corresponding codes.

# Timestamp from the sonde.
std_msgs/Header header


uint8 DATE_DD = 51
uint8 DATE_MM = 52
uint8 DATE_YY = 53
uint8 TIME = 54
uint8 ODO_PERCSAT = 211
uint8 ODO_M = 212
uint8 TEMP_C = 1
uint8 COND_U = 5
uint8 SPCOND_U = 7
uint8 SAL = 12
uint8 TURBIDITY_FNU = 223
uint8 TSS_M = 190
uint8 PH_M = 17
uint8 PH = 18
uint8 ORP = 19
uint8 TDS_M = 110
uint8 PRESS_PSIA = 20
uint8 DEPTH_M = 22
uint8 CHLOROPHYLL_U = 193
uint8 CHLOROPHYLL_RFU = 194
uint8 ODO_PERC_SAT = 211
uint8 ODO_PERC_LOCAL = 214
uint8 ODO_MG = 212
uint8 BGAPE_U = 226
uint8 FDOM_RFU = 227
uint8 TEMP_F = 2
uint8 TDS_G = 10
uint8 BATTERY = 28
uint8 NH3 = 47
uint8 NH4 = 48
uint8 CL_MG = 112
uint8 BGAPC_RFU = 216
uint8 NLFCOND_U = 238
uint8 CABLE = 230

uint8[] parameters # List of parameters saved.
float32[] data # Corresponding data to each parameter; see the manual.
