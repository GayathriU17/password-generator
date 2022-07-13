#password generator
import string
import random
lc=[]
sym=[]
num=[]
for letter in string.ascii_lowercase:
    lc.append(letter)

for letter in string.ascii_uppercase:
    lc.append(letter)

sym=['@', '#', '$', '^', '&', '*', '(', ')', '-', '+']
num=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

num_a=int(input('How many letters do you want in the password?'))
num_num=int(input('How many numbers do you want in the password?'))
num_sym=int(input('How many symbols do you want in the password?'))

pw=[]

for i in range(num_a):
    pw.append(random.choice(lc))

for i in range(num_sym):
    pw.append(random.choice(sym))

for i in range(num_num):
    pw.append(random.choice(num))

pw_new=''.join((map(str, pw)))
print(pw_new)

