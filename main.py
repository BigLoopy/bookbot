def main():
    book_to_analyze = "books/frankenstein.txt"
    text = get_book_text(book_to_analyze)
    word_count = count_words(text)
    letters = get_letter_count(text)

    print(f"analyzing {book_to_analyze}")
    print(f"Number of words: {word_count}")
    print(f"Letter Counts: {letters}")

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

    return letters

main()

