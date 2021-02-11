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

    >>> wf=WordFinder("simple.txt")
    3 words read.

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    """

    def __init__(self, path):
        """Read dictionary and reports # items read."""

        txt_file = open(path, 'r')

        self.path = path
        self.words = self.populate_words_list(txt_file)

        print(f"{len(self.words)} words read.")

    def __repr__(self):
        """Show representation."""
        return f"<WordsFinder path={self.path} num_words={len(self.words)}>"

    def populate_words_list(self, file):
        """Reads words from txt and adds to words list on instance."""
        return [line.strip() for line in file]

    def random(self):
        """
        Returns a random word from the list of words harvested from the txt file.
        """
        return choice(self.words)


class SpecialWordFinder(WordFinder):
    """
    Subclass of WordFinder enabling parsing of txt files contianing blank rows and # comments.

    --> no additional attributes

    >>> swf=SpecialWordFinder('other_words.txt')
    4 words read.

    >>> swf.random() in ["kale", "parsnips", "apple", "mango"]
    True

    >>> swf.random() in ["kale", "parsnips", "apple", "mango"]
    True

    >>> swf.random() in ["kale", "parsnips", "apple", "mango"]
    True
    """

    def __init__(self, path):
        super().__init__(path)

    def populate_words_list(self, file):
        """Parse txt_file -> list of words, skipping blanks/comments."""
        return [line.strip() for line in file if not line.startswith('#') and line.strip()]
