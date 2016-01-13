from random import choice
from sys import argv


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    contents = open(file_path).read()
    return contents

    
def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}

    texty = text_string.split()
    for i in range(len(texty) - 2):
        # import pdb 
        # pdb.set_trace()
        key = (texty[i],texty[i + 1])
        if key in chains:
            chains[key].append(texty[i + 2])
        else: chains[key] = [texty[i + 2],]

    # print chains
    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    rand_key = choice(chains.keys())
    text = rand_key[0] + " " + rand_key[1]
    new_key = (rand_key[1], choice(chains[rand_key]))
    
    try:
        while  True:
            text = text + " " + new_key[1]
            new_key = (new_key[1],choice(chains[new_key]))
        
    except KeyError: 
        return text


if len(argv) == 2:
    input_path = argv[1]

    # Open the file and turn it into one long string
    input_text = open_and_read_file(input_path)

    # Get a Markov chain
    chains = make_chains(input_text)

    # Produce random text
    random_text = make_text(chains)

    print random_text

else:
    print "Please provide a script and text file."
