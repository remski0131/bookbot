def main():
    path = "books/frankenstein.txt"
    text = get_text(path)
    word_count = get_word_count(path)
    char_count = count_letters(text)
    print(char_count)


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


main()



