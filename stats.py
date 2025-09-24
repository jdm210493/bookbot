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

def sorted_list(counts): # this function takes a dictionary called counts 
    keys_list = [] # it creates an empty list
    for k, v in counts.items(): # it loops through eack key-value pair
        if k.isalpha(): # if the key is an alphabetical character, it adds a dictionary to keys_list with the character and its count
            keys_list.append({"char": k, "num": v})

    def sort_on(item): # it defines a helper function sort_on that returns the "num" value from each dictionary
        return item["num"]

    keys_list.sort(reverse=True, key=sort_on) # it sorts keys_list in descending order by count using the helper function
    return keys_list # it returns the sorted list
