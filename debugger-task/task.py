def calculate_word_lengths(text):
    """Calculates the lengths of words in a string."""
    words = list(text)
    lengths = []
    for word in words:
        lengths.append(len(word))
    return lengths
