#####################################################################
# Author: Alexandra Yuhas
# Username: yuhasa
#
# Assignment: P0: Final Project
#
# Purpose: This file creates a class called Decrypt which is used to decrypt encrypted ciphers.
######################################################################
# Acknowledgements: Dr. Scott Heggen for a LOT of help.
#
#  Coding help from:
#   https://www.quora.com/How-do-I-count-the-frequency-of-different-letters-that-are-in-a-text-file-python-and-display-the-amount-on-a-list
#   https://docs.python.org/3/howto/sorting.html
#   https://inventwithpython.com/hacking/chapter20.html
# General Idea help from:
#   http://scottbryce.com/cryptograms/stats.htm
#   https://en.wikipedia.org/wiki/Letter_frequency
#   http://crypto.interactive-maths.com/frequency-analysis-breaking-the-code.html#encrypt
# Original Project:
#   A8: Ciphers
#   Most of this code is not from A8. However, the import and export methods are directly from A8.
#   A8 provided me with the idea and motivation to complete this project.
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################
import copy   # I need to make a deepcopy later in the program, so I had to import copy
import time   # I used the sleep function so I had to import time.

class Decrypt:
    """
    This begins the class definition for my new class, Decrypt.
    """

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, input_file = "message_input.txt"):
        """
        A constructor for the Decrypt class

        :param input_file: The file to be decrypted
        """
        self.input_file = input_file                         # The file to be decrypted
        self.cipher = ""                                     # A placeholder for the cipher
        self.import_file()                                   # This calls the import_file method
        self.message = ""

    def import_file(self):
        """
        Imports a file stored in the variable self.input_file

        :return: a string representing the contents of the file
        """
        f = open(self.input_file, "r")
        self.cipher = f.read()                   # Set self.cipher to the file contents
        f.close()

    def export_file(self, text_to_export, filename):
        """
        Exports a file called filename

        :param text_to_export: the string to be written to the exported file
        :param filename: a string representing the name of the file to be exported to
        """
        f = open(filename, "w")
        f.write(text_to_export)
        f.close()
        print("File exported to " + filename)

    def frequency(self, cipher, alphabet):
        """
        Takes a cipher, performs frequency analysis to decrypt cipher, returns decrypted message.
        :param cipher: the encrypted file
        :param alphabet: the alphabet so we can interate through it
        :return: None
        """

        d = {}
        for letter in alphabet:   # This for loop takes every letter in the alphabet and puts it into the dictionary with a value of 0.
            d[letter] = 0
        for letter in cipher:     # This for loop then iterates through the cipher and if the letter is in the cipher, it changes the value in the dictionary to the number of times the letter shows up in the cipher.
            if letter in d:
                d[letter] = d.get(letter, 0) + 1
        letter_freq = {}
        for letter in alphabet:   # This for loop adds the letters that are in and not in the cipher to this new dictionary
            if d.get(letter, 0) not in letter_freq:
                letter_freq[d[letter]] = [letter]
            else:
                letter_freq[d[letter]].append(letter)
        freq_tuples = list(letter_freq.items()) # Then we create a list of tuples of the frequencies and letters, so we can see which letters go with which frequencies.
        freq_tuples.sort()  # This sorts the list so that we can see it from least to greatest so we can see which letters appear the most often.
        self.message = copy.deepcopy(self.cipher)
        S = {'S':'e', 'H':'t', 'C':'o', 'O':'a', 'W':'i', 'B':'n','G':'s', 'V':'h', 'F':'r', 'Z':'l','Q':'c','I':'u','R':'d', 'T':'f', 'D':'p', 'A':'m','M':'y','K':'w','U':'g','J':'v','P':'b','Y':'k','L':'x','E':'q','X':'j'}
        # The dictionary S takes the old letters (uppercase) that appear the most often and pairs them with the new letters (lowercase) that are supposed to appear the most often in the English language
        for letter in S:  # This for loop iterates through S and replaces all the old letters with the new letters in self.message (a copy of the cipher).
            self.message = self.message.replace(letter, S[letter])
        time.sleep(3)
        print("If my analysis is correct (we'll just assume it is, because I am a genuis computer), Caesar's message should read something like this:")
        print()
        print(self.message) # This prints the now decrypted message.



def main():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print("Hi human! I am the decrypter machine.")
    print()
    print("I recently received an encrypted message meant for a friend of Caesar's.")
    print()
    user_input = input("I would like to read it. Would you? Type Y or N")
    print()
    if user_input == 'N':
        print("Wow. OK. I see how it is. Looks like we aren't going to have any fun today.")
        quit()
    else:
        print("I'm just going to assume your answer meant yes. Here goes! Lets see what little old Caesar is up to.")
        print()
        cipher0 = Decrypt("cipher_to_friend_2.txt")
        cipher0.frequency(cipher0.cipher, alphabet)
        print("Thanks for checking out my decryption skilllllz. I appreciate it. Have a merry Christmas!!")

main()


