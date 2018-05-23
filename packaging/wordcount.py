import re
import sys

class WordCount:
    """ 
    Class used to count word, letter, character of an object. 
    """

    def __init__(self, filename):
        self.filename = filename

    def open_file(self, filename):
        """ open a file object """
        with open(filename, 'r') as f:
                content = f.read()
                return content

    def word_count(self):
        """ returns a file's word count"""
        wc = self.open_file(self.filename)
        self = len(wc.split())
        #return ("Words:",len(wc.split()))
        return ("Words:", self)

    def sentence_count(self):
        """ returns a file's sentence count"""
        sc = self.open_file(self.filename)

        return ("Sentences: ", sc.count('.') + sc.count('!') + sc.count('?'))

    def letter_count(self):
        """ returns a file's character count, excluding punctuation"""
        letter_count = 0

        pattern = r'[\W]' # exclude any punctuation

        cc_file = self.open_file(self.filename)

        total_words = cc_file.split()

        for word in total_words:
            for letter in word:
                if not re.search(pattern, letter):
                    letter_count +=1
        return ("Letters: ", letter_count)

    def counts(self):
        return (self.word_count(), '\n', self.sentence_count(), '\n', self.letter_count())

#print("__name__:", __name__)
#
#
#file='alice.txt'
#
#
#
#
#def word_count(file):
#    with open(file, 'r') as f:
#        content = f.read()
#        print(content.split())
#        print('Word count:', len(content.split()))
#
#def sentence_count(file):
#    with open(file, 'r') as f:
#        content = f.read()
#        print('Total sentences:    ', content.count('.'), '!', '?')
#

if __name__ == '__main__':
    alice = WordCount(sys.argv[1])
    print(WordCount.counts(alice))

    #word_count(file)
    #sentence_count(file)
