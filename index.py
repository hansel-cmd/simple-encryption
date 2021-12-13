print("hello world")



class Encryption():

    # Alphabets
    alphabets = 'abcdefghijklmnopqrstuvwxyz'

    def __init__(self):
        pass

    def encrypt(self, message):
        word_list = message.split(' ')
        for word in word_list:
            self.rotate(word)
    
    def rotate(word):
        for char in word:
            print("hello")


    
# me = Encryption()


alphabets = "abcdefghijklmnopqrstuvwxyz"


test = "hello world, hahah! oh my god@ wtf are u doing bruh*!?"


test_list = test.split(' ')

for char in test_list[0]:
    print(char, end='')
    if char.isalpha():
        print('alphabet')