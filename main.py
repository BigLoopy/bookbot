def main():
    book_to_analyze = "books/frankenstein.txt"
    text = get_book_text(book_to_analyze)
    word_count = count_words(text)
    letters = get_letter_count(text)

    print(f"--- Begin report of {book_to_analyze} ---")
    print(f"{word_count} words found in the document")
    print_letters_in_order(letters)

def get_book_text(path):
    with open("books/frankenstein.txt") as f:
        return f.read()
    
def count_words(text_to_count):
    return len(text_to_count.split())

def get_letter_count(text):
    letters = {}
    for letter in text.lower():
        if (letter not in letters):
            letters[letter] = 0
        letters[letter] += 1

    #print(letters)
    letters_list = []
    for letter in letters:
        letters_list.append({"letter":letter, "count": letters[letter]})

    #print(letters_list)
    return letters_list

def sort_on(dict):
    #print(dict["count"])
    return dict["count"]

def print_letters_in_order(letters):
    letters.sort(reverse=True,key=sort_on)
    for letter in letters:
        if (letter["letter"].isalpha()):
            print(f"The '{letter["letter"]}' character was found {letter["count"]} times")
    
    


main()

