import time
import os

alphabet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,1234567890!?@#$%^&*()';/.[]{}'<>"
sendmessage = ""

os.system('cls')
message = input("type your sentence: ")

for c in message:
    for a in alphabet:
        time.sleep(0.001)
        os.system('cls')
        print(sendmessage + a)
        if c == a:
            sendmessage += a
            break
            





