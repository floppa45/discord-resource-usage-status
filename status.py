import psutil
from pypresence import Presence
import time

client_id = '898429395759407215'
RPC = Presence(client_id,pipe=0)
RPC.connect()

while True:
    cpu_per = round(psutil.cpu_percent(),1) 
    mem = psutil.virtual_memory()
    mem_per = round(psutil.virtual_memory().percent,1)
    print(RPC.update(details="RAM: "+str(mem_per)+"%", state="CPU: "+str(cpu_per)+"%", large_image = "31515"))
    time.sleep(15)