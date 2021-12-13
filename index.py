class Encryption():

    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    vowels = "aeiouAEIOU"

    def __init__(self): pass

    def encrypt(self, message):
        word_list = message.lower().split(' ')

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
        

class Decryption():

    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    vowels = "aeiouAEIOU"

    def __init__(self): pass

    def count_vowels(self, word):
        count = sum((*map(word.count, "AEIOU"), 0))
        return count if count else 13

    def decrypt(self, message):
        word_list = message.split(' ')

        decrypted_message = []
        for word in word_list:
            self.vowel_count = self.count_vowels(word)
            decrypted_message.append(''.join(self.rotate(word)))
        
        return ' '.join(decrypted_message)

    def rotate(self, word):
        rotated_word = []
        for char in word:
            if char.isalpha():
                if char.islower():
                    rotated_word.append(self.swap_char(char))
                else:
                    rotated_word.append(char.lower())
            else:
                rotated_word.append(char)

        return rotated_word

    def swap_char(self, char):
        index = self.alphabets.find(char)
        padding = index - self.vowel_count
        if padding < 0:
            padding = len(self.alphabets) + padding
        return self.alphabets[(padding)]




me = Encryption()
print(me.encrypt("If I Can't Save The One Small Girl In Front Of Me, How Can I Become A Hero That Saves Everyone?"))

you = Decryption()
print(you.decrypt("Ig I dAo'u uAxE uiE OpE tnAmm hIsm Io gsOou Og nE, iOx dAo I eEfOpE A jEtO uiAu uAxEu EzEvcOrE?"))

 