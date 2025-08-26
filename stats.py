def get_num_words(book):
    words = book.split()
    count = 0
    for word in words:
        count += 1
    return count

def count_characters(book):
    lowered_text = book.lower()
    char_count = {}
    count = 0
    for char in lowered_text:
        count = 0
        if char in char_count:
            count = char_count[char]
            char_count[char] = count+1
        elif char not in char_count:
            char_count[char] = count+1        
    return char_count

def sort_on(items):
    return items[1]
    
def sorted_dict(dict):
    sort_dict = list(dict.items())
    sort_dict.sort(reverse=True, key = sort_on)
    return sort_dict