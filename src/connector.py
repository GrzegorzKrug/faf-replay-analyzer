import win32com.client as cli

import pywintypes
import win32pipe
import win32api

from win32 import win32process as process
from ReadWriteMemory import ReadWriteMemory

rwm = ReadWriteMemory()
FAF_NAME = "ForgedAlliance.exe"

p = rwm.get_process_by_name(FAF_NAME)
print(p)
pid = p.pid
print(pid)

# han = pywintypes.HANDLE(pid)
hand = win32api.OpenProcess(1, True, pid)
# han.start()
# win32pipe.GetNamedPipeServerProcessId(pid)
process.TerminateProcess(hand, 0)

# i = process.GetCurrentProcessId()
# i = process.EnumProcesses()
# print(i)
