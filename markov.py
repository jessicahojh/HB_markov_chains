"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    contents = open(file_path).read()

    return contents

print(open_and_read_file("green-eggs.txt"))

string_of_text = open_and_read_file("green-eggs.txt")

#print(type(string_of_text))


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """
    #contents = open((green-eggs.txt).read())

    words = text_string.split()

    chains = {}

    i = 0

    for i in range(len(words) - 2):
        pairs = (words[i], words[i + 1]) # pairs are made into a tuple
        value = words[i+2]
        print(pairs)
        print(value)



        # for pairs in words:
        #     chains[pairs] = chains.get(value) # list of possible next words


    print(chains)


    return chains


    # split words by space in between
    # get rid of \n by r.stripping
    # create for loop to take pairs of word
    # convert the pairs from list to tuple
    # sort the list of tuples (by keys)
    # make a list of possible words that go after the tuple

make_chains(string_of_text)


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    # loop over the dictionary
    # start at first tuple (reference the key) "Would, you"
    # choose random word from the list (from value)
    # then take word from key[1] and new random word to find the tuple that equals that

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
