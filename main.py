from stats import word_count,char_count



def get_book_text(path) -> str:
    with open(path) as f:
        file_contents = f.read()
        return file_contents


def main() :
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    word_count(text)
    print(char_count(text))
main()
