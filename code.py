import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
digits = [1,2,3,4,5,6,7,8,9,0]
symbols = ['!','@','#','$','&','*']

letters_length = int(input("enter the no of letters:"))
symbols_length = int(input("enter the no of symbols:"))
digits_length = int(input("enter the no of digits:"))

password_list =[]

for i in range(0, letters_length):
    password_list.append(random.choice(letters))

for i in range(0, symbols_length):
    password_list.append(random.choice(symbols))

for i in range(0, digits_length):
    password_list.append(random.choice(digits))

print(password_list)
random.shuffle(password_list)
password = ''
for pas in password_list:
    password = password + str(pas)
print(password)
