def get_no_of_words(filepath):
    with open(filepath) as f: 
        text = f.read()
        words = text.split()
        no_of_words = len(words)    
        return no_of_words

def no_of_characters(filepath):
    with open(filepath) as f: 
        text = f.read()
        no_of_char = {}
        for char in text:
            char = char.lower()
            if char in no_of_char:
                no_of_char[char] += 1
            else:
                no_of_char[char] = 1
    # print(no_of_char)
    return no_of_char

def convert_to_list(char_dict):
    list_of_dicts = []
    for character, count in char_dict.items():
        new_dict = {"char": character, "num": count}
        list_of_dicts.append(new_dict)
    return list_of_dicts  # Return the whole list, not list_of_dicts["num"]

def sort_on(single_dict):
    return single_dict["num"]  # This gets called on each dictionary in the list