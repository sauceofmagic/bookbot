#alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_counts = get_num_char(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    
    # Find the count of the letter 'a'
    count_a = next((entry['num'] for entry in character_counts if entry['character'] == 'a'), 0)

    print(f"Count of 'a': {count_a}")

    for entry in character_counts:
        print(f"The '{entry['character']}' character was found {entry['num']} times")
    
    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_char(text):
    text = text.lower()
    char_count = {}
    # Counting the characters
    for char in text:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    # Getting characters dictionary into a list of dictionaries for sorting
    char_list = []
    for char, count in char_count.items():
        char_list.append({"character": char, "num": count})

    # Sorting the list of dictionaries based on num value
    char_list.sort(key=lambda x: x['num'], reverse=True)
    
    return char_list


def get_book_text(path):
    with open(path) as f:
        return f.read()


if __name__ == "__main__":
    main()

