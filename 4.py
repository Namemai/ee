from bot import OverPoll
import threading
def login(resp, auth):
    bot = OverPoll(resp, auth)

threading.Thread(target=login, args=("client1","EQ8CpzzqMhIRQax4m69e.tsWh/XhwZNQR/EYas4X8FG.Fv5f/rf+lNnH1u/We0D6FHv0m81QAYP8Qvvo2Xyj8AE=")).start()
threading.Thread(target=login, args=("client2","EQtBjlsLhyYE3AhQtVUd.ARAzAuWFaouOQmcAei0odq.HJtHiHbQTiMoJC/IQdXVoCXxoN80CqDZSw/VJkNpBo0=")).start()
threading.Thread(target=login, args=("client3","EQlrHDNONo2uy9Rvm3f6.68J8xVmSlAPaErf1HvBFXG.v+BwNyRqWp8KdVWi35pVaJVcQmk+VC8uJxwaDlqozAE=")).start()
threading.Thread(target=login, args=("client4","EQQxRKRPurI8vzzQsnY1.6aDpR7WaeYIerTV/ke45mq.0PRosPlB7DLqx4bV16MgD2ombieWcjW9Z2T4CWsKmtk=")).start()
print("USER LOGIN SUCCES.!!")
