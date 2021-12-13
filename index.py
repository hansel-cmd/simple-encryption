print("hello world")



class Encryption():

    # Alphabets
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    vowels = "aeiou"

    def __init__(self):
        pass

    def encrypt(self, message):
        word_list = message.split(' ')

        encrypted_message = []
        for word in word_list:
            self.vowel_count = self.count_vowels(word)
            encrypted_message.append(self.rotate(word))
        
        return ' '.join(encrypted_message)

    def count_vowels(self, word):
        count = sum((*map(word.count, "aeiouAEIOU"), 0))
        return count if count else 13

    def rotate(self, word):
        rotated_word = []
        for char in word:
            if char.isalpha():
                rotated_word.append(self.swap_char(char))
            else:
                rotated_word.append(char)

        return rotated_word
    
    def swap_char(self, char):
        index = alphabets.find(char)
        return self.alphabets[(index + self.vowel_count) % len(alphabets)]
        



# me = Encryption()
# me.encrypt("hello world, hahaAaaah! oh my god@ wtf are u doing bruh*!?")


alphabets = "abcdefghijklmnopqrstuvwxyz"


test = "hello world, hahaAaaah! oh my god@ wtf are u doing bruh*!?"
test_list = test.split(' ')

# rotate is 13
rotate = 3
index = alphabets.find('x')


# for char in test_list[0]:
#     print(char, end=' ')
#     if char.isalpha():
#         ndx = alphabets.find(char)


# print(sum((*map(test_list[2].count, "aeiouAEIOU"), 0)))

te = ["hello", "oh", "my", "god"]
print(''.join(te))
