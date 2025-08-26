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
        