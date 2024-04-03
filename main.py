def main():
    path_to_file = "books/frankenstein.txt" 
    file_contents = book_text(path_to_file)
    count = word_count(file_contents)
    letter_dir = letters(file_contents)
    sorted_letters = sort_letter(letter_dir)
    
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{count} words found in the document")
    for x in sorted_letters:
        print(f"The '{x["let"]}' character was found {x["num"]} times")
    print("--- End report ---")

def book_text(file_path):
    with open(file_path) as f:
        return f.read()

def word_count(book):
    return len(book.split())

def letters(file_contents):
    letters = {}
    lower_letter = file_contents.lower()
    for letter in lower_letter:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters

def sort_letter(letter_dir):
    sorted_letters = []
    for letter in letter_dir:
        if letter.isalpha():
            sorted_letters.append({"let" : letter, "num" : letter_dir[letter]})

    def sort_on(dict):
        return dict["num"]
    sorted_letters.sort(reverse=True, key=sort_on)
    return sorted_letters



main()



