import win32com.client
import time

from ReadWriteMemory import ReadWriteMemory

rwm = ReadWriteMemory()
FAF_NAME = "ForgedAlliance.exe"

process = rwm.get_process_by_name(FAF_NAME)
process.open()
# process.kill()

# health_pointer= process.get_pointer(0x004e4dbc, offsets=[0xf4])
# x_pointer = process.get_pointer(0x699FE50)
# print(0x699FE50)
# print(x_pointer)
PT_TIME = 0x236E8FE8

# health = process.read(health_pointer)
# x = process.read(x_pointer)

PT_MASS_MAX = [
        0x1C6126B8,
        0x1C9DC7C8,
        0x1D5B7330,
]
PT_MASS_INCOME = [
        0x19d69408,
        0x19d694c8
]

PT_E_INCOME_STR = [
        0x2176cd25,
        0x235cc625
]

addresses = PT_E_INCOME_STR

# health_pointer = process.get_pointer(0x004e4dbc, offsets=[0xf4])

power_300 = 3158067

while True:
    for adr in addresses:
        mem = process.read(adr)
        print(mem)
        # val = str(mem)
        # process.write(adr, power_300)

    time.sleep(0.2)
