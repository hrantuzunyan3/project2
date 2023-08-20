#import random

#papers = ['A','B','C']

#q_list = [random.choice(papers) for i in range(40)]
#print (q_list)


import random,string

password_length = int(input("provide the password length:"))

characters = string.ascii_letters + string.digits + string.punctuation

password = ""   

for index in range(password_length):
    password = password + random.choice(characters)

print("Password generated: {}".format(password))