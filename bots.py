from bot import OverPoll
import threading
def login(resp, auth):
    bot = OverPoll(resp, auth)

threading.Thread(target=login, args=("client1","EQv0K3MBU1J8aOLFEj4a.6YAlxRoBiuWsWmMO3zlrsG.1MleXLGOCUa3F+aIniAEtxmj8Jrba8CUgd+0Tw5B2T8=")).start()
threading.Thread(target=login, args=("client2","EQ2PdhUNoUiVwtGo0aR9.ZuiY4NJ7RVhq5MYUQZC8gq.CWQOkullBgG2b45ATw1m/TmpUVQaZKPdLjeWBYeOqX8=")).start()
threading.Thread(target=login, args=("client3","EQQ7DuSX6swy9bbbHvy9.NZRizCD1AxS0Y7UngEhsUq.M6d/jVv9M4LWuhO3Be8+G67b/njPb0RHmVF5ypfViog=")).start()
threading.Thread(target=login, args=("client4","EQoQm7OYBcsXTHIrZhka.c9LmlsiyQRgzhUGlZNb/EG.oNZV1xyL293yqTXtt656aTiYSSZ5sLM18K9DUwEP5Ts=")).start()
print("USER LOGIN SUCCES.!!")
