def count_words(text_string):
    words = text_string.split()
    return len(words)

def count_chars(text):
    text = text.lower()
    counts = {}
    for ch in text:
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1
    return counts
