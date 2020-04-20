
from bot import OverPoll
import threading
def login(resp, auth):
    bot = OverPoll(resp, auth)

threading.Thread(target=login, args=("client1","EQ8CpzzqMhIRQax4m69e.tsWh/XhwZNQR/EYas4X8FG.Fv5f/rf+lNnH1u/We0D6FHv0m81QAYP8Qvvo2Xyj8AE=")).start()
threading.Thread(target=login, args=("client2","EQtBjlsLhyYE3AhQtVUd.ARAzAuWFaouOQmcAei0odq.HJtHiHbQTiMoJC/IQdXVoCXxoN80CqDZSw/VJkNpBo0=")).start()
threading.Thread(target=login, args=("client3","token")).start()
threading.Thread(target=login, args=("client4","token")).start()
threading.Thread(target=login, args=("client5","token")).start()
threading.Thread(target=login, args=("client6","token")).start()
threading.Thread(target=login, args=("client7","token")).start()
threading.Thread(target=login, args=("client8","token")).start()
threading.Thread(target=login, args=("client9","token")).start()
threading.Thread(target=login, args=("client10","token")).start()
print("USER LOGIN SUCCES.!!")
