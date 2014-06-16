from sys import argv

script, filename = argv

def get_list_from_line(line, my_file):
    #for line in my_file:
    line = line.rstrip().lower()
    words = line.rsplit(' ')
    return words

# def remove_punctuation(words):
#     for word in words:
#         while ord(word[-1]) < 97:
#             word = word[0:-1] 
#     return words

# def replace_puncuation_with_space(my_file):
#     for character in my_file:
#         character = character.lower
#         if ord(character) < 97 or ord(character) > 122:
#             character = " "
#     return my_file
    

def update_dictionary(words, word_count):
    for word in words:
        #word = word.strip(';:,.-"!?_)')#dict.setdefault will set dict[key] = default if key is not in dictionary
        # it will insert the key into the dictionary if not there

        # if word.isalpha():
        word_count[word] = word_count.setdefault(word, 0) + 1
        #elif "'" in word:
            #word_count[word] = word_count.setdefault(word, 0) + 1
        # if "--" in word:
        #     separate_hyphens = word.rsplit("--")
        #     for separate_words in separate_hyphens:
        #          word_count[separate_words] = word_count.setdefault(separate_words, 0) + 1

    return word_count

def print_counts(word_count):
      # In Python, you don't have to define variables before using them. key, value
    for key, value in sorted(word_count.items()):
        print key, value


def main():
    my_file = open(filename)

    #my_file = replace_puncuation_with_space(my_file)

    word_count = {}

    for line in my_file:
        update_dictionary(get_list_from_line(line, my_file),word_count)
        
    print_counts(word_count)

  

if __name__ == '__main__':
     main() 
