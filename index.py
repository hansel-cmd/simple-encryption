print("hello world")



class Encryption():

    # Alphabets
    alphabets = 'abcdefghijklmnopqrstuvwxyz'


    def __init__(self):
        pass

    def encrypt(self, message):
        word_list = message.split(' ')

        encrypted_message = []
        for word in word_list:
            encrypted_message.append(self.rotate(word))
        
        return encrypted_message.join()
    
    def rotate(self, word):
        rotated_word = []
        for char in word:
            if char.isalpha():
                rotated_word.append(self.swap_char(char))
            else:
                rotated_word.append(char)
    
    def swap_char(self, char):



    
# me = Encryption()


alphabets = "abcdefghijklmnopqrstuvwxyz"


test = "hello world, hahah! oh my god@ wtf are u doing bruh*!?"


test_list = test.split(' ')

for char in test_list[10]:
    print(char, end=' ')
    if char.isalpha():
        print('alphabet')