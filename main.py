def main():
       book_path = "books/frankenstein.txt"
       text = get_book_text(book_path)
       word_count = book_word_count(text)
       #print(f"word count is {word_count}")
       character_count = char_count(text)
       #print(character_count)
       char_list = dict_to_list(character_count)
       char_list.sort(reverse=True, key=sort_on)
       #print(char_list)
       report(word_count, char_list)



def get_book_text(path):
        with open(path) as f:
            return f.read()
                

def book_word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
      char_dict = {}
      lower_text = text.lower()
      count = 0
      for l in lower_text:
            if l.isalpha():
                if l not in char_dict:
                    char_dict[l] = 1
                else:
                  char_dict[l] += 1
      return char_dict

def dict_to_list(character_dict):
      char_list = []
      for c in character_dict:
            char_list.append({"character" : c , "num" : character_dict[c]})
      return char_list

def sort_on(list_dict):
      return list_dict["num"]

def report(word_count, list_dict):
     print("--- Begin report of books/frankenstein.txt ---")
     print(f"{word_count} words were found in the document.\n\n")
     for item in list_dict:
          print(f"The {item["character"]} was found {item["num"]} times.")
     return print("--- End report ---")
      
                  
            
main()