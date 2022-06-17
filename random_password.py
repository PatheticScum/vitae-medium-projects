import random

lower = "qwertyuiopasdfghjklzxcvbnm"

upper = "QWERTYUIOPASDFGHJKLZXCVBNM"

symbol = "[]{}()=+-_"

number = "0123456789"

outcome = lower + upper + symbol + number

length = 9

password = "".join(random.sample(outcome, length))
print("The password you generated: ", password)
