def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    text = text.lower()
    character_count = {}
    for character in text:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return character_count

def get_sorted(d):
    return d["num"]

def char_dict_sorted(num_chars_dict):
    sorted_list = []
    for c in num_chars_dict:
        sorted_list.append({"char": c, "num": num_chars_dict[c]})
    sorted_list.sort(reverse=True, key=get_sorted)
    return sorted_list

