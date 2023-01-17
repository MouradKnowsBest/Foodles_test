from collections import Counter
from itertools import islice
import unittest

def take_n_elements_from_dict(n, dict):
    return list(islice(dict, n))

def frequency_of_word_in_sentence(sentence, n):
    
    if (not sentence) or (sentence == ""):
        print("sorry there is no sentence entered !  Please enter a sentence")
    else:
        sorted_sentence_list = sorted([word for word in sentence.split()])
        
        counter = Counter(sorted_sentence_list)

        sorted_and_ordered_sentence_list = dict(sorted(counter.items(), key=lambda item: item[1], reverse=True))
                    
        return take_n_elements_from_dict(n, sorted_and_ordered_sentence_list.items())
        

    
if __name__ == "__main__":
    frequency_of_word_in_sentence("", 3)
    frequency_of_word_in_sentence("baz bar foo foo zblah zblah zblah baz toto bar", 3)
    print(frequency_of_word_in_sentence("baz bar foo foo zblah zblah zblah baz toto bar", 3))
 