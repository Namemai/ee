
from bot import OverPoll
import threading
def login(resp, auth):
    bot = OverPoll(resp, auth)

threading.Thread(target=login, args=("client1","EQlqiyAbvpbaC1mRTXna.6YAlxRoBiuWsWmMO3zlrsG.NfEa6BqtVVYREkkvUijMLAkWD6GNAKT4TjTcB5q5wwJHa9BojiwoQ646Bj6f1/pP=")).start()
threading.Thread(target=login, args=("client2","EQ4s5LtNJerESY1HmeCa.c9LmlsiyQRgzhUGlZNb/EG.fCRyzxciGzWGVRR4BqLUbJtcglmjgzBttb7XIlHhfqcuQiI4T59Wa21b3POD6l58=")).start()
threading.Thread(target=login, args=("client3","EQl9Sqp44X9LPlYM4uNe.IgXDmaTHkrYL1znDJ1xypG.6M3XHir2bjCllCBpNTHAKijnD5ftmxpRH5Zf+7IzeQSq0z4zNN6MVYLKYciIvdch=")).start()
threading.Thread(target=login, args=("client4","EQ8M8n3V4PJyRufWT0j9.ZuiY4NJ7RVhq5MYUQZC8gq.zCoArvu8y1i7bBkddpeZ7lAg0jOXCzhKp19MgKZKma45FiWeqbZgzKKVby3NRurY=")).start()
threading.Thread(target=login, args=("client5","EQfauAtUvon2KhgbP2L9.NZRizCD1AxS0Y7UngEhsUq.BNyNy7gYpkZC0Xsfhu7NUI3DkW9RCUgWH+gdg7V5g6mMyp+QZLfph9mHMB/f+nW+=")).start()
threading.Thread(target=login, args=("client6","EQUCCy8Ab6HFLL31RRn4.spUm8672KnRV8OpyEW085a.FLJNqhKYJlhiL3ygtXTK7eJUqFZw3Pk91i0ZJNFvvvFsWqK6xpsYrlwK1OGhkxw6=")).start()
threading.Thread(target=login, args=("client7","EQnCkj9PmrFWkde8pXP7.9JP173BZR7RvIhsxJxLFrW.g0XsH2dfMzKSokxRLYy4x4qpzuT35WE1MnwMJL2wDbe+/YeJkfn/OgGWmZH+jI08=")).start()
print("LOGIN SUCCES.!!")
