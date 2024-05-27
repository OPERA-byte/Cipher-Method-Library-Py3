

class Vigenere:
    dictionary_key = ''
    base_alphabet = []
    ciphered_dictionary = []
    key_stream = ''

    def __init__(self, dictionary_key='SATOR'):
        self.dictionary_key = dictionary_key
    def preapend_dictionary_key_to_base_alphabet(self, dictionary_key):
        alphabet = (["A", "B", "C", "D", "E", "F",
                     "G", "H", "I", "J", "K", "L", "M",
                     "N", "O", "P", "Q", "R", "S", "T",
                     "U", "V", "W", "X", "Y", "Z"])
        temp_character = ''
        for i in range(len(dictionary_key)):
            temp_character = dictionary_key[(len(dictionary_key) - 1) - i]
            alphabet.remove(temp_character)
            alphabet.insert(0, temp_character)
        return alphabet

    def print_vigenere_table(self):
        for i in range(len(self.ciphered_dictionary)):
            print("     " + self.ciphered_dictionary[i])

    def construct_vigenere_table(self, base_alphabet):
        self.ciphered_dictionary.clear()
        temp_character = ''
        self.ciphered_dictionary.append(''.join(base_alphabet))
        for i in range(len(base_alphabet)-1):
            sub_set = []
            temp_character = base_alphabet[0]
            sub_set = base_alphabet[1:len(base_alphabet)]
            self.ciphered_dictionary.append(''.join(sub_set) + temp_character)
            base_alphabet.remove(temp_character)
            base_alphabet.append(temp_character)
        self.print_vigenere_table()

    def new_vigenere_table(self, dictionary_key='GLYPH'):
        self.dictionary_key = dictionary_key
        self.base_alphabet = self.preapend_dictionary_key_to_base_alphabet(self.dictionary_key)
        self.construct_vigenere_table(self.base_alphabet)

    def format_key_stream(self, key_stream, plain_text):
        plain_text_length = len(plain_text)
        key_stream_length = len(key_stream)
        temp_character = ''
        for i in range(plain_text_length - key_stream_length):
            temp_character = key_stream[i]
            key_stream += temp_character
        return key_stream

    # def encrypt(self, temp_key_stream, plain_text):
    #     self.key_stream = self.format_key_stream(temp_key_stream, plain_text)
    #     temp_plain_text_char = ''
    #     plain_text_int = -1
    #     key_stream_int = -1
    #     temp_cipher_text = ''
    #     cipher_text_arr = []
    #     for i in range(len(plain_text)):
    #         if not plain_text[i].isalpha():
    #             cipher_text_arr.append(plain_text[i])
    #         else:
    #             plain_text_int = self.ciphered_dictionary[0].index(plain_text[i])
    #             key_stream_int = self.ciphered_dictionary[0].index(self.key_stream[i])
    #             temp_cipher_text = self.ciphered_dictionary[plain_text_int][key_stream_int]
    #             cipher_text_arr.append(temp_cipher_text)
    #     return ''.join(cipher_text_arr)






# program = Vigenere()
# # base_alphabet = program.construct_vigenere_table(alphabet)
# # program.new_vigenere_table()
# word = program.encrypt("KEYWORD", "SECRET MESSAGE")
# print(word)





