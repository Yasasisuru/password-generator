import random
password=int(input("enter the length of password -"))
letter="abcdefghilklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%&*"
randomPw="".join(random.sample(letter,password))
print(randomPw)