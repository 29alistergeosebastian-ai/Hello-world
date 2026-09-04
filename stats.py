def word_count(text:str):
    words = text.split()
    num_words = len(words)
    print(f"Found {num_words} total words")
   
def char_count(text:str) :
    char_dict = {}

    for char in text.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    print(char_dict)
