import pyotp
import time

f = open("read.txt", "r")
totp = pyotp.TOTP(f.read())
code = totp.now()
print(f'Current OTP: {code}')
while (totp.verify(code)):
    time.sleep(1)
print('Expired.')
