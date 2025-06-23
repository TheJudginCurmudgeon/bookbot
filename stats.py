def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    character_count = {}
    text_lower = text.lower()
    for char in text_lower:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count

def sort_on(item):
    return item["num"]

def sorted_list(characters):
    sorted_dict = []
    for char, num in characters.items():
        if char.isalpha():
            sorted_dict.append({
                "char": char, "num": num
            })
    sorted_dict.sort(key=sort_on, reverse=True)
    return sorted_dict
    
