# Python 3 code to print MAC address, (physical address)
# in a formatted manner

import uuid
print ("Formatted MAC address : ")
print (':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff)
for elements in range(0,2*6,2)][::-1]))
print(hex(uuid.getnode()))
# f8:75:a4:66:97:ce
