# Please see the EXO User manual #603789REF Rev E pag. 77
# for corresponding codes.

# Timestamp from the sonde.
std_msgs/Header header

uint8[] parameters # List of parameters saved.
float32[] data # Corresponding data to each parameter; see the manual.
