import sys
text = input("Enter your password(or any text) to encrypt it : ")
encrypted = ""
for letter in text:
    if((ord(letter) >= 65 and ord(letter)<78) or (ord(letter) >= 97 and ord(letter) < 110)):
        encrypted += chr(ord(letter)+13)
    elif((ord(letter) >= 78 and ord(letter) < 97) or (ord(letter) >= 110 and ord(letter) <= 122)):
        encrypted += chr(ord(letter)-13)
    elif(ord(letter) >= 48 and ord(letter) < 53):
        encrypted += chr(ord(letter)+5)
    elif(ord(letter) >= 53 and ord(letter) <= 57):
        encrypted += chr(ord(letter)+5)
    elif(ord(letter) == 64):
        encrypted += chr(38)
    elif(ord(letter) == 32):
        print("Invalid text. \n 1. Maybe it contains space in between. \n Or \n 2. Maybe it contains invalid character(not a alphabet, digit or '@').")
        sys.exit("")
    else:
        encrypted += chr(ord(letter)+13)
print(encrypted)
