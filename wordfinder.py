"""Word Finder: finds random words from a dictionary."""

from random import choice


class WordFinder:
    """
    Accesses a file containing words (one word per line), creates list of words, prints the number of words in the list, can produce a random word from the list.

    Attributes
    --------------------
    path: str
      the file path including filename of the txt file containing a list of words
    words: list
      the list of words extracted from the txt file of words
    """

    def __init__(self, path):
        self.path = path
        self.words = []
        self.populate_words_list()
        self.print_num_words()

    def __repr__(self):
        return f"<WordsFinder path={self.path} num_words={len(self.words)}>"

    def populate_words_list(self):
        self.words = []
        file = open(self.path, 'r')
        for line in file:
            self.words.append(line.strip())
        file.close()

    def print_num_words(self):
        print(f"{len(self.words)} words read.")

    def random(self):
        print(choice(self.words))


class SpecialWordFinder(WordFinder):
    """
    Subclass of WordFinder enabling parsing of txt files contianing blank rows and # comments.

    --> no additional attributes
    """

    def __init__(self, path):
        super().__init__(path)

    def populate_words_list(self):
        self.words = []
        file = open(self.path, 'r')
        for line in file:
            if not line.startswith('#') and line != "\n":
                self.words.append(line.strip())
        file.close()
