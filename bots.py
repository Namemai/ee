from bot import OverPoll
import threading
def login(resp, auth):
    bot = OverPoll(resp, auth)

threading.Thread(target=login, args=("client1","EQv0K3MBU1J8aOLFEj4a.6YAlxRoBiuWsWmMO3zlrsG.1MleXLGOCUa3F+aIniAEtxmj8Jrba8CUgd+0Tw5B2T8=")).start()
threading.Thread(target=login, args=("client2","EQ2PdhUNoUiVwtGo0aR9.ZuiY4NJ7RVhq5MYUQZC8gq.CWQOkullBgG2b45ATw1m/TmpUVQaZKPdLjeWBYeOqX8=")).start()
threading.Thread(target=login, args=("client3","EQQ7DuSX6swy9bbbHvy9.NZRizCD1AxS0Y7UngEhsUq.M6d/jVv9M4LWuhO3Be8+G67b/njPb0RHmVF5ypfViog=")).start()
threading.Thread(target=login, args=("client4","EQoQm7OYBcsXTHIrZhka.c9LmlsiyQRgzhUGlZNb/EG.oNZV1xyL293yqTXtt656aTiYSSZ5sLM18K9DUwEP5Ts=")).start()
threading.Thread(target=login, args=("client5","EQgrtWDAYYnqyYOay8R4.spUm8672KnRV8OpyEW085a.WpWZr7v4O8MP0nWZU3Xu8gwzxZuw+L9ot1c1jEaoC9s=")).start()
threading.Thread(target=login, args=("client6","EQQ7ojPkMnAjhNwbeq87.9JP173BZR7RvIhsxJxLFrW.44GIkRLLzhCGDHBKZsYU9+h8Lnig/wBKPcgF7sU/YpI=")).start()
threading.Thread(target=login, args=("client7","EQCUW6B14AU6IXSdqvKd.BhBt2iou452EqQ0WX2tgxq.NRcdWXEFOs6vsto5jg5aMcHAG9D8BIIjw4xxWKLJYmw=")).start()
threading.Thread(target=login, args=("client8","EQgjwR6y0dwvXWw6MhC9.D8a7trU8qYHeMP9wgPk56q.VW2pUJdF+7nFCTfYSMRkQ7KgdowuG4YvTk4uS3Zo9nI=")).start()
threading.Thread(target=login, args=("client9","EQtdUVBo0bnUuUUlP2Oe.IgXDmaTHkrYL1znDJ1xypG.j+CiLP5V4dNtW8cs35ngBA+2gvVnLenVIRX5Yn71nCw=")).start()
print("USER LOGIN SUCCES.!!")
