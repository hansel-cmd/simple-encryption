class Encryption():

    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    vowels = "aeiouAEIOU"

    def __init__(self): pass

    def encrypt(self, message):
        word_list = message.split(' ')

        encrypted_message = []
        for word in word_list:
            self.vowel_count = self.count_vowels(word)
            encrypted_message.append(''.join(self.rotate(word)))
        
        return ' '.join(encrypted_message)

    def count_vowels(self, word):
        count = sum((*map(word.count, "aeiouAEIOU"), 0))
        return count if count else 13

    def rotate(self, word):
        rotated_word = []
        for char in word:
            if char.isalpha():
                if char not in self.vowels:
                    rotated_word.append(self.swap_char(char))
                else:
                    rotated_word.append(char.upper())
            else:
                rotated_word.append(char)

        return rotated_word
    
    def swap_char(self, char):
        index = self.alphabets.find(char)
        return self.alphabets[(index + self.vowel_count) % len(self.alphabets)]
        

me = Encryption()
print(me.encrypt("Drink some water, reload your mags, and let's get back out there."))