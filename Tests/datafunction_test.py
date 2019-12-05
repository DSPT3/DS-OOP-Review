import datafunctions as dfn

def test_increment():

def increment(x):
    return(x + 1)

def min_max_scaler(x):
    """Returns numpy array with original values scaled"""
    return (x - x.min()) / (x.max() - x.min())

def strip_punctuation(text):
    exclude = string.punctuation
    return ''.join(s for s in text if s not in exclude)

def bag_of_words(text):
    text = strip_punctuation(text)
    words = set(text.split(' '))
    return wordsasser dfn.increment(2)  == 3
    