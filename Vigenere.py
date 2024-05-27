

class Vigenere:
    """
       Vigenere cipher implementation.

       Attributes:
           dictionary_key (str): The key used to prepend to the base alphabet.
           base_alphabet (list): The base alphabet modified with dictionary key characters prepended.
           ciphered_dictionary (list): The Vigenere table containing the ciphered alphabet.
           key_stream (str): The formatted key stream matching the length of the plaintext.

    """
    dictionary_key = ''
    base_alphabet = []
    ciphered_dictionary = []
    key_stream = ''

    def __init__(self, dictionary_key='SATOR'):
        """
                Initialize the Vigenere cipher object with a dictionary key.

                Args:
                    dictionary_key (str, optional): The key to prepend to the base alphabet.
                        Defaults to 'SATOR'.

        """
        self.dictionary_key = dictionary_key
    def preapend_dictionary_key_to_base_alphabet(self, dictionary_key):
        """
            Prepend the characters of the dictionary key to the base alphabet.

            Args:
                dictionary_key (str): The key to prepend to the base alphabet.

            Returns:
                list: The modified base alphabet with dictionary key characters prepended.
        """
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
        """
            Print the Vigenere table.

            Prints each row of the Vigenere table contained in self.ciphered_dictionary.

        """
        for i in range(len(self.ciphered_dictionary)):
            print("     " + self.ciphered_dictionary[i])

    def construct_vigenere_table(self, base_alphabet):
        """
            Construct the Vigenere table using the provided base alphabet.

            Args:
                base_alphabet (list): The base alphabet used to construct the Vigenere table.
        """
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
        """
            Create a new Vigenere table using the specified dictionary key.

            Args:
                dictionary_key (str, optional): The key to prepend to the base alphabet.
                    Defaults to 'GLYPH'.

        """
        self.dictionary_key = dictionary_key
        self.base_alphabet = self.preapend_dictionary_key_to_base_alphabet(self.dictionary_key)
        self.construct_vigenere_table(self.base_alphabet)

    def format_key_stream(self, key_stream, plain_text):
        """
            Format the key stream to match the length of the plaintext.

            Args:
                key_stream (str): The key stream.
                plain_text (str): The plaintext.

            Returns:
                str: The formatted key stream.

        """
        plain_text_length = len(plain_text)
        key_stream_length = len(key_stream)
        temp_character = ''
        for i in range(plain_text_length - key_stream_length):
            temp_character = key_stream[i]
            key_stream += temp_character
        return key_stream




