def main():
    path = "books/frankenstein.txt"
    text = get_text(path)
    word_count = get_word_count(path)
    char_count = count_letters(text)
    list_char = dict_list(char_count)
    print(f"--- Begin count of book {path} ---")
    print(f"{word_count} words were found in this book.\n")
    char_count_log(list_char)
    print("\nEnd of Report.")


def get_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(path):
    word_count = 0
    word_list = get_text(path).split()
    for word in word_list:
        word_count += 1
    return word_count

def count_letters(text):
    letters = {}
    words = text.lower()
    for word in words:
        if word in letters:
            letters[word] += 1
        else:
            letters[word] = 1
    return letters

def dict_list(char_count):
    list_of_dict = []
    for k, v in char_count.items():
        if k.isalpha():
            list_of_dict.append({'letter': k, 'number': v})
    list_of_dict.sort(key=lambda x: x['number'], reverse=True)
    return list_of_dict


def char_count_log(list_char):

    for char_dict in list_char:
        print(f"The letter '{char_dict['letter']}' was found {char_dict['number']} times")





main()



