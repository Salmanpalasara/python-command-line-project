import random

lower = "qwertyuioplkjhgfdsazxcvbnm"
upper = "ZXCVBNMLKOPIJHUYGTFRDESWAQ"
number = "0123456789"
symbol = "!@#$%^&*()_-+={|}:;/"

common = lower+upper+number+symbol

length = int(input("Enter a length of the password :-> "))

password = "".join(random.sample(common,length))

print("Password :-> ",password)
