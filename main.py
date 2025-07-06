import sys
from stats import get_no_of_words, no_of_characters, sort_on, convert_to_list

def get_book_text(filepath): 
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath= sys.argv[1]
    no_of_words = get_no_of_words(filepath)
    print(f"{no_of_words} words found in the document")
    no_of_char = no_of_characters(filepath)
    # Convert dictionary to list
    list_of_chars = convert_to_list(no_of_char)
    # Sort the list
    # Sort the list first
    list_of_chars.sort(reverse=True, key=sort_on)

    # Print the word count in the right format
    print(f"Found {no_of_words} total words")

    # Loop through and print each character count
    for char_dict in list_of_chars:
        char = char_dict["char"]
        count = char_dict["num"]
        # Only print if it's an alphabetical character
        if char.isalpha():
            print(f"{char}: {count}")

main()