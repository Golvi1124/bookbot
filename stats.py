def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    text = text.lower()
    char_counts = {}
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_on(item):
    return item["num"]

def sorted_chars(char_counts):
    # Make a list of dicts
    char_list = []
    for char, count in char_counts.items():
        if char.isalpha():  # only include letters
            char_list.append({"char": char, "num": count})
    
    # Sort the list by count, descending
    char_list.sort(reverse=True, key=sort_on)
    return char_list