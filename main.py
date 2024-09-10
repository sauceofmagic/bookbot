#alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_counts = get_num_char(text)
    print(f"{num_words} words found in the document")
    count_a = character_counts.get('a', 0)  # Using get to avoid KeyError if 'a' is not in the dictionary
    print(f"Count of letters: {character_counts}")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_char(text):
    text = text.lower()
    char_count = {}

    for char in text:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count


def get_book_text(path):
    with open(path) as f:
        return f.read()


if __name__ == "__main__":
    main()

